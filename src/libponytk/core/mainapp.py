import sys
import logging
import argparse
from os.path import dirname, join, abspath

from .. import commands
from .commands import REGISTRY

class LazyDocstring(object):
    """Simple docstring factory for only loading the docstring
    when first used"""
    def __init__(self, cls, methodname=None, *args, **kwargs):
        self.cls = cls
        self.methodname = methodname
        self.args = args
        self.kwargs = kwargs
        self.docstring = None

    def __mod__(self, other):
        return str(self) % other

    def __str__(self):
        if self.docstring is not None:
            return self.docstring
        instance = self.cls(*self.args, **self.kwargs)
        if self.methodname is None:
            return instance.__doc__
        self.docstring = getattr(instance, self.methodname).__doc__
        return self.docstring

def main():
    parser = argparse.ArgumentParser()
    base_dir = dirname(dirname(abspath(__file__)))
    parser.add_argument('--debug', default=False, action='store_true')
    parser.add_argument('--templates-dir',
            default=join(base_dir, 'templates'))
    parser.add_argument('--media-dir',
            default=join(base_dir, 'media') + '/')
    subparsers = parser.add_subparsers()
    for k, v in REGISTRY.iteritems():
        subparser = subparsers.add_parser(k, help=LazyDocstring(v))
        subparser.set_defaults(func=v)
        v.provide_arguments(subparser)
    args = parser.parse_args()
    loglevel = args.debug and logging.DEBUG or logging.INFO
    logging.basicConfig(level=loglevel, stream=sys.stderr)
    args.func()(args)
