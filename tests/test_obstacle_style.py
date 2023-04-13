from horsetalk import ObstacleStyle


def test_jump_category_can_be_created_from_enum():
    assert ObstacleStyle.HURDLE == ObstacleStyle(1)


def test_jump_category_can_be_created_from_name():
    assert ObstacleStyle.HURDLE == ObstacleStyle["HURDLE"]


def test_jump_category_can_be_created_from_lowercase_name():
    assert ObstacleStyle.HURDLE == ObstacleStyle["hurdle"]


def test_jump_category_can_be_created_from_abbreviation():
    assert ObstacleStyle.PLAIN_FENCE == ObstacleStyle["plain"]
