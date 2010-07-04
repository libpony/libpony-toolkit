from __future__ import with_statement

from ..core import BaseCommand, InputError, utils

from os.path import join, dirname, abspath, basename, exists
import os
import jinja2
import codecs
import simplejson


class Command(BaseCommand):
    """
    Creates a new article with the given slug and language
    in the given path. slug and language are required
    parameters
    """
    def execute(self, args):
        folder = abspath(args.base_folder)
        article_folder = join(folder, args.slug)
        file_ = join(article_folder,
                'index.%s.%s.rst' % (args.language, args.slug))
        metafile = join(article_folder,
                'metadata.%s.json' % args.language)

        if exists(article_folder):
            raise InputError, "Target folder already exists"
        if not utils.is_valid_slug(args.slug):
            raise InputError, "Please use a valid slug (%s)" % utils.RE_SLUG

        output = u'''%s\n\nTEASER\n\n----------------------------\n\nBODY'''
        titleblock = u'%s\n%s' % (args.title, '='*len(args.title))

        sample_metadata = {'tags': []}

        os.makedirs(article_folder)
        with codecs.open(file_, 'w+', encoding='utf-8') as fp:
            fp.write(output % titleblock)
        with codecs.open(metafile, 'w+', encoding='utf-8') as fp:
            simplejson.dump(sample_metadata, fp, indent=4)

    @classmethod
    def provide_arguments(cls, parser):
        parser.add_argument('base_folder',
            help='This is the folder where all your articles are stored')
        parser.add_argument('slug')
        parser.add_argument('language')
        parser.add_argument('--title', default='TITLE')
