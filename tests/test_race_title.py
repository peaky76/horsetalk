from horsetalk import (
    Obstacle,
    RaceAgeStatus,
    RaceExperienceStatus,
    RaceTitle,
    RaceWeightStatus,
)


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


def test_race_title_parse_can_correctly_identify_age_status_when_present():
    expected = RaceAgeStatus.JUVENILE
    actual = RaceTitle.parse(
        "BETSAFE BEST ODDS GUARANTEED JUVENILE MAIDEN HURDLE (Qualifier) (4)"
    )["age_status"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_age_status_when_not_present():
    expected = None
    actual = RaceTitle.parse("HAPPY NEW YEAR HANDICAP (4)")["age_status"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_experience_status_when_present():
    expected = RaceExperienceStatus.NOVICE
    actual = RaceTitle.parse("LADBROKES FOOTBALL ACCA BOOTY FILLIES NOVICE STAKES (5)")[
        "experience_status"
    ]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_experience_status_when_not_present():
    expected = None
    actual = RaceTitle.parse("HAPPY NEW YEAR HANDICAP (4)")["experience_status"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_weight_status_when_present():
    expected = RaceWeightStatus.HANDICAP
    actual = RaceTitle.parse("HAPPY NEW YEAR HANDICAP (4)")["weight_status"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_weight_status_when_not_present():
    expected = None
    actual = RaceTitle.parse("DERBY STAKES (Group 1)")["weight_status"]
    assert expected == actual
