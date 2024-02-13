from horsetalk import (
    AgeCategory,
    Gender,
    HorseExperienceLevel,
    JumpCategory,
    RaceDesignation,
    RaceTitle,
)


def test_race_title_parse_returns_dict():
    expected = dict
    actual = type(RaceTitle.parse(""))
    assert expected == actual


def test_race_title_parse_can_correctly_identify_jump_category_when_present():
    expected = JumpCategory.HURDLE
    actual = RaceTitle.parse("HAPPY NEW YEAR NOVICES HURDLE (4)")["jump_category"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_jump_category_when_not_present():
    expected = None
    actual = RaceTitle.parse("HAPPY NEW YEAR HANDICAP (4)")["jump_category"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_jump_category_when_cross_country():
    expected = JumpCategory.CROSS_COUNTRY
    actual = RaceTitle.parse("CROSS COUNTRY HANDICAP CHASE (5)")["jump_category"]
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
    expected = [RaceDesignation.HANDICAP]
    actual = RaceTitle.parse("HAPPY NEW YEAR HANDICAP (4)")["race_designation"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_multiple_race_designations_when_present():
    expected = [RaceDesignation.AUCTION, RaceDesignation.MAIDEN]
    actual = RaceTitle.parse("HAPPY NEW YEAR AUCTION MAIDEN (4)")["race_designation"]
    assert expected == actual


def test_race_title_parse_can_correctly_identify_race_designation_when_not_present():
    expected = None
    actual = RaceTitle.parse("EVER READY DERBY (Group 1)")["race_designation"]
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
