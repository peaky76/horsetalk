from horsetalk import HorseExperienceLevel


def test_horse_experience_level_can_be_created_from_enum():
    assert HorseExperienceLevel.MAIDEN == HorseExperienceLevel(1)


def test_horse_experience_level_can_be_created_from_name():
    assert HorseExperienceLevel.MAIDEN == HorseExperienceLevel["MAIDEN"]


def test_horse_experience_level_can_be_created_from_lowercase_name():
    assert HorseExperienceLevel.MAIDEN == HorseExperienceLevel["maiden"]


def test_horse_experience_level_can_be_created_from_apostrophised_name():
    assert HorseExperienceLevel.NOVICE == HorseExperienceLevel["NOVICE'S"]
