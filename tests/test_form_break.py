from horsetalk import FormBreak


def test_form_break_can_be_created_from_enum():
    assert FormBreak("-") == FormBreak.YEAR


def test_form_break_str_returns_expected_string():
    assert str(FormBreak.YEAR) == "-"
