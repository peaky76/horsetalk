from horsetalk import AgeCategory


def test_race_age_status_can_be_created_from_enum():
    assert AgeCategory.JUVENILE == AgeCategory(1)


def test_race_age_status_can_be_created_from_name():
    assert AgeCategory.JUVENILE == AgeCategory["JUVENILE"]


def test_race_age_status_can_be_created_from_lowercase_name():
    assert AgeCategory.JUVENILE == AgeCategory["juvenile"]


def test_race_age_status_can_be_created_from_apostrophised_name():
    assert AgeCategory.VETERAN == AgeCategory["VETERAN'S"]
