from horsetalk import Obstacle, RaceTitle


def test_race_title_parse_returns_dict():
    expected = dict
    actual = type(RaceTitle.parse(""))
    assert expected == actual


def test_race_title_parse_can_correctly_identify_obstacle_when_present():
    expected = Obstacle.HURDLE
    actual = RaceTitle.parse("HAPPY NEW YEAR NOVICES HURDLE (4)")["obstacle"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_obstacle_when_not_present():
    expected = None
    actual = RaceTitle.parse("HAPPY NEW YEAR HANDICAP (4)")["obstacle"]
    assert expected == actual
