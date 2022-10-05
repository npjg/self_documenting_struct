
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
    Native = '@'
    # TODO: Document this better.
    NativeNoAlignment = '='
    Little = '<'
    Big = '>'
    Network = '!'

## Specifies the default byte order in case another byte order is 
## not provided in a format string.
default_byte_order = ByteOrder.Little

## Gives more descrptive names to commonly-used size format characters
## used for packing/unpacking bytes with the struct module.
@dataclass
class PrimitiveDataType:
    PadByte = 'x'
    Char = 'c'
    SignedChar = 'b'
    UnsignedChar = 'B'
    Bool = '?'
    Short = 'h'
    UnsignedShort = 'H'
    Int = 'i'
    UnsignedInt = 'I'
    Long = 'l'
    UnsignedLong = 'L'
    LongLong = 'q'
    UnsignedLongLong = 'Q'
    Float = 'f'
    Double = 'd'
    CString = 's'
    PascalString = 'p'

## Defines data types based on combinations of byte orders
## and primitive data types. Each of these should have
## packing and unpacking methods provided.
@dataclass
class DataType:
    uint8 = f'{ByteOrder.Native}{PrimitiveDataType.UnsignedChar}'
    int8 = f'{ByteOrder.Native}{PrimitiveDataType.SignedChar}'
    uint16_le = f'{ByteOrder.Little}{PrimitiveDataType.UnsignedShort}'
    int16_le = f'{ByteOrder.Little}{PrimitiveDataType.Short}'
    uint16_be = f'{ByteOrder.Big}{PrimitiveDataType.UnsignedShort}'
    int16_be = f'{ByteOrder.Big}{PrimitiveDataType.Short}'
    uint32_le = f'{ByteOrder.Little}{PrimitiveDataType.UnsignedInt}'
    int32_le = f'{ByteOrder.Little}{PrimitiveDataType.Int}'
    uint32_be = f'{ByteOrder.Big}{PrimitiveDataType.UnsignedInt}'
    int32_be = f'{ByteOrder.Big}{PrimitiveDataType.Int}'
    c_string = f'{PrimitiveDataType.CString}'
