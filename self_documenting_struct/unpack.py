
import struct
from struct import unpack as raw
from struct import unpack_from as raw_from
from struct import iter_unpack as iter_raw

from .data_types import Primitive, Type

## The following methods read items from a binary stream. 
## All of these methods are "atomic": They return only one item each.
## Since the result of a struct unpack is a tuple even if the struct
## only contains one item, we will always return the first index.
## \param[in] stream - A binary stream that supports the read method.
## \return The decoded data type.
def uint8(stream) -> int:
    return struct.unpack(Type.uint8, stream.read(1))[0]

def int8(stream) -> int:
    return struct.unpack(Type.int8, stream.read(1))[0]

def uint16_le(stream) -> int:
    return struct.unpack(Type.uint16_le, stream.read(2))[0]

def int16_le(stream) -> int:
    return struct.unpack(Type.int16_le, stream.read(2))[0]

def uint16_be(stream) -> int:
    return struct.unpack(Type.uint16_be, stream.read(2))[0]

def int16_be(stream) -> int:
    return struct.unpack(Type.int16_be, stream.read(2))[0]

def uint32_le(stream) -> int:
    return struct.unpack(Type.uint32_le, stream.read(4))[0]

def int32_le(stream) -> int:
    return struct.unpack(Type.int32_le, stream.read(4))[0]

def uint32_be(stream) -> int:
    return struct.unpack(Type.uint32_be, stream.read(4))[0]

def int32_be(stream) -> int:
    return struct.unpack(Type.int32_be, stream.read(4))[0]

def pascal_string(stream) -> bytes:
    try:
        return struct.unpack(Primitive.pascal_string, stream)
    except:
        string_length = uint8(stream)
        return stream.read(string_length)
