from horsetalk import (
    AgeCategory,
    ExperienceLevel,
    Obstacle,
    RaceTitle,
    WeightDeterminant,
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


def test_race_title_parse_can_correctly_identify_age_category_when_present():
    expected = AgeCategory.JUVENILE
    actual = RaceTitle.parse(
        "BETSAFE BEST ODDS GUARANTEED JUVENILE MAIDEN HURDLE (Qualifier) (4)"
    )["age_category"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_age_category_when_not_present():
    expected = None
    actual = RaceTitle.parse("HAPPY NEW YEAR HANDICAP (4)")["age_category"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_experience_level_when_present():
    expected = ExperienceLevel.NOVICE
    actual = RaceTitle.parse("LADBROKES FOOTBALL ACCA BOOTY FILLIES NOVICE STAKES (5)")[
        "experience_level"
    ]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_experience_level_when_not_present():
    expected = None
    actual = RaceTitle.parse("HAPPY NEW YEAR HANDICAP (4)")["experience_level"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_weight_determinant_when_present():
    expected = WeightDeterminant.HANDICAP
    actual = RaceTitle.parse("HAPPY NEW YEAR HANDICAP (4)")["weight_determinant"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_weight_determinant_when_not_present():
    expected = None
    actual = RaceTitle.parse("DERBY STAKES (Group 1)")["weight_determinant"]
    assert expected == actual
