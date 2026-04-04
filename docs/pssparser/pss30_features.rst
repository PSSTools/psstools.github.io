PSS 3.0 Features
================

PSS 3.0 (August 2024) adds significant enhancements to PSS 2.x.
pssparser supports the full PSS 3.0 grammar including:

- **Monitors** — Behavioral coverage with temporal operators
- **String enhancements** — String methods and substring operator
- **Reference collections** — Collections containing reference types
- **Procedural randomization** — ``randomize`` statements in exec blocks
- **Activity atomic blocks** — ``atomic`` execution blocks in activities
- **Yield statements** — ``yield`` in target exec blocks
- **Platform qualifiers** — ``target``/``solve`` qualifiers on functions

For complete details on each feature see the
`pssparser PSS 3.0 documentation <https://github.com/PSSTools/pssparser/blob/main/docs/pss30_features.rst>`_.

Monitors
--------

Monitors define behavioral coverage constructs that observe action execution.

.. code-block:: none

   monitor ReadWriteSequence {
       activity {
           concat {
               ReadReg;
               WriteReg;
           }
       }
   }

   component pss_top {
       action ReadReg  { }
       action WriteReg { }

       cover ReadWriteSequence;
   }

String Enhancements
-------------------

Built-in string methods: ``size()``, ``find()``, ``find_last()``,
``find_all()``, ``lower()``, ``upper()``, ``split()``, ``chars()``.

Substring operator:

.. code-block:: none

   string s   = "hello world";
   string sub = s[0..4];   // "hello"
   int    len = s.size();  // 11

Reference Collections
---------------------

Reference types may now appear in ``array``, ``list``, ``map``, and ``set``
collections:

.. code-block:: none

   component pss_top {
       action A { }
       list<ref A> active_actions;
   }

See Also
--------

- :doc:`pss30_migration` — Migration guide from PSS 2.x
- :doc:`architecture` — Implementation architecture
