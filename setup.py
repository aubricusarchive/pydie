#!/usr/bin/env python

import os
import sys
from setuptools import setup

from pydie import __version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

# Setup arg values
url              = 'http://github.com/aubricus/pydie'
name             = 'pydie'
version          = __version__
description      = 'Generate a random roll from a n-number of an n-sided die.'
long_description = ''
license          = open('LICENSE.md').read()
author           = 'Aubrey Taylor'
author_email     = 'aubricus@gmail.com'
zip_safe         = False
download_url     = 'https://github.com/aubricus/pydie/archive/master.zip'

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

try:
    import subprocess
    import pandoc

    process = subprocess.Popen(
        ['which pandoc'],
        shell=True,
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    pandoc_path = process.communicate()[0]
    pandoc_path = pandoc_path.strip('\n')

    pandoc.core.PANDOC_PATH = pandoc_path

    readme = pandoc.Document()
    license = pandoc.Document()

    readme.markdown = open('README.md').read()
    license.markdown = open('LICENSE.md').read()

    long_description = readme.rst
    license = license.rst

except:
    pass

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
    license=license,
    classifiers=classifiers,
    download_url=download_url,
)

del os.environ['PYTHONDONTWRITEBYTECODE']
