Info
====
- **Reference:** self.browser.atoms.button
- **Variations:** .anchor
- **Uses:**
  - self.browser.atoms.nested
  - self.browser.atoms.string
- **Parent Library:** mote-lib-base
- **Pattern Type:** Atom

----

Data Spec
=========
.. code-block:: yaml

    # Uses self.browser.atoms.nested, and as such accepts the same properties.
    # Default
    tag: button

    # Variation .anchor
    tag: a
    attrs:
        href: '#'

    # -----

    # Default classes. Can be overridden, and additional classes can be added as desired.
    classes:
        block: Button

    # Uses self.browser.atoms.string for text value. Override the below 'value' key to change the text.
    children:
        text:
            id: self.browser.atoms.string
            value: Button text

----

Usage
=====
Buttons come in two flavours - ``<button>`` and ``<a>``.

``<button>`` is the default, and is used in forms and interactions which should trigger a JavaScript interaction.

``<a>`` is the .anchor variation, and is used for any use case where a button should redirect the user to a new page.

To override the text in the button, you need to override ``children.text.value`` with the desired string.
