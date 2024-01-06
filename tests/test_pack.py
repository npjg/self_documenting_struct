import pytest

import self_documenting_struct.pack as pack

def test_uint8():
    value = 42
    expected = b'\x2a'
    converted_value = pack.uint8(value)
    assert converted_value == expected

def test_int8():
    value = -42
    expected = b'\xd6'
    converted_value = pack.int8(value)
    assert converted_value == expected

def test_uint16_le():
    value = 12345
    expected = b'\x39\x30'
    converted_value = pack.uint16_le(value)
    assert converted_value == expected

def test_int16_le():
    value = -12345
    expected = b'\xc7\xcf'
    converted_value = pack.int16_le(value)
    assert converted_value == expected

def test_uint16_be():
    value = 12345
    expected = b'\x30\x39'
    converted_value = pack.uint16_be(value)
    assert converted_value == expected

def test_int16_be():
    value = -12345
    expected = b'\xcf\xc7'
    converted_value = pack.int16_be(value)
    assert converted_value == expected

def test_uint32_le():
    value = 1234567890
    expected = b'\xd2\x02\x96\x49'
    converted_value = pack.uint32_le(value)
    assert converted_value == expected

def test_int32_le():
    value = -1234567890
    expected = b'\x2e\xfd\x69\xb6'
    converted_value = pack.int32_le(value)
    assert converted_value == expected

def test_uint32_be():
    value = 1234567890
    expected = b'\x49\x96\x02\xd2'
    converted_value = pack.uint32_be(value)
    assert converted_value == expected

def test_int32_be():
    value = -1234567890
    expected = b'\xb6\x69\xfd\x2e'
    converted_value = pack.int32_be(value)
    assert converted_value == expected
