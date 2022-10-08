
import struct
from struct import pack as raw
from struct import pack_into as raw_into

from .data_types import Type

## The following methods encode Python objects in binary data types.
## All these methods are "atomic": They write only one item each.
## \param[in] value - The value to encode. This value must fit in the
##                    space provided in the target data type.
## \return The value encoded in the target binary data type.
def uint8(value: int) -> bytes:
    return struct.pack(Type.uint8, value)

def int8(value: int) -> bytes:
    return struct.pack(Type.int8, value)

def uint16_le(value: int) -> bytes:
    return struct.pack(Type.uint16_le, value)

def int16_le(value: int) -> bytes:
    return struct.pack(Type.int16_le, value)

def uint16_be(value: int) -> bytes:
    return struct.pack(Type.uint16_be, value)

def int16_be(value: int) -> bytes:
    return struct.pack(Type.int16_be, value)
    
def uint32_le(value: int) -> bytes:
    return struct.pack(Type.uint32_le, value)

def int32_le(value: int) -> bytes:
    return struct.pack(Type.int32_le, value)

def uint32_be(value: int) -> bytes:
    return struct.pack(Type.uint32_be, value)

def int32_be(value: int) -> bytes:
    return struct.pack(Type.int32_be, value)
