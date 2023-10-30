from horsetalk import ObstacleStyle


def test_jump_category_can_be_created_from_enum():
    assert ObstacleStyle(1) == ObstacleStyle.HURDLE


def test_jump_category_can_be_created_from_name():
    assert ObstacleStyle["HURDLE"] == ObstacleStyle.HURDLE


def test_jump_category_can_be_created_from_lowercase_name():
    assert ObstacleStyle["hurdle"] == ObstacleStyle.HURDLE


def test_jump_category_can_be_created_from_abbreviation():
    assert ObstacleStyle["plain"] == ObstacleStyle.PLAIN_FENCE
