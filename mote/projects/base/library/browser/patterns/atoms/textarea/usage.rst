Info
====
- **Reference:** self.browser.atoms.textarea
- **Uses:** self.browser.atoms.nested
- **Parent Library:** mote-lib-base
- **Pattern Type:** Atom

----

Data Spec
=========
.. code-block:: yaml

    # Default class.
    classes:
        block: TextArea

    # HTML Attributes may be added as follows:
    attrs:
        disabled: disabled
        readonly: readonly
        data-foo: foo

    # How to add a default text value:
    children:
        text:
            id: self.browser.atoms.string
            value: This is how you provide default content to the textarea.

