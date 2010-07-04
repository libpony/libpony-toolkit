from __future__ import with_statement

from ..core import BaseCommand, InputError
from .. import pagebuilding, djangoemu

from os.path import join, dirname, abspath, basename
import glob
import jinja2
import codecs


class Command(BaseCommand):
    """
    This is a simple command for building an article using the same
    RST configuration also used for the site. It accepts one argument
    indicating the path to the article's folder.
    """
    def execute(self, args):
        input_folder = args.input_folder
        loader = jinja2.FileSystemLoader(args.templates_dir)
        env = jinja2.Environment(loader=loader)
        env.filters['date'] = djangoemu.date_filter
        template = env.get_template('libponytk/article.html')

        for file_ in glob.glob(join(input_folder, 'index.*.rst')):
            input_file = basename(file_)
            output_file = '_%s.html' % basename(file_)
            self.log.info("%s -> %s" % (input_file, output_file))
            output_path = join(dirname(file_), output_file)
            page = pagebuilding.build(file_)
            tvars = {
                'STATIC_URL': args.media_dir,
                'article': page,
                }
            with codecs.open(output_path, 'w+', encoding='utf-8') as fp:
                fp.write(template.render(**tvars))

    @classmethod
    def provide_arguments(cls, parser):
        parser.add_argument('input_folder')
