AST Structure
=============

The PSS language is object-oriented with some aspect-oriented features.
The AST structure reflects this by maintaining both a **physical** and a
**logical** view of the content.

Physical View
-------------

Parsing a file produces a physical AST rooted at a
``pssp::ast::IGlobalScope`` object. There is a 1:1 relationship between
source file and ``IGlobalScope``.

Logical View (Symbol Tree)
--------------------------

Symbol resolution builds a **Symbol Tree** that provides a merged, logical
view of the content. A symbol scope exists for any construct that supports
multiple contributors — for example, ``package``, ``action``, ``component``,
and ``function``. Scopes that do not support contribution from multiple
sources (e.g., ``constraint``) appear only in the physical view.

Example
-------

Given two files:

.. code-block:: none

   // pss_top.pss
   component pss_top {
       action Entry { }
   }

.. code-block:: none

   // pss_top_ext.pss
   extend component pss_top {
       action B { }
   }

The resulting tree is:

.. code-block:: text

   RootSymbolTree
   ├── children
   │   └── pss_top : SymbolTypeScope
   │       ├── Entry : SymbolTypeScope
   │       └── B : SymbolTypeScope
   └── units
       ├── pss_top.pss : GlobalScope
       │   └── pss_top : Component
       │       └── Entry : Action
       └── pss_top_ext.pss : GlobalScope
           └── pss_top : ExtendType
               └── B : Action

The ``children`` subtree provides the merged view (type extensions
included), while ``units`` preserves each file's physical representation.

See Also
--------

- :doc:`ast_usage` — Traversing and querying the AST
- :doc:`api_reference` — Full API reference
