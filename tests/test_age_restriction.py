from horsetalk import AgeRestriction


def test_age_restriction_minimum_when_single_year_restriction():
    assert AgeRestriction("2yo").minimum == 2


def test_age_restriction_maximum_when_single_year_restriction():
    assert AgeRestriction("2yo").maximum == 2


def test_age_restriction_minimum_when_open_ended_restriction():
    assert AgeRestriction("3yo+").minimum == 3


def test_age_restriction_maximum_when_open_ended_restriction():
    assert AgeRestriction("3yo+").maximum == None


def test_age_restriction_minimum_when_upper_bounded_restriction():
    assert AgeRestriction("2-4yo").minimum == 2


def test_age_restrictions_maximum_when_upper_bounded_restriction():
    assert AgeRestriction("2-4yo").maximum == 4


def test_age_restriction_minimum_when_longhand():
    assert AgeRestriction("2 year olds only").minimum == 2


def test_age_restriction_maximum_when_longhand():
    assert AgeRestriction("2 year olds only").maximum == 2


def test_age_restriction_repr_when_single_year_restriction():
    assert repr(AgeRestriction("2yo")) == "<AgeRestriction: 2yo>"


def test_age_restriction_repr_when_open_ended_restriction():
    assert repr(AgeRestriction("3yo+")) == "<AgeRestriction: 3yo+>"


def test_age_restriction_repr_when_upper_bounded_restriction():
    assert repr(AgeRestriction("2-4yo")) == "<AgeRestriction: 2-4yo>"


def test_age_restriction_str_when_single_year_restriction():
    assert str(AgeRestriction("2yo")) == "2yo"


def test_age_restriction_str_when_open_ended_restriction():
    assert str(AgeRestriction("3yo+")) == "3yo+"


def test_age_restriction_str_when_upper_bounded_restriction():
    assert str(AgeRestriction("2-4yo")) == "2-4yo"
