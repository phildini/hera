#!/usr/bin/env python
import io
import re
from setuptools import setup, find_packages
import sys

with io.open('./juno/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='juno',
    version=version,
    description='A desktop app for Jupyter Notebook',
    long_description=long_description,
    author='Philip James',
    author_email='phildini@phildini.net',
    license='Apache Software License',
    packages=find_packages(
        exclude=[
            'docs', 'tests',
            'windows', 'macOS', 'linux',
            'iOS', 'android',
            'django'
        ]
    ),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Apache Software License',
    ],
    install_requires=[
        'jupyter',
        'pathlib',
    ],
    options={
        'app': {
            'formal_name': 'Juno',
            'bundle': 'com.juno',
            'document_types': {
                'notebook': {
                    'descritption': 'Jupyter Notebook',
                    'extension': 'ipynb',
                }
            }
        },

        # Desktop/laptop deployments
        'macos': {
            'app_requires': [
                'toga-cocoa==0.3.0.dev11',
            ]
        },
        'linux': {
            'app_requires': [
                'toga-gtk==0.3.0.dev11',
            ]
        },
        'windows': {
            'app_requires': [
                'toga-winforms==0.3.0.dev11',
            ]
        },

        # Mobile deployments
        'ios': {
            'app_requires': [
                'toga-ios==0.3.0.dev11'
            ]
        },
        'android': {
            'app_requires': [
                'toga-android==0.3.0.dev11'
            ]
        },

        # Web deployments
        'django': {
            'app_requires': [
                'toga-django==0.3.0.dev11'
            ]
        },
    }
)
