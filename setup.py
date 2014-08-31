import os
import re

try:
        from setuptools import setup
except ImportError:
        from distutils.core import setup

PACKAGE_NAME = 'hummingbird'

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'README.rst')) as fp:
    README = fp.read()
with open(os.path.join(HERE, PACKAGE_NAME, '__init__.py')) as fp:
    VERSION = re.search("__version__ = '([^']+)'", fp.read()).group(1)

setup(
    name="Hummingbird",
    version="0.0.1",
    author="Melody Kelly",
    author_email="melody@melody.blue",
    description=("An API Wrapper for Hummingbird.me"),
    license="MIT",
    keywords="Hummingbird anime api wrapper",
    url="https://github.com/KnightHawk3/hummingbird",
    packages=[PACKAGE_NAME, '{0}.tests'.format(PACKAGE_NAME)],
    long_description=README,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=['requests>=2.4.0'],
    test_suite='{0}.tests'.format(PACKAGE_NAME)
)
