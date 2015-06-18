#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')


def _read(fname):
    try:
        return open(path.join(path.dirname(__file__), fname)).read()
    except IOError:
        return ''


def load_requirements(file_name):
    requirements = []
    for l in _read(file_name).split('\n'):
        if l and not l.startswith('#'):
            if l.startswith('-r'):
                requirements.extend(load_requirements(l[3:]))
            else:
                requirements.append(l)
    return requirements


requirements = load_requirements('requirements.txt')

test_requirements = load_requirements('test_requirements.txt')

setup(
    name='python_wrap_cases',
    version='0.1.0',
    description="Simple library for generate test cases.",
    long_description=readme + '\n\n' + history,
    author="Kirill Ermolov",
    author_email='erm0l0v@ya.ru',
    url='https://github.com/erm0l0v/python_wrap_cases',
    packages=[
        'python_wrap_cases',
    ],
    package_dir={'python_wrap_cases':
                 'python_wrap_cases'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='python_wrap_cases',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
