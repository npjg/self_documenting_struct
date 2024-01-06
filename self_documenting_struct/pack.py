
import struct
from struct import pack as raw
from struct import pack_into as raw_into

from .data_types import Type

## The following methods encode Python objects in binary data types.
## All these methods are "atomic": They write only one item each.
## \param[in] value - The value to encode. This value must fit in the
##                    space provided in the target data type.
## \param[in] into - If provided, the encoded value is written to this
##                   binary stream rather than being returned.
## \return The value encoded in the target binary data type,
##         or None if the value was written into a stream.
def uint8(value: int, into = None) -> bytes:
    if into is None:
        return struct.pack(Type.uint8, value)
    else:
        struct.pack_into(Type.uint8, into, into.tell(), value)

def int8(value: int, into = None) -> bytes:
    if into is None:
        return struct.pack(Type.int8, value)
    else:
        struct.pack_into(Type.int8, into, into.tell(), value)

def uint16_le(value: int, into = None) -> bytes:
    if into is None:
        return struct.pack(Type.uint16_le, value)
    else:
        struct.pack_into(Type.uint16_le, into, into.tell(), value)

def int16_le(value: int, into = None) -> bytes:
    if into is None:
        return struct.pack(Type.int16_le, value)
    else:
        into.write(struct.pack(Type.int16_le, value))

def uint16_be(value: int, into = None) -> bytes:
    if into is None:
        return struct.pack(Type.uint16_be, value)
    else:
        into.write(struct.pack(Type.uint16_be, value))

def int16_be(value: int, into = None) -> bytes:
    if into is None:
        return struct.pack(Type.int16_be, value)
    else:
        struct.pack_into(Type.int16_be, into, into.tell(), value)
    
def uint32_le(value: int, into = None) -> bytes:
    if into is None:
        return struct.pack(Type.uint32_le, value)
    else:
        into.write(struct.pack(Type.uint32_le, value))

def int32_le(value: int, into = None) -> bytes:
    if into is None:
        return struct.pack(Type.int32_le, value)
    else:
        into.write(struct.pack(Type.int32_le, value))

def uint32_be(value: int, into = None) -> bytes:
    if into is None:
        return struct.pack(Type.uint32_be, value)
    else:
        into.write(struct.pack(Type.uint32_be, value))

def int32_be(value: int, into = None) -> bytes:
    if into is None:
        return struct.pack(Type.int32_be, value)
    else:
        into.write(struct.pack(Type.int32_be, value))
