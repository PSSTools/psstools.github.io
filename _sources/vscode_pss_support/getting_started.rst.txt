Getting Started
===============

Installation
------------

Install the extension from the VS Code Marketplace or from a ``.vsix`` file.

Requirements: VS Code 1.75.0 or newer.

First Steps
-----------

1. Open a folder containing ``.pss`` files.
2. The extension activates automatically for ``.pss`` files.
3. The **Outline** panel (``Ctrl+Shift+O``) shows your declarations.
4. Hover, Go to Definition, and completions work immediately.

Keyboard Shortcuts
------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Action
     - Shortcut
   * - Go to Definition
     - ``F12``
   * - Find All References
     - ``Shift+F12``
   * - Rename Symbol
     - ``F2``
   * - Outline
     - ``Ctrl+Shift+O``
   * - Workspace Symbols
     - ``Ctrl+T``
   * - Trigger Completions
     - ``Ctrl+Space``
   * - Format Document
     - ``Shift+Alt+F``
   * - Call Hierarchy
     - ``Shift+Alt+H``

Configuration
-------------

Create ``.pssconfig.json`` in your workspace root to configure include/exclude
globs, formatting options, and lint rules. See
`docs/CONFIGURATION.md <https://github.com/PSSTools/vscode-pss-support/blob/main/docs/CONFIGURATION.md>`_
in the repository.

CLI
---

Check PSS files from the command line without opening VS Code:

.. code-block:: bash

   npx pss-check src/
