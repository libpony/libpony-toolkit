from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages


setup(
    name = 'libponytk',
    version = '0.1',
    author = 'Horst Gutmann',
    author_email = 'horst@zerokspot.com',
    license = 'BSD',
    description = 'Collection of scripts for working on libpony articles',
    packages = find_packages(),
    package_dir = {'':'src'},

    install_requires = ['docutils==0.6', 'pygments', 'argparse', 'html5lib',
        'jinja2', 'simplejson'],

    entry_points = {
        'console_scripts': ['libponytk = libponytk.core.mainapp:main'],
    },
    test_suite = 'libponytk.tests.test_all'
)
