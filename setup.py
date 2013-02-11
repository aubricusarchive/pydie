#!/usr/bin/env python
import os
import sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

packages = [
    'pydie'
]

requires = [
    'docopt==0.6.1'
]

entry_points = {
    'console_scripts': [
            'pydie = pydie.cli:main',
        ],
}

setup(
    name='pydie',
    version='0.1.2',
    description='Generate a random roll from a n-number of an n-sided die',
    author='Aubrey Taylor',
    author_email='aubricus@gmail.com',
    url='http://github.com/aubricus/pydie',
    packages=packages,
    install_requires=requires,
    package_dir={'pydie': 'pydie'},
    entry_points=entry_points,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),

)

del os.environ['PYTHONDONTWRITEBYTECODE']
