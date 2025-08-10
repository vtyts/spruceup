from os import path
from setuptools import setup, find_packages

from spruceup.__init__ import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='spruceup',
    version=__version__,
    author='Marek Borowiec',
    author_email='petiolus@gmail.com',
    description='A module for lexible identification, visualization, and removal of outliers from large multiple sequence alignments',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/marekborowiec/spruceup',
    keywords='alignment trimming outliers phylogenetics phylogenomics genomics bioinformatics',
    packages=['spruceup'],
    package_dir={'spruceup': 'spruceup'},
    include_package_data=True,
    python_requires='>=3.6.0, !=3.7.4',
    install_requires=[
        'matplotlib>=3.0.3',
        'numpy>=1.17',
        'scipy>=1.3.1',
        'psutil==5.6.6',
        'tqdm==4.29.1',
        'treeswift==1.0.100',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    test_suite="tests",
)
