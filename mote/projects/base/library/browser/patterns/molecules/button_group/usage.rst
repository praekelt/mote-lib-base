Info
====
- **Reference:** self.browser.molecules.button_group
- **Uses:**: self.browser.atoms.nested.list
- **Parent Library:** mote-lib-base
- **Pattern Type:** Molecule

----

Data Spec
=========
.. code-block:: yaml

    # By default, this pattern uses self.browser.atoms.nested.list
    # but this can be overridden if desired.
    id: self.browser.atoms.nested.list

    # Default parent tag.
    tag: ul

    # Default class on parent.
    classes:
        block: ButtonGroup

    # Default config for the <li> wrapping each button.
    wrapper:
        tag: li
        classes:
            element: ButtonGroup-buttonWrapper

        # Optionally, you may pass the <li> tags attributes
        # which all of them will receive.
        attrs:
            foo: bar

    # Children must be passed in as a list.
    # Due to the generic nature of this pattern,
    # you will need to specify the `id` of the
    # desired child pattern you wish to render.
    # This allows you to have custom button patterns
    # which can still be used with button_group.
    children:
        -
            id: self.browser.atoms.button
        -
            id: self.browser.atoms.button
