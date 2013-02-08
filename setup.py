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

requires = ['docopt==0.6.1']

setup(
    name='pydie',
    version='0.1.0',
    description='Generate a random roll from a n-number of an n-sided die',
    long_description=open('README.md').read(),
    author='Aubrey Taylor',
    author_email='aubricus@gmail.com',
    url='http://github.com/aubricus/pydie',
    license=open('LICENSE.md').read(),
    packages=packages,
    package_data={'': ['LICENSE.md']},
    include_package_data=True,
    install_requires=requires,
    package_dir={'pydie': 'pydie'},
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