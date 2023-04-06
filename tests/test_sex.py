from horsetalk import Sex


def test_sex_can_be_created_from_enum():
    assert Sex.MALE == Sex(1)


def test_sex_can_be_created_from_name():
    assert Sex.MALE == Sex["MALE"]


def test_sex_can_be_created_from_lowercase_name():
    assert Sex.MALE == Sex["male"]


def test_sex_can_be_created_from_abbreviation():
    assert Sex.MALE == Sex["M"]
