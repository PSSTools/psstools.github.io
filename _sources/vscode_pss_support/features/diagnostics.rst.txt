Diagnostics
===========

The extension reports problems in real time. Diagnostics appear as squiggles
in the editor and are listed in the **Problems** panel (``Ctrl+Shift+M``).

Syntax Diagnostics
------------------

Detected immediately by the ANTLR4 parser:

- Missing or mismatched braces, brackets, and parentheses.
- Invalid or unexpected tokens.
- Incomplete declarations.

Semantic Diagnostics
--------------------

Multiple analysis passes check semantic correctness:

- **Pass 1 — Symbol Table**: duplicate declarations within the same scope.
- **Pass 2 — Extensions and Imports**: unresolved ``extend`` targets, kind
  mismatches, and unresolved ``import`` paths.
- **Pass 3 — Reference Resolution**: undefined types, unresolved base types,
  circular inheritance chains.

Lint Rules
----------

Optional style and quality checks. Each rule can be enabled or disabled in
``.pssconfig.json`` or VS Code settings.

.. list-table::
   :header-rows: 1
   :widths: 35 15 50

   * - Rule
     - Default
     - Description
   * - ``no-empty-constraint``
     - enabled
     - Warn on empty ``constraint`` blocks.
   * - ``no-unused-field``
     - enabled
     - Warn on fields never referenced.
   * - ``naming-convention``
     - enabled
     - Suggest fixes for identifiers that violate naming conventions.
   * - ``max-activity-depth``
     - enabled
     - Warn on activities nested beyond a configurable depth.
   * - ``no-unreachable-branch``
     - enabled
     - Warn on branches that can never be taken.

Set ``pss.lint.enabled`` to ``false`` to disable all lint checks.

Semantic Tokens
---------------

AST-aware syntax highlighting beyond the TextMate grammar. Token types and
modifiers are applied based on the resolved semantic meaning of each
identifier — distinguishing, for example, type declarations from type
references, and ``rand`` fields from regular fields.
