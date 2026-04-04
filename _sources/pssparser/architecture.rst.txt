Architecture
============

pssparser is implemented in two layers:

C++ Core
--------

The core parser is written in C++ and built on top of ANTLR4. It:

* Tokenises and parses PSS source files using a generated ANTLR4 grammar.
* Constructs a physical AST (one ``IGlobalScope`` per file).
* Performs symbol resolution and builds a merged Symbol Tree.
* Exposes the result through a C++ API.

Python Bindings
---------------

Python bindings wrap the C++ core using pybind11. The ``pssparser`` Python
package re-exports the C++ types and adds the high-level ``Parser``
convenience class.

PSS 3.0 Implementation Phases
------------------------------

PSS 3.0 support was implemented across seven incremental phases:

1. **Foundation & Assessment** — Grammar gaps identified against the spec.
2. **Grammar Completion** — ANTLR4 grammar updated for all PSS 3.0 constructs.
3. **AST Implementation** — New AST node types added (monitors, yield, etc.).
4. **Symbol Resolution** — Linker updated to resolve PSS 3.0 symbols.
5. **API Exposure** — C++ API extended and regenerated bindings.
6. **Testing** — Grammar and semantic test suites expanded.
7. **Documentation** — This documentation updated.

Key Design Decisions
--------------------

* **Single grammar file** — One ANTLR4 grammar covers both PSS 2.x and 3.0;
  version-specific constructs are guarded by parser predicates where needed.
* **Physical + logical duality** — Keeping both views avoids losing
  file-level provenance while still enabling the merged type-extension model.
* **Minimal Python surface** — The Python API mirrors the C++ API closely so
  that C++ and Python users share the same mental model.

See Also
--------

- :doc:`ast_structure` — Data model details
- :doc:`pss30_features` — PSS 3.0 feature reference
