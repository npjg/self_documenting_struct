Most projects that use the [`struct` library](https://docs.python.org/3/library/struct.html) use raw format strings, which are difficult to understand and remember. This library intuitively wraps the `struct` library to address this issue. provides dataclasses that define the various `struct` format string elements, which can then be combined into format strings in a far more consistent and self-documenting manner than they could otherwise.

I wrote this library to aid my reverse engineering efforts.
 - On a practical level, I grew tired of copy-pasting unintuitive `struct` format strings for common data types like integers and C strings. 
 - On a philosophical level, I believe read-time convenience should be favored above write-time convenience - especially for code that documents file formats.

| Old-style `struct` format string     | Self-documenting `struct`  |
| -----------            | ----------- |
| `'<H'`                   | `f'{Type.uint16_le}'` |
| `'hhl'` | `f'{Primitive.short}{Primitive.short}{Primitive.long}'`  |
| `'<10sHHb'`               | `f'{ByteOrder.little}10{Primitive.fixed_length_string}2{Primitive.ushort}{Primitive.bool}'` |

Some simple data types are provided as a sample, with read/write helper functions. The `struct` library methods are still available, but they are renamed as "raw" methods:
| Old-style `struct` method     | Self-documenting `struct` method |
| -----------            | ----------- |
|`struct.pack` | `self_documenting_struct.pack.raw` |
|`struct.pack_into` | `self_documenting_struct.pack.raw_into` |
|`struct.unpack` | `self_documenting_struct.unpack.raw` |
|`struct.unpack_from` | `self_documenting_struct.unpack.raw_from` |
|`struct.iter_unpack` | `self_documenting_struct.unpack.iter_raw` |
|`struct.calcsize` | `self_documenting_struct.calcsize` |

## Example Usage
You can unpack and pack with the existing simple data types already provided for you.
```python
    import self_documenting_struct as struct

    with open('C:\WINDOWS\BEAR.EXE', 'rb') as bear_file:
        # Since this contains just one element, the tuple is automatically unpacked 
        # by the uint32_le method.
        #
        # More readable than struct.unpack_from('<I', bear_file)[0].
        an_integer: int = struct.unpack.uint32_le(bear_file)

    with open('C:\WINNT\BUNNY32.DLL', 'wb') as bunny_file:
        a_packed_integer: bytes = struct.pack.unt32_le(an_integer)
        bunny_file.write(a_packed_integer)
```

Or you can self-documentingly define your own data types using the `ByteOrder`, `Primitive`, and `Type` dataclasses. 
(The `Primitive` dataclass names individual format characters, and the `Type` dataclass contains common compositions of `ByteOrder`s `Primitive`s.)

```python
    import self_documenting_struct as struct
    from self_documenting_struct.data_types import Primitive, Type

    # This is much more readable than "<Hx?".
    foo_bar_type_string: str = f'{Type.uint16_le}{Primitive.pad_byte}{Primitive.bool}'

    with open('C:\WINDOWS\BEAR.EXE', 'rb') as bear_file:
        # Creates a tuple with the given elements.
        # Like usual, you must access the tuple yourself.
        foo_bar_int, _, foo_bar_bool = struct.unpack.raw_from(foo_bar_type_string, bear_file)

    with open('C:\WINNT\BUNNY32.DLL', 'wb') as bunny_file:
        struct.raw_into(foo_bar_type_string, foo_bar)
```
And, of course, you can define a custom module that extends the self-documenting functionality to your own types.

## TODOs
 - Add native support for more simple data types useful for reverse engineering.
 - Add support for the `Struct` object.