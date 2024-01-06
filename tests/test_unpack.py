import pytest
from io import BytesIO

from self_documenting_struct import unpack

def test_uint8():
    stream = BytesIO(b'\x01')
    result = unpack.uint8(stream)
    assert result == 1

    stream = BytesIO(b'\xff')
    result = unpack.uint8(stream)
    assert result == 255

def test_int8():
    stream = BytesIO(b'\x7f')
    result = unpack.int8(stream)
    assert result == 127

    stream = BytesIO(b'\x80')
    result = unpack.int8(stream)
    assert result == -128

def test_uint16_le():
    stream = BytesIO(b'\x01\x00')
    result = unpack.uint16_le(stream)
    assert result == 1

    stream = BytesIO(b'\xff\xff')
    result = unpack.uint16_le(stream)
    assert result == 65535

def test_int16_le():
    stream = BytesIO(b'\x7f\x00')
    result = unpack.int16_le(stream)
    assert result == 127

def test_uint16_be():
    stream = BytesIO(b'\x00\x01')
    result = unpack.uint16_be(stream)
    assert result == 1

    stream = BytesIO(b'\xff\xff')
    result = unpack.uint16_be(stream)
    assert result == 65535

def test_int16_be():
    stream = BytesIO(b'\x00\x7f')
    result = unpack.int16_be(stream)
    assert result == 127

def test_uint32_le():
    stream = BytesIO(b'\x01\x00\x00\x00')
    result = unpack.uint32_le(stream)
    assert result == 1

def test_int32_le():
    stream = BytesIO(b'\x7f\x00\x00\x00')
    result = unpack.int32_le(stream)
    assert result == 127

def test_uint32_be():
    stream = BytesIO(b'\x00\x00\x00\x01')
    result = unpack.uint32_be(stream)
    assert result == 1

def test_int32_be():
    stream = BytesIO(b'\x00\x00\x00\x7f')
    result = unpack.int32_be(stream)
    assert result == 127

def test_pascal_string():
    stream = BytesIO(b'\x05Hello')
    result = unpack.pascal_string(stream)
    assert result == b'Hello'

    stream = BytesIO(b'\x0bHello World')
    result = unpack.pascal_string(stream)
    assert result == b'Hello World'



