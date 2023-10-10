from horsetalk import AgeCategory


def test_age_category_can_be_created_from_enum():
    assert AgeCategory.JUVENILE == AgeCategory(1)


def test_age_category_can_be_created_from_name():
    assert AgeCategory.JUVENILE == AgeCategory["JUVENILE"]


def test_age_category_can_be_created_from_lowercase_name():
    assert AgeCategory.JUVENILE == AgeCategory["juvenile"]


def test_age_category_can_be_created_from_apostrophised_name():
    assert AgeCategory.VETERAN == AgeCategory["VETERAN'S"]


def test_age_category_to_age_restriction_returns_correct_minimum_when_juvenile():
    assert 4 == AgeCategory.JUVENILE.to_age_restriction().minimum


def test_age_category_to_age_restriction_returns_correct_maximum_when_juvenile():
    assert 4 == AgeCategory.JUVENILE.to_age_restriction().maximum


def test_age_category_to_age_restriction_returns_correct_minumum_when_veterans():
    assert 10 == AgeCategory.VETERAN.to_age_restriction().minimum


def test_age_category_to_age_restriction_returns_correct_maximum_when_veterans():
    assert AgeCategory.VETERAN.to_age_restriction().maximum is None
