
from dataclasses import dataclass

## Most projects that use the `struct' library use the raw format strings,
## which are difficult to understand. This library provides dataclasses
## that define the various struct format string elements, which can 
## then be combined into format strings in a far more stream-documenting manner
## than they could otherwise.
##
## Some sample data types are provided, with read/write helper functions.
## \author Nathanael Gentry
## \date   10/02/2022

## Gives more descriptive names to the byte order format characters
## used for packing/unpacking bytes with the struct module.
@dataclass
class ByteOrder:
    native = '@'
    # TODO: Document this better.
    native_standard_alignment = '='
    little = '<'
    big = '>'
    network = '!'

## Specifies the default byte order in case another byte order is 
## not provided in a format string.
default_byte_order = ByteOrder.Little

## Gives more descrptive names to commonly-used size format characters
## used for packing/unpacking bytes with the struct module.
##
## These format characters define "primitive" C data types, but when combined 
## with each other and/or ByteOrder characters, they can define more complex
## data types.
##
## Unsigned integer types are prefixed with a "u", and  signed integer types 
## do not have a prefix.
@dataclass
class Primitive:
    pad_byte = 'x'
    # `byte` corresponds to the C type `char`. 
    # Python unpacks `byte` to a `bytes` object of length 1.
    byte = 'c'
    # Python unpacks `char` to a signed 8-bit integer.
    char = 'b'
    # Python unpacks `uchar` to an unsigned 8-bit integer.
    uchar = 'B'
    bool = '?'
    short = 'h'
    ushort = 'H'
    int = 'i'
    uint = 'I'
    long = 'l'
    ulong = 'L'
    longlong = 'q'
    ulonglong = 'Q'
    float = 'f'
    half_precision_float = 'e'
    double = 'd'
    # Fixed-length strings require a string length provided in the format string.
    # For a string of 10 characters, the format string would be `10s`.
    # Note that this is the only type where a digit prepending the format
    # character is a byte count, NOT a repetition count. Thus, to read three 
    # 10-byte fixed-length strings, you must write `10s10s10s`.
    fixed_length_string = 's'
    # This string length is defined by the first byte stored/read
    # rather than by a fixed length in the format string like the above.
    # Thus, each Pascal string read can have a different length.
    # To read 3 Pascal strings, write `3p` as usual.
    pascal_string = 'p'

## Defines data types based on combinations of byte orders
## and primitive data types. Each of these should have
## packing and unpacking methods provided.
@dataclass
class Type:
    uint8 = f'{ByteOrder.native}{Primitive.UnsignedChar}'
    int8 = f'{ByteOrder.native}{Primitive.SignedChar}'
    uint16_le = f'{ByteOrder.little}{Primitive.UnsignedShort}'
    int16_le = f'{ByteOrder.little}{Primitive.Short}'
    uint16_be = f'{ByteOrder.big}{Primitive.UnsignedShort}'
    int16_be = f'{ByteOrder.big}{Primitive.Short}'
    uint32_le = f'{ByteOrder.little}{Primitive.UnsignedInt}'
    int32_le = f'{ByteOrder.little}{Primitive.Int}'
    uint32_be = f'{ByteOrder.big}{Primitive.UnsignedInt}'
    int32_be = f'{ByteOrder.big}{Primitive.Int}'
    c_string = f'{Primitive.c_string}'
