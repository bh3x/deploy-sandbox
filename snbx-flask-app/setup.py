#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from glob import glob
from os.path import basename
from os.path import splitext
import os

from setuptools import find_packages
from setuptools import setup

# Hard linking doesn't work inside VirtualBox shared folders. This means that
# you can't use tox in a directory that is being shared with Vagrant, since tox
# relies on `python setup.py sdist` which uses hard links. As a workaround,
# disable hard-linking if setup.py is a descendant of /vagrant.  For more
# details, see:
# https://stackoverflow.com/questions/7719380/python-setup-py-sdist-error-operation-not-permitted
if os.path.abspath(__file__).split(os.path.sep)[1] == 'vagrant':
    del os.link


setup(
    name='snbxflaskapp',
    version='0.0.0',
    description=(
        'Experimental Flask APP Sandbox'
    ),
    author='Adrian Buturca',
    author_email='adrian.bh3x@gmail.com',
    url='http://www.github.com/bh3x',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==0.10.1',
    ],
    classifiers=[
        'Development Status :: 4 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        'Topic :: Software Development :: Bug Tracking'
    ]
)
