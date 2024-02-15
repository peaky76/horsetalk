.. horsetalk documentation master file, created by
   sphinx-quickstart on Thu Feb 15 18:27:04 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

horsetalk
=========

For horse racing enthusiasts, a series of classes and functions to help you parse and structure horse racing data.
Most of the classes are parsers which automatically take a string and create an object out of it.

For example, with the current year being 2024...

>>> from horsetalk import Horse
>>> h = Horse("Dobbin (GB) 3")
>>> h.name
'Dobbin'
>>> h.country
'GB'
>>> h.age
3
>>> h.year_of_birth
2021

For more information, see :doc:`api`

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Home <self>
   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
