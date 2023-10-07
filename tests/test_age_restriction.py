from horsetalk import AgeRestriction


def test_age_restriction_minimum_when_single_year_restriction():
    assert AgeRestriction("2yo").minimum == 2


def test_age_restriction_maximum_when_single_year_restriction():
    assert AgeRestriction("2yo").maximum == 2


def test_age_restriction_minimum_when_open_ended_restriction():
    assert AgeRestriction("3yo+").minimum == 3


def test_age_restriction_maximum_when_open_ended_restriction():
    assert AgeRestriction("3yo+").maximum == None


def test_age_restriction_minimum_when_age_limited_restriction():
    assert AgeRestriction("2-4yo").minimum == 2


def test_age_restrictions_maximum_when_age_limited_restriction():
    assert AgeRestriction("2-4yo").maximum == 4
