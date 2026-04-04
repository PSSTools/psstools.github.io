PSSTools
========

**PSSTools** is a collection of open-source tools for working with the
`Accellera Portable Test and Stimulus Standard (PSS)
<https://www.accellera.org/activities/working-groups/portable-stimulus>`_.

PSS is a language for specifying portable, intent-based tests at a high
level of abstraction, enabling automatic test generation across multiple
execution platforms and verification environments.

.. toctree::
   :maxdepth: 1
   :caption: Tools

   pssparser/index
   vscode_pss_support/index

.. toctree::
   :maxdepth: 1
   :caption: Project

   about

----

Tools at a Glance
-----------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Tool
     - Description
   * - :doc:`pssparser <pssparser/index>`
     - ANTLR4-based PSS parser with C++ and Python APIs, full PSS 3.0 support
   * - :doc:`VSCode PSS Support <vscode_pss_support/index>`
     - VS Code extension with diagnostics, navigation, completions, and more
