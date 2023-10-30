from horsetalk import AgeCategory


def test_age_category_can_be_created_from_enum():
    assert AgeCategory(1) == AgeCategory.JUVENILE


def test_age_category_can_be_created_from_name():
    assert AgeCategory["JUVENILE"] == AgeCategory.JUVENILE


def test_age_category_can_be_created_from_lowercase_name():
    assert AgeCategory["juvenile"] == AgeCategory.JUVENILE


def test_age_category_can_be_created_from_apostrophised_name():
    assert AgeCategory["VETERAN'S"] == AgeCategory.VETERAN


def test_age_category_to_age_restriction_returns_correct_minimum_when_juvenile():
    assert AgeCategory.JUVENILE.to_age_restriction().minimum == 4


def test_age_category_to_age_restriction_returns_correct_maximum_when_juvenile():
    assert AgeCategory.JUVENILE.to_age_restriction().maximum == 4


def test_age_category_to_age_restriction_returns_correct_minumum_when_veterans():
    assert AgeCategory.VETERAN.to_age_restriction().minimum == 10


def test_age_category_to_age_restriction_returns_correct_maximum_when_veterans():
    assert AgeCategory.VETERAN.to_age_restriction().maximum is None
