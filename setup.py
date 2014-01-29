#!/usr/bin/env python

import os
import sys
from setuptools import setup

from pydie import get_version

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

# Setup arg values
url              = 'http://github.com/aubricus/pydie'
name             = 'pydie'
version          = get_version()
description      = 'Generate a random roll from a n-number of an n-sided die'
long_description = open('README.rst').read()
author           = 'Aubrey Taylor'
author_email     = 'aubricus@gmail.com'
zip_safe         = False

package_dir = {'pydie': 'pydie'}
packages = [
    'pydie'
]
package_data = {
    'pydie': ['LICENSE.md', 'README.md']
}

requires = [
    'setuptools',
    'docopt==0.6.1'
]

entry_points = {
    'console_scripts': ['pydie = pydie.cli:main']
}

classifiers = (
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
)

setup(
    url=url,
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    packages=packages,
    package_data=package_data,
    install_requires=requires,
    entry_points=entry_points,
    package_dir=package_dir,
    long_description=long_description,
    classifiers=classifiers,
)

del os.environ['PYTHONDONTWRITEBYTECODE']
