from horsetalk.gender import Gender


def test_gender_can_be_created_from_enum():
    assert Gender.COLT == Gender(2)


def test_gender_can_be_created_from_name():
    assert Gender.COLT == Gender["COLT"]


def test_gender_can_be_created_from_lowercase_name():
    assert Gender.COLT == Gender["colt"]


def test_gender_can_be_created_from_abbreviation():
    assert Gender.COLT == Gender["C"]
