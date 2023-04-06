from horsetalk import Obstacle


def test_obstacle_can_be_created_from_enum():
    assert Obstacle.HURDLE == Obstacle(1)


def test_obstacle_can_be_created_from_name():
    assert Obstacle.HURDLE == Obstacle["HURDLE"]


def test_obstacle_can_be_created_from_lowercase_name():
    assert Obstacle.HURDLE == Obstacle["hurdle"]


def test_obstacle_can_be_created_from_hyphenated_name():
    assert Obstacle.CROSS_COUNTRY == Obstacle["CROSS-COUNTRY"]


def test_obstacle_can_be_created_from_unhyphenated_name():
    assert Obstacle.CROSS_COUNTRY == Obstacle["CROSS COUNTRY"]


def test_obstacle_can_be_created_from_abbreviation():
    assert Obstacle.HURDLE == Obstacle["h"]
