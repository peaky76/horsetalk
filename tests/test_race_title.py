from horsetalk import (
    AgeCategory,
    Gender,
    HorseExperienceLevel,
    Obstacle,
    RaceDesignation,
    RaceTitle,
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


def test_race_title_parse_can_correctly_identify_horse_experience_level_when_present():
    expected = HorseExperienceLevel.NOVICE
    actual = RaceTitle.parse("LADBROKES FOOTBALL ACCA BOOTY FILLIES NOVICE STAKES (5)")[
        "horse_experience_level"
    ]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_horse_experience_level_when_not_present():
    expected = None
    actual = RaceTitle.parse("HAPPY NEW YEAR HANDICAP (4)")["horse_experience_level"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_race_designation_when_present():
    expected = RaceDesignation.HANDICAP
    actual = RaceTitle.parse("HAPPY NEW YEAR HANDICAP (4)")["race_designation"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_race_designation_when_not_present():
    expected = None
    actual = RaceTitle.parse("DERBY STAKES (Group 1)")["race_designation"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_gender_when_one_present():
    expected = [Gender.FILLY]
    actual = RaceTitle.parse("32Red.com FILLIES HANDICAP (5)")["gender"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_gender_when_multiple_present():
    expected = [Gender.FILLY, Gender.MARE]
    actual = RaceTitle.parse("32Red.com FILLIES AND MARES HANDICAP (5)")["gender"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_gender_when_none_present():
    expected = None
    actual = RaceTitle.parse("HAPPY NEW YEAR HANDICAP (4)")["gender"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_name():
    expected = "LADBROKES FOOTBALL ACCA BOOTY"
    actual = RaceTitle.parse("LADBROKES FOOTBALL ACCA BOOTY FILLIES NOVICE STAKES (5)")[
        "name"
    ]
    assert expected == actual
