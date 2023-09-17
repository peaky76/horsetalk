import pytest
from horsetalk.parsing_enum import ParsingEnum


@pytest.fixture
def dummy_enum():
    class DummyEnum(ParsingEnum):
        FOO = 1
        BAR = 2
        BAZ = 3

    return DummyEnum


def test_parsing_enum_raises_keyerror_when_passed_a_non_string_key(dummy_enum):
    with pytest.raises(KeyError):
        ParsingEnum[1.0]
