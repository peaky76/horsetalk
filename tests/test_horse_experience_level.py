from horsetalk import HorseExperienceLevel


def test_horse_experience_level_can_be_created_from_enum():
    assert HorseExperienceLevel(1) == HorseExperienceLevel.MAIDEN


def test_horse_experience_level_can_be_created_from_name():
    assert HorseExperienceLevel["MAIDEN"] == HorseExperienceLevel.MAIDEN


def test_horse_experience_level_can_be_created_from_lowercase_name():
    assert HorseExperienceLevel["maiden"] == HorseExperienceLevel.MAIDEN


def test_horse_experience_level_can_be_created_from_apostrophised_name():
    assert HorseExperienceLevel["NOVICE'S"] == HorseExperienceLevel.NOVICE
