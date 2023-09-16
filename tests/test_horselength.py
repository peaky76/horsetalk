import pytest
from horsetalk import Horselength


def test_horselength_can_be_initialized_with_no_arguments():
    assert isinstance(Horselength(), Horselength)


def test_horselength_default_and_float_equivalence():
    assert Horselength(0) == Horselength()


def test_horselength_empty_string_and_float_equivalence():
    assert Horselength(0) == Horselength("")


def test_horselength_none_and_float_equivalence():
    assert Horselength(0) == Horselength(None)


def test_horselength_can_be_initialized_with_int():
    assert Horselength(1)


def test_horselength_can_be_initialized_with_float():
    assert Horselength(1.0)


def test_horselength_can_be_initialized_with_int_as_string():
    assert Horselength("1")


def test_horselength_can_be_initialized_with_float_as_string():
    assert Horselength("1.0")


def test_horselength_string_integer_and_float_equivalence():
    assert Horselength(1.0) == Horselength("1")


def test_horselength_string_float_and_float_equivalent():
    assert Horselength(1.2) == Horselength("1.2")


def test_horselength_can_be_initialized_with_fraction_as_string():
    assert Horselength("1/2")


def test_horselength_can_be_initialized_with_whole_and_fraction_as_string():
    assert Horselength("3 1/2")


def test_horselength_fraction_and_float_equivalence():
    assert Horselength(0.5) == Horselength("1/2")


def test_horselength_whole_and_fraction_and_float_equivalence():
    assert Horselength(3.5) == Horselength("3 1/2")


def test_horselength_can_be_initialized_with_description():
    assert Horselength("head")


def test_horselength_can_be_initialized_with_description_abbreviation():
    assert Horselength("hd")


def test_horselength_description_and_float_equivalence():
    assert Horselength(0.2) == Horselength("head")


def test_horselength_raises_error_if_initialized_with_invalid_string():
    with pytest.raises(ValueError):
        Horselength("shitloads")


def test_horselength_str_when_fraction():
    assert "1/2" == str(Horselength("1/2"))


def test_horselength_str_when_fraction_and_whole():
    assert "3 1/2" == str(Horselength("3 1/2"))


def test_horselength_str_when_description():
    assert "head" == str(Horselength("head"))


def test_horselength_can_be_summed():
    assert 1 == Horselength("1/2") + Horselength("nk") + Horselength("hd")


def test_horselength_can_be_compared():
    assert Horselength("1/2") > Horselength("nk")


def test_horselength_repr_uses_correct_class_name():
    assert "Horselength" in repr(Horselength("1/2"))


def test_horselength_to_string_when_result_of_cumulation():
    assert "6 3/5" == str(Horselength("6 1/2") + Horselength("shd"))


def test_horselength_add_to_another_horselength_returns_horselength_instance():
    assert isinstance(Horselength("1") + Horselength("1"), Horselength)


def test_horselength_add_to_a_decimal_returns_horselength_instance():
    assert isinstance(Horselength("1") + 1, Horselength)


def test_horselength_radd_with_a_decimal_returns_horselength_instance():
    assert isinstance(1 + Horselength("1"), Horselength)


def test_horselength_subtract_from_another_horselength_returns_horselength_instance():
    assert isinstance(Horselength("1") - Horselength("1"), Horselength)


def test_horselength_rsubtract_from_a_decimal_returns_horselength_instance():
    assert isinstance(1 - Horselength("1"), Horselength)
