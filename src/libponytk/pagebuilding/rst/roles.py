import re, warnings

from docutils.parsers.rst import roles as docutilsroles

from . import nodes


ABBR_RE = re.compile(r'^([^(]+)( \((.*)\))?$')

def abbr_role(type, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Provides :role:`ABBR[ (EXPLANATION)]`.
    """
    mo = ABBR_RE.match(text)
    if mo is not None:
        abbr = mo.group(1)
        expl = None
        if len(mo.groups()) > 2:
            expl = mo.group(3)
            node = nodes.Abbreviation(abbr, abbr, explanation=expl)
        else:
            node = nodes.Abbreviation(abbr, abbr)
        return [node], []
    warnings.warn("Invalid pattern for abbr found: %s" % text)
    return content, []

def url_role(type, rawtext, text, lineno, inlines, options={}, content=[]):
    """
    Provides :url:`some url`
    """
    return [nodes.Url(text, text)], []

def file_role(type, rawtext, text, lineno, inlines, options={}, content=[]):
    """
    Provides :file:`some url`
    """
    return [nodes.File(text, text)], []

def command_role(type, rawtext, text, lineno, inlines, options={}, content=[]):
    """
    Provides :file:`some url`
    """
    return [nodes.Command(text, text)], []

docutilsroles.register_local_role('abbr', abbr_role)
docutilsroles.register_local_role('url', url_role)
docutilsroles.register_local_role('file', file_role)
docutilsroles.register_local_role('command', command_role)
