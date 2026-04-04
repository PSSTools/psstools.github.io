AST Usage Guide
===============

This page shows common patterns for traversing and querying the AST
produced by pssparser.

Parsing and Linking
-------------------

.. code-block:: python

   from pssparser import Parser

   parser = Parser()
   parser.parses([
       ("a.pss", open("a.pss").read()),
       ("b.pss", open("b.pss").read()),
   ])
   root = parser.link()

``root`` is the ``RootSymbolTree``. Use it as the starting point for all
subsequent queries.

Walking the Symbol Tree
-----------------------

The symbol tree exposes children via the ``children`` attribute:

.. code-block:: python

   for child in root.children:
       print(child.name, type(child).__name__)

Visiting the Physical AST
--------------------------

Each ``unit`` in the symbol tree corresponds to a parsed file. Visitor
classes can be generated from the AST grammar; the typical pattern is to
subclass the generated visitor and override the ``visit_*`` methods for
the node types you care about.

.. code-block:: python

   from pssparser.ast import AstVisitor

   class ActionPrinter(AstVisitor):
       def visit_Action(self, node):
           print("Action:", node.name)
           self.visitChildren(node)

   printer = ActionPrinter()
   for unit in root.units:
       printer.visit(unit)

Error Handling
--------------

``parses()`` raises ``pssparser.ParseError`` on syntax errors. The
exception carries a list of diagnostics:

.. code-block:: python

   from pssparser import Parser, ParseError

   try:
       parser.parses([("bad.pss", "broken pss {")])
   except ParseError as e:
       for diag in e.diagnostics:
           print(diag.severity, diag.message, diag.location)

See Also
--------

- :doc:`ast_structure` — AST data model overview
- :doc:`api_reference` — Full API reference
