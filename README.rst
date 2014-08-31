.. image:: https://badge.waffle.io/KnightHawk3/Hummingbird.png?label=ready&title=Ready 
 :target: https://waffle.io/KnightHawk3/Hummingbird
 :alt: 'Stories in Ready'
.. _main_page:

Hummingbird: The Python Hummingbird API Wrapper
===============================================

.. begin_description

.. image:: https://travis-ci.org/KnightHawk3/Hummingbird.svg
    :target: https://travis-ci.org/KnightHawk3/Hummingbird

Hummingbird is a wrapper that aims to create a simple interface to hummingbird.me's API. 

Here's a example, getting the information about "Neon Genesis Evangelion"

.. code-block:: pycon

    >>> import hummingbird
    >>> bird = hummingbird.Hummingbird('username', 'password')
    >>> results = bird.search_anime('Evangelion')
    >>> for result in results:
    ...     print(result.title)
    Petit Eva: Evangelion@School
    Neon Genesis Evangelion
    Evangelion: 4.0
    Evangelion: 1.0 You Are (Not) Alone
    Evangelion: 2.0 You Can (Not) Advance
    >>> results[1].status
    'Finished Airing'

.. end_description

.. begin_installation

.. _installation:

Installation
------------

Hummingbird is supported by anything above python 3.0. The recommended way
to install is via `pip <http://pypi.python.org/pypi/pip>`_

.. code-block:: bash

   $ pip install hummingbird

If you don't have ``pip`` installed, then the Hitchhiker's Guide to Python has
a section for setting it up on `Windows
<http://docs.python-guide.org/en/latest/starting/install/win/>`_,
`Mac <http://docs.python-guide.org/en/latest/starting/install/osx/>`_ and
`Linux <http://docs.python-guide.org/en/latest/starting/install/linux/>`_.
There is also a `Stack overflow question on installing pip on Windows
<http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows>`_
that might prove helpful.

Alternatively you can do it via
`easy_install <http://pypi.python.org/pypi/setuptools>`_

.. code-block:: bash

    $ easy_install hummingbird

.. end_installation

.. begin_support

Support
-------

Contact KnightHawk3 on Hummingbird or email me at Melody@Melody.Blue. Eventually
there will be a subreddit or wiki for support.

If you've uncovered a bug or have a feature request, then `make an issue on the
project page at github <https://github.com/KnightHawk3/Hummingbird/issues>`_.

.. end_support

Documentation
-------------

There are lots of docstrings but eventually there will be a readthedocs.
