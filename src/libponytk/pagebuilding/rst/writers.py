from docutils.writers.html4css1 import Writer as BaseWriter, HTMLTranslator as BaseTranslator

class Writer(BaseWriter):
    def __init__(self, *args, **kwargs):
        BaseWriter.__init__(self, *args, **kwargs)
        self.translator_class = Translator

class AbbrTranslatorMixin:
    def visit_Abbreviation(self, node):
        attrs = {}
        if node.hasattr('explanation'):
            attrs['title'] = node['explanation']
        self.body.append(self.starttag(node, 'abbr', '', **attrs))

    def depart_Abbreviation(self, node):
        self.body.append('</abbr>')

class UrlTranslatorMixin:
    def visit_Url(self, node):
        attrs = {"class": "url"}
        self.body.append(self.starttag(node, 'span', '', **attrs))

    def depart_Url(self, node):
        self.body.append('</span>')

class FileTranslatorMixin:
    def visit_File(self, node):
        attrs = {"class": "file"}
        self.body.append(self.starttag(node, 'span', '', **attrs))

    def depart_File(self, node):
        self.body.append('</span>')

class CommandTranslatorMixin:
    def visit_Command(self, node):
        attrs = {'class': 'command'}
        self.body.append(self.starttag(node, 'span', '', **attrs))

    def depart_Command(self, node):
        self.body.append('</span>')

class Translator(FileTranslatorMixin, UrlTranslatorMixin, AbbrTranslatorMixin,
        CommandTranslatorMixin,
        BaseTranslator):
    pass
