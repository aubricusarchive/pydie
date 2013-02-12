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

package_data = {'pydie': ['LICENSE.md', 'README.md']}

requires = [
    'setuptools',
    'docopt==0.6.1'
]

entry_points = {
    'console_scripts': ['pydie = pydie.cli:main']
}

setup(
    url='http://github.com/aubricus/pydie',
    name='pydie',
    version='0.1.8',
    description='Generate a random roll from a n-number of an n-sided die',
    author='Aubrey Taylor',
    author_email='aubricus@gmail.com',
    packages=packages,
    package_data=package_data,
    install_requires=requires,
    entry_points=entry_points,
    package_dir={'pydie': 'pydie'},
    long_description=open('README.rst').read(),
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
