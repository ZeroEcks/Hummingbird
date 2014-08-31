import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Hummingbird",
    version="0.0.1",
    author="Melody Kelly",
    author_email="melody@melody.blue",
    description=("An API Wrapper for Hummingbird.me"),
    license="MIT",
    keywords="Hummingbird anime api wrapper",
    url="https://github.com/KnightHawk3/hummingbird",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "Inteded Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=['requests>=2.4.0']
)
