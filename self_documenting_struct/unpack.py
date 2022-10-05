
import struct

from .data_types import DataType

## The following methods read items from a binary stream. 
## All of these methods are "atomic": They return only one item each.
## Since the result of a struct unpack is a tuple even if the struct
## only contains one item, we will always return the first index.
## \param[in] stream - A binary stream that supports the read method.
## \return The decoded data type.
def uint8(stream) -> int:
    return struct.unpack(DataType.uint8, stream.read(1))[0]

def int8(stream) -> int:
    return struct.unpack(DataType.int8, stream.read(1))[0]

def uint16_le(stream) -> int:
    return struct.unpack(DataType.uint16_le, stream.read(2))[0]

def int16_le(stream) -> int:
    return struct.unpack(DataType.int16_le, stream.read(2))[0]

def uint16_be(stream) -> int:
    return struct.unpack(DataType.uint16_be, stream.read(2))[0]

def int16_be(stream) -> int:
    return struct.unpack(DataType.int16_be, stream.read(2))[0]

def uint32_le(stream) -> int:
    return struct.unpack(DataType.uint32_le, stream.read(4))[0]

def int32_le(stream) -> int:
    return struct.unpack(DataType.int32_le, stream.read(4))[0]

def uint32_be(stream) -> int:
    return struct.unpack(DataType.uint32_be, stream.read(4))[0]

def int32_be(stream) -> int:
    return struct.unpack(DataType.int32_be, stream.read(4))[0]

def c_string(stream) -> bytes:
    return struct.unpack_from(DataType.c_string, stream)[0]
