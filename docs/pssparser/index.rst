pssparser
=========

**pssparser** is an ANTLR4-based parser for the Accellera PSS language.
It converts PSS source files into an Abstract Syntax Tree (AST) and
provides both C++ and Python APIs for downstream processing.

Source: https://github.com/PSSTools/pssparser

Key Features
------------

- **PSS 3.0 Support** – Full grammar support for PSS 3.0 (August 2024 spec)
- **Monitors** – Behavioral coverage with temporal operators
- **String Enhancements** – String methods and substring operator
- **Reference Collections** – Collections of reference types
- **C++ and Python APIs** – Use from either language
- **Complete AST** – Full abstract syntax tree representation
- **High Performance** – Fast parsing with minimal memory overhead

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   quickstart
   cli

.. toctree::
   :maxdepth: 2
   :caption: PSS 3.0

   pss30_features
   pss30_migration

.. toctree::
   :maxdepth: 2
   :caption: Developer Guide

   architecture
   ast_structure
   ast_usage
   api_reference
