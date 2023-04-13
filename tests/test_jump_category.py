from horsetalk import JumpCategory


def test_jump_category_can_be_created_from_enum():
    assert JumpCategory.HURDLE == JumpCategory(1)


def test_jump_category_can_be_created_from_name():
    assert JumpCategory.HURDLE == JumpCategory["HURDLE"]


def test_jump_category_can_be_created_from_lowercase_name():
    assert JumpCategory.HURDLE == JumpCategory["hurdle"]


def test_jump_category_can_be_created_from_hyphenated_name():
    assert JumpCategory.CROSS_COUNTRY == JumpCategory["CROSS-COUNTRY"]


def test_jump_category_can_be_created_from_unhyphenated_name():
    assert JumpCategory.CROSS_COUNTRY == JumpCategory["CROSS COUNTRY"]


def test_jump_category_can_be_created_from_abbreviation():
    assert JumpCategory.HURDLE == JumpCategory["h"]
