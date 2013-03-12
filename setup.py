# -*- coding: utf-8 -*-

"""
rae
---

Una

"""

import sys

from distutils.core import setup

extra_setup = {}
if sys.version_info >= (3,):
    extra_setup['use_2to3'] = True
    # extra_setup['use_2to3_fixers'] = ['your.fixers']

setup(
    name='rae',
    version='0.0,1',
    author='Mario Rodas',
    author_email='rodasmario2@gmail.com',
    url='https://github.com/marsam/rae',
    # packages=['rae'],
    scripts=['rae.py'],
    license='MIT License',
    description='Consutla a la rae',
    long_description=__doc__,
    install_requires=[
        'lxml',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'License :: OSI Approved :: MIT License',
    ],
    **extra_setup
)
