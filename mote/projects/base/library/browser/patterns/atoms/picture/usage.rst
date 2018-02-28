Info
====
- **Reference:** self.browser.atoms.picture
- **Uses:** self.browser.atoms.image
- **Parent Library:** mote-lib-base
- **Pattern Type:** Atom

----

Data Spec
=========
.. code-block:: yaml

    # Default class. Additional classes may be added as desired.
    classes:
        block: Picture

    # Any HTML attribute can be passed in as a key/value pair as shown below.
    # Emits foo="bar" on the element.
    attrs:
        foo: bar

    # As per responsive image spec, <picture> can have multiple instances of <source>
    sources:
        # Each source.srcset can have multiple images, and can have attrs applied.
        - srcset:
            attrs:
                type: 'image/webp'
                media: '(min-width: 500px) and (max-width: 1000px)'
            images:
                -
                    src: foo@200.webp
                    dimensions: 200w 100h
                -
                    src: foo@400.webp
                    dimensions: 400w 200h
        - srcset:
            images:
                -
                    src: foo@200.png
                    dimensions: 200w 100h
                -
                    src: foo@400.png
                    dimensions: 400w 200h

    # Uses self.browser.atoms.image.
    # Empty src applied by default. Override with img.attrs.src
    img:
        attrs:
            src: ''

----

Usage
=====
The picture tag forms part of the responsive image spec, and works in a similar fashion to
HTML5 video.

Multiple ``<sources>`` may be supplied, each of which can have its own ``srcset`` and other valid HTML attributes.
