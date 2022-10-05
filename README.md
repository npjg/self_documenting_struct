# self_documenting_struct

Most projects that use the `struct' library use the raw format strings,
which are difficult to understand. This library provides dataclasses
that define the various struct format string elements, which can 
then be combined into format strings in a far more stream-documenting manner
than they could otherwise.

Some simple data types are provided as a sample, with read/write helper functions.