Info
====
- **Reference:** self.browser.atoms.select
- **Parent Library:** mote-lib-base
- **Pattern Type:** Atom

----

Data Spec
=========

.. code-block:: yaml

    # Default class. Additional classes can be added as desired.
    classes:
        block: Select

    # Optional. If you need a multi-select, supply the property as below.
    # Alternatively, use self.browser.atoms.select.multiple
    attrs:
        multiple: multiple

    # The options should be configured as below.
    items:
        -
            option:
                text: foo
                attrs:
                    value: foo
                    disabled: disabled
                    selected: selected

        -
            # <optgroup> is supported, and you can mix options and optgroups as desired.
            group:
                attrs:
                    label: foo
                    disabled: disabled
                options:
                    -
                        text: foo
                        attrs:
                            value: foo
                            disabled: disabled
                            selected: selected

----

Usage
=====
This pattern returns a select with options and optgroups with options, as desired.

If you need a multiselect, make use of ``self.browser.atoms.select.multiple`` or supply the ``attr``
directly as ``attrs.multiple``.

Options make use of ``attrs`` and ``text`` values. If no ``text`` value is specified, you may instead pass it ``option.attrs.label`` as per the HTML5 spec.

Optgroups allow you to group options in a select under a single heading. This heading may be supplied as ``group.attrs.label``. Another valid attribute is ``disabled``, which is also demonstrated in the example data above.
