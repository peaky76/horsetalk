from horsetalk import JockeyExperienceLevel


def test_jockey_experience_level_can_be_created_from_enum():
    assert JockeyExperienceLevel(3) == JockeyExperienceLevel.APPRENTICE


def test_jockey_experience_level_can_be_created_from_name():
    assert JockeyExperienceLevel["APPRENTICE"] == JockeyExperienceLevel.APPRENTICE


def test_jockey_experience_level_can_be_created_from_lowercase_name():
    assert JockeyExperienceLevel["apprentice"] == JockeyExperienceLevel.APPRENTICE


def test_jockey_experience_level_can_be_created_from_plural_name():
    assert JockeyExperienceLevel["apprentices"] == JockeyExperienceLevel.APPRENTICE
