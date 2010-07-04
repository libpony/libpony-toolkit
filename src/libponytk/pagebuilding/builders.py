import logging
import html5lib
from docutils.core import publish_parts

from .rst import Writer, pygments_addon, roles
from .structures import Page


class AbstractPageBuilder(object):
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__module__ + '.' + self.__class__.__name__)

    def __call__(self, data, **options):
        if isinstance(data, basestring):
            self.log.debug("Processing string:")
            self.log.debug(data)
            return self.build_string(data, **options)
        self.log.debug("Processing non-string -> file-like object")
        return self.build_file(data, **options)
    
    def split_body(self, parent_node):
        teaser_elems = []
        body_elems = []
        verdict_elems = []
        in_body = False
        in_verdict = False
        teaser = None
        body = None
        verdict = None
        nodelist = parent_node.childNodes
        
        if len(parent_node.getElementsByTagName("hr")) > 1:
            verdict_start = parent_node.getElementsByTagName("hr")[-1]
        else:
            verdict_start = None
        
        for elem in nodelist:
            if not in_body:
                if in_verdict:
                    verdict_elems.append(elem)
                else:
                    if elem.localName == 'hr':
                        in_body = True
                        continue
                    teaser_elems.append(elem)
            else:
                if elem == verdict_start:
                    in_verdict = True
                    in_body = False
                    continue
                body_elems.append(elem)
        teaser_html = self.innerHTML(teaser_elems)
        body_html = self.innerHTML(body_elems)
        if not len(body_elems):
            body = teaser_html.lstrip().rstrip()
        else:
            teaser = teaser_html.lstrip().rstrip()
            body = body_html.lstrip().rstrip()
        if len(verdict_elems):
            verdict = self.innerHTML(verdict_elems).strip()
        return (teaser, body, verdict)
        
    def split_html(self, html_text, body_selector=None):
        tree = html5lib.parse(html_text, treebuilder="dom")
        page = Page()
        titles = tree.getElementsByTagName("h1")
        if len(titles):
            page.title = self.innerHTML(titles[0])
            for title in titles:
                title.parentNode.removeChild(title)
        if body_selector is None:
            body = tree.getElementsByTagName("body")[0]
        else:
            body = body_selector(tree)
        separators = body.getElementsByTagName("hr")
        if len(separators):
            page.teaser, page.body, page.verdict = self.split_body(body)
        else:
            page.body = self.innerHTML(body).lstrip().rstrip()
        return page
                
    def innerHTML(self, node):
        if isinstance(node, list):
            return u"".join([x.toxml() for x in node])
        return u"".join([x.toxml() for x in node.childNodes])
        
    def build_file(self, data, **options):
        return self.build_string(data.read(), **options)
        
class RstPageBuilder(AbstractPageBuilder):
    def build_string(self, data, **options):
        doc = publish_parts(source=data, 
            writer=Writer(),
            settings_overrides={
                'initial_header_level': 2,
                'input_encoding': 'utf-8',
                'output_encoding': 'utf-8',
                })
        return self.split_html(doc['whole'], body_selector=self._body_selector)
        
    def _body_selector(self, tree):
        return tree.getElementsByTagName('div')[0]


