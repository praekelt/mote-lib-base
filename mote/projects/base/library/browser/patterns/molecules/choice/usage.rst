Info
====
- **Reference:** self.browser.molecules.choice
- **Uses:**: self.browser.atoms.nested, self.browser.atoms.input.checkbox/radio
- **Parent Library:** mote-lib-base
- **Pattern Type:** Molecule

----

Data Spec
=========
.. code-block:: yaml

    tag: label

    classes:
        block: Choice

    children:
        # This pattern has two children - the input, and the indicator.
        # The input must precede the indicator to allow for CSS sibling
        # selector styling based on the input's :checked pseudoclass status.
        input:
            # Override the input's id to ``self.browser.atoms.input.radio`` if you
            # need radio button behaviour.
            id: self.browser.atoms.input.checkbox

            classes:
                element: Choice-input

            # It is strongly recommended to provide
            # an aria-describedby attribute which points to the
            # pseudo-label text.
            attrs:
                aria-describedby: choice-label

        indicator:
            id: self.browser.atoms.nested
            tag: span
            classes:
                element: Choice-indicator

            children:
                box:
                    id: self.browser.atoms.null
                label:
                    id: self.browser.atoms.text
                    attrs:
                        id: choice-label
                    value: Choice Text

----

Usage
=====
This pattern provides a sane baseline for creating custom checkboxes and radio buttons
using CSS.

In principle, it can be used as a baseline for toggles as well.


