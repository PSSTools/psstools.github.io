##########
Quickstart
##########

Installing pssparser
====================

pssparser is most easily installed as a Python package from PyPI:

.. code-block:: bash

   pip install pssparser

Trying pssparser
================

pssparser provides the ``Parser`` utility class to simplify parsing and
linking PSS content from a Python script.

.. code-block:: python

   from pssparser import Parser

   parser = Parser()
   parser.parses([(
       "file1.pss",
       """
       component pss_top {
         action A { }
       }
       """)
   ])

   root = parser.link()

The basic flow:

- ``parses()`` accepts a list of ``(filename, content)`` tuples and raises
  an exception if syntax errors are encountered.
- ``link()`` resolves cross-file references and returns a linked symbol tree
  for further processing.

Next Steps
==========

- :doc:`cli` — Use pssparser from the command line
- :doc:`ast_structure` — Understand the AST structure
- :doc:`pss30_features` — Explore PSS 3.0 features
