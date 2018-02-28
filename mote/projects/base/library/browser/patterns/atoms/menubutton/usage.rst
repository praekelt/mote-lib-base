Info
====
- **Reference:** self.browser.atoms.menubutton
- **Uses:**: self.browser.atoms.nested, self.browser.atoms.string
- **Parent Library:** mote-lib-base
- **Pattern Type:** Atom

----

Data Spec
=========
.. code-block:: yaml

    # Uses self.browser.atoms.nested, and is an anchor tag by default.
    tag: a

    # Default class. Additional classes can be added as desired.
    classes:
        block: MenuButton

    # Default attributes.
    # Override attrs.href with desired URL.
    attrs:
        href: ''
        role: menuitem

    # Uses self.browser.atoms.string for text, by default.
    # Override children.text.value to replace text.
    # Add children.[key] to add additional patterns if desired.
    children:
        text:
            id: self.browser.atoms.string
            value: Menu Item

----

Usage
=====
Use for the creation of links in menus. This pattern has the relevant HTML role assigned by default,
and can render any other pattern within itself. This should make it easy to compose complex menu item
designs with icons, images, etc.
