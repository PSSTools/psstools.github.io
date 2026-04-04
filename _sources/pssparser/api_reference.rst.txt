API Reference
=============

This page summarises the public Python API for pssparser.

``pssparser.Parser``
--------------------

High-level entry point for parsing and linking PSS content.

.. code-block:: python

   class Parser:
       def parses(self, files: list[tuple[str, str]]) -> None:
           """Parse a list of (filename, content) tuples.

           Raises ParseError if any file contains syntax errors.
           """

       def link(self) -> RootSymbolTree:
           """Resolve cross-file references.

           Returns a linked RootSymbolTree.
           Raises LinkError if symbol resolution fails.
           """

``pssparser.RootSymbolTree``
----------------------------

Root of the merged symbol tree returned by ``Parser.link()``.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Attribute
     - Description
   * - ``children``
     - Top-level ``SymbolTypeScope`` objects (packages, components, etc.)
   * - ``units``
     - ``IGlobalScope`` objects — one per parsed file (physical view)

``pssparser.ParseError``
------------------------

Raised by ``Parser.parses()`` on syntax errors.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Attribute
     - Description
   * - ``diagnostics``
     - List of ``Diagnostic`` objects describing each error

``pssparser.Diagnostic``
------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Attribute
     - Description
   * - ``severity``
     - ``"error"``, ``"warning"``, or ``"info"``
   * - ``message``
     - Human-readable description
   * - ``location``
     - ``(filename, line, column)`` tuple

Source Repository
-----------------

Full C++ API documentation is available in the source repository at
https://github.com/PSSTools/pssparser.
