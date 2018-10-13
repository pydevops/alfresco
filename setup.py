#!/usr/bin/env python

from distutils.core import setup

version = '0.0.1'


setup(
    name='AlfrescoAPI',
    version='0.1.0',
    author='Victor Yang',
    author_email='pythonrocks@gmail.com',
    packages=['alfresco'],
    url='http://pypi.python.org/pypi/Alfresco/',
    license='LICENSE.txt',
    description='Useful stuff.',
    long_description=open('README.md').read(),
    install_requires=[
        "cmislib >= 0.5",
        "cmislibalf>=0.3.1",
    ],
)
