Info
====
- **Reference:** self.browser.atoms.text
- **Variations:** .anchor, .blockquote, .bold, .data, .emphasis, .heading1/2/3/4/5/6, .italic, .label, .legend, .mark, .paragraph, .small, .strong, .time
- **Parent Library:** mote-lib-base
- **Pattern Type:** Atom

----

Data Spec
=========
.. code-block:: yaml

    # All text atoms will have this default class.
    classes:
        block: Text

    # Variations/Optional
    # Every defined variation has a modifier class baked into it
    # in order to make it easier to style individually.
    # The format is as follows:
    classes:
        modifier: Text--type...

    # The text value may be provided as follows:
    value: foo

----

Usage
=====
This pattern may be used for any HTML text element, which consists of just a tag wrapping a plaintext string.

Some sensible defaults have been provided as variations, and may be called as ``self.browser.atoms.text.[name]``
