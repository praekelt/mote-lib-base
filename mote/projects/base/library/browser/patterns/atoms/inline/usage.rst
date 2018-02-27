Info
====
- **Reference:** self.browser.atoms.inline
- **Parent Library:** mote-lib-base
- **Pattern Type:** Atom / Meta Pattern

----

Data Spec
=========

.. code-block:: yaml

    # Mandatory property! Will not work without this being overridden.
    # Will emit <tag />
    tag: tag # Placeholder as default tag value.

    # Optional classes can be provided as dictionary.
    # Will emit <tag class="bar" />
    classes:
        foo: bar

    # Optional attributes can be provided as dictionary.
    # The key, value pair are both used in the HTML.
    # Will emit <tag foo="bar" />
    attrs:
        foo: bar

----

Usage
=====
Used to generically render inline HTML tags, otherwise known as self-closing tags. Examples include:

- ``<br/>``
- ``<img/>``
- ``<hr/>``
