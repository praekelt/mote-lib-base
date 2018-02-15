The base Mote pattern library
==============================

Mote itself is only a framework for pattern libraries and doesn't provide
any pattern libraries itself. The base library provides common patterns like
buttons, anchors, panels, images and many more. Its aim is to provide a solid
base for other pattern libraries.

Base a pattern library on this base by setting the ``parents`` in a Mote project's
metadata.yaml file:

.. code-block:: yaml

    parents:
        - base
        - myproject

