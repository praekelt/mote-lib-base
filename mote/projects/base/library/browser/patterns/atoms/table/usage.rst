Info
====
- **Reference:** self.browser.atoms.table
- **Parent Library:** mote-lib-base
- **Pattern Type:** Atom

----

Data Spec
=========
.. code-block:: yaml

    # Default classes.
    # This applies to the <table> element itself.
    classes:
        block: Table

    # This globally applies classes to all table rows.
    row_classes:
        element: Table-row

    # This globally applies classes to all table cells.
    col_classes:
        element: Table-cell

    # Table structure
    # Rows and columns are expected to be provided as lists.
    rows:
        -
            # Each row is treated as a <tr> by default, but this
            # can be overriden with the tag property.
            tag: thead

            # Classes may be applied to individual rows as desired.
            classes:
                modifier: Table-row--backgroundDark

            columns:
                -
                    # Each column is treated as a <td> by default, but this
                    # can be overriden with the tag property.
                    tag: th

                    # Classes may be applied to individual cells as desired.
                    classes:
                        modifier:
                            Table--heading

                    # The content of a given cell can be any
                    # other pattern, and can be specified with
                    # the id property.
                    content:
                        id: self.browser.atoms.text.bold
                        value: Table Header 1
                -
                    tag: th
                    classes:
                        modifier:
                            Table--heading
                    content:
                        id: self.browser.atoms.text.bold
                        value: Table Header 2
        -
            columns:
                -
                    content:
                        id: self.browser.atoms.string
                        value: Table Cell
                -
                    content:
                        id: self.browser.atoms.string
                        value: Table Cell

----

Usage
=====
As demonstrated in the example above, tables are quite customisable.

You may supply global classes for the standard elements which comprise a table,
and where necessary you may override or provide additional classes or attributes per cell or row.

Any other pattern may be injected into a table cell.

