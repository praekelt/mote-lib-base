Info
====
- **Reference:** self.browser.molecules.breadcrumbs
- **Uses:**: self.browser.atoms.nested, self.browser.atoms.nested.list
- **Parent Library:** mote-lib-base
- **Pattern Type:** Molecule

----

Data Spec
=========
.. code-block:: yaml

    tag: nav

    # Default class.
    classes:
        block: Breadcrumb

    # Default attributes.
    # As a best practice, we add an aria-label to the breadcrumb so
    # that screen readers and search engine crawlers have an easier
    # time of figuring out what it is.
    attrs:
        aria-label: breadcrumb

    # Because we're using self.browser.atoms.nested
    # we need to pass in children to flesh out the pattern.
    # We're passing in a single child, called "items", which is
    # itself a nested.list atom.
    children:
        items:
            id: self.browser.atoms.nested.list
            tag: ol
            classes:
                element: Breadcrumb-items

            wrapper:
                tag: li
                classes:
                    element: Breadcrumb-item

            # These are the actual items in the breadcrumb.
            # Because it's a list, the children patterns
            # need to be explicitly defined using the
            # reserved 'id' key in order to render.
            children:
                -
                    id: self.browser.atoms.text.anchor
                    value: Home
                -
                    # In this example, the "current" item
                    # is simply a <span> with a text value.
                    id: self.browser.atoms.text
                    value: Current

----

Usage
=====
All you need to do to make use of this pattern is provide it with breadcrumb items to render.

This can be done by passing in a list of patterns with their relevant configs to ``children.items.children``.

If the above seems redundant, it isn't. It's a result of nesting ``self.browser.atoms.nested`` within another ``self.browser.atoms.nested`` atom.

See the example above for an example of how to render breadcrumb items within ``children.items.children``.
