from horsetalk import JumpCategory


def test_jump_category_can_be_created_from_enum():
    assert JumpCategory(1) == JumpCategory.HURDLE


def test_jump_category_can_be_created_from_name():
    assert JumpCategory["HURDLE"] == JumpCategory.HURDLE


def test_jump_category_can_be_created_from_lowercase_name():
    assert JumpCategory["hurdle"] == JumpCategory.HURDLE


def test_jump_category_can_be_created_from_hyphenated_name():
    assert JumpCategory["CROSS-COUNTRY"] == JumpCategory.CROSS_COUNTRY


def test_jump_category_can_be_created_from_unhyphenated_name():
    assert JumpCategory["CROSS COUNTRY"] == JumpCategory.CROSS_COUNTRY


def test_jump_category_can_be_created_from_abbreviation():
    assert JumpCategory["h"] == JumpCategory.HURDLE
