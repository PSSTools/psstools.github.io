PSS 3.0 Migration Guide
=======================

PSS 3.0 is largely backward compatible with PSS 2.x. Most existing PSS 2.x
code works without modification.

Breaking Changes
----------------

The following identifiers are newly reserved keywords in PSS 3.0:

``monitor``, ``yield``, ``randomize``, ``atomic``, ``eventually``,
``concat``, ``overlap``, ``schedule``

If your PSS 2.x code uses any of these as identifiers, rename them:

.. code-block:: none

   // PSS 2.x — will fail if 'monitor' used as identifier
   action monitor { }        // ERROR in PSS 3.0

   // PSS 3.0 — use a different name
   action monitor_action { } // OK

Validation Checklist
--------------------

1. **Parse check** — verify all files parse without errors:

   .. code-block:: python

      from pssparser import Parser

      parser = Parser()
      parser.parses([("file.pss", open("file.pss").read())])
      root = parser.link()

2. **Keyword check** — search for identifier conflicts:

   .. code-block:: bash

      grep -rE '\b(monitor|yield|randomize|atomic)\b' *.pss

3. **Regression check** — run your existing test suite.

Common Patterns
---------------

**Behavioral coverage with monitors**

Replace ad-hoc coverage tracking with first-class monitor declarations and
``cover`` statements (see :doc:`pss30_features`).

**Procedural randomization**

Use ``randomize(x) { ... }`` in ``exec`` blocks for dynamic constraints
instead of always relying on declarative ``rand``.

**Reference collections**

Manage action handle lists with ``list<ref A>``, ``map<string, ref A>``,
etc., rather than manual pools.

For full before/after code examples see the upstream
`pssparser migration guide <https://github.com/PSSTools/pssparser/blob/main/docs/pss30_migration.rst>`_.

See Also
--------

- :doc:`pss30_features` — Complete PSS 3.0 feature reference
- :doc:`quickstart` — Getting started guide
