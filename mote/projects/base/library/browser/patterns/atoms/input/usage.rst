Info
====
- **Reference:** self.browser.atoms.input
- **Variations**: .button, .checkbox, .color, .date, .datetime, .email, .file, .number, .password, .radio, .range, .reset, .search, .submit, .tel, .time, .url, .week
- **Uses:**: self.browser.atoms.inline
- **Parent Library:** mote-lib-base
- **Pattern Type:** Atom

----

Data Spec
=========
.. code-block:: yaml

    # Uses self.browser.atoms.inline, thus we provide the default tag value.
    tag: input

    # Default class. Additional classes may be provided as desired.
    classes:
        block: Input

    # Each variation will provide a default value for type. Default is 'text'.
    # Additional attributes, such as required may be added as such: 'required: required'
    attrs:
        type: text # Any valid HTML Input type value. This is abstracted away in the variations.

----

Usage
=====
Basic form input. Make use of variations to get a specific input type, or override the type attr manually.
