from horsetalk import Sex


def test_sex_can_be_created_from_enum():
    assert Sex(1) == Sex.MALE


def test_sex_can_be_created_from_name():
    assert Sex["MALE"] == Sex.MALE


def test_sex_can_be_created_from_lowercase_name():
    assert Sex["male"] == Sex.MALE


def test_sex_can_be_created_from_abbreviation():
    assert Sex["M"] == Sex.MALE
