Info
====
- **Reference:** self.browser.atoms.nested
- **Variations:** .list
- **Parent Library:** mote-lib-base
- **Pattern Type:** Atom / Meta Pattern

----

Data Spec
=========

.. code-block:: yaml

    tag: foo # Optional. Use for wrapping HTML tag. e.g: div
    classes:
        foo: bar # Optional OrderedDict. Each key is a slot for a class. e.g: block: ClassName
    attrs: # Optional OrderedDict. Each key becomes a valid HTML property, and its value becomes the property's value.
        id: my-id
        role: banner

    wrapper: # Optional. Use for wrapping children in a tag. Implements classes and attrs the same as above.
        tag: bar
        classes:
            foo: bar
        attrs:
            id: my-id

    # If using self.browser.atoms.nested, pass it a dictionary
    children:
        child1: # this key is arbitrary, but allows for overriding a specific child by name.
            id: self.browser.[pattern]
        child2:
            id: self.browser.[pattern]

    # If using self.browser.atoms.nested.list, pass it a list
    children:
        - # This approach allows you to override the entire list of children without referencing each one by name.
            id: self.browser.[pattern]
        -
            id: self.browser.[pattern]


----

Usage
=====
The nested pattern allows one to, at minimum, generically render other patterns within it.

You can pass it an optional ``tag`` value, which will result in a wrapping HTML tag around the children.
In addition, you can also pass it an optional ``wrapper`` tag to have each child wrapped by another tag.
This is useful for generically creating, for example, a ``ul > li`` markup structure using only data.

Children may be provided as either a dictionary or a list.

Use a dictionary when you desire the ability to arbitrarily override a single child by being able to reference its key.
This will ensure that other siblings are unaffected and will render as expected.

Use a list when you want to override the entire list of children, or do not need to have a unique key for each child.
