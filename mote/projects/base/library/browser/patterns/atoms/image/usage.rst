Info
====
- **Reference:** self.browser.atoms.image
- **Parent Library:** mote-lib-base
- **Pattern Type:** Atom

----

Data Spec
=========
.. code-block:: yaml

    # Default class. Add additional classes as desired.
    classes:
        block: Image

    # Pass in any attrs you want to the image tag, including alt attributes, src, etc.
    attrs:
        src: /static/images/image.png

    # Optional:
    # Support for the responsive image spec.
    # You can pass in a list of images, along with their dimension metadata.
    srcset:
        -
            src: foo@200.jpeg
            dimensions: 200w 100h
        -
            src: foo@800.jpeg
            dimensions: 800w 400h


----

Usage
=====
This is a regular ``<img>`` tag.

Any desired html attributes can be passed in through the ``attrs`` dictionary.

Optionally, if you wish to make use of the ``srcset=""`` attribute, you may do so as demonstrated above.
