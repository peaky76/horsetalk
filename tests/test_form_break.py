from horsetalk import FormBreak


def test_form_break_can_be_created_from_enum():
    assert FormBreak.YEAR == FormBreak("-")
