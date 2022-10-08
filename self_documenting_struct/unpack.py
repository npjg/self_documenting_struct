
import struct
from struct import unpack as raw
from struct import unpack_from as raw_from
from struct import iter_unpack as iter_raw

from .data_types import Type

## The following methods read items from a binary stream. 
## All of these methods are "atomic": They return only one item each.
## Since the result of a struct unpack is a tuple even if the struct
## only contains one item, we will always return the first index.
## \param[in] stream - A binary stream that supports the read method.
## \return The decoded data type.
def uint8(stream) -> int:
    return struct.unpack_from(Type.uint8, stream)[0]

def int8(stream) -> int:
    return struct.unpack_from(Type.int8, stream)[0]

def uint16_le(stream) -> int:
    return struct.unpack_from(Type.uint16_le, stream)[0]

def int16_le(stream) -> int:
    return struct.unpack_from(Type.int16_le, stream)[0]

def uint16_be(stream) -> int:
    return struct.unpack_from(Type.uint16_be, stream)[0]

def int16_be(stream) -> int:
    return struct.unpack_from(Type.int16_be, stream)[0]

def uint32_le(stream) -> int:
    return struct.unpack_from(Type.uint32_le, stream)[0]

def int32_le(stream) -> int:
    return struct.unpack_from(Type.int32_le, stream)[0]

def uint32_be(stream) -> int:
    return struct.unpack_from(Type.uint32_be, stream)[0]

def int32_be(stream) -> int:
    return struct.unpack_from(Type.int32_be, stream)[0]

def c_string(stream) -> bytes:
    return struct.unpack_from(Type.c_string, stream)[0]
