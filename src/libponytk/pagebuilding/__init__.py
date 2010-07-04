import codecs

from .builders import RstPageBuilder


DEFAULT_MAPPING = {
        'rst': RstPageBuilder
        }

def build(path, pagetype=None, typemapping=None):
    """
    Constructs a page out of the path to a file.
    """
    if pagetype is None:
        pagetype = path.split('.')[-1]

    if typemapping is None:
        typemapping = {}

    mapping = {}
    mapping.update(DEFAULT_MAPPING)
    mapping.update(typemapping)

    with codecs.open(path, encoding='utf-8') as fp:
        return mapping[pagetype]()(fp)
