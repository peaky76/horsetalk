from horsetalk import JockeyExperienceLevel


def test_jockey_experience_level_can_be_created_from_enum():
    assert JockeyExperienceLevel.APPRENTICE == JockeyExperienceLevel(3)


def test_jockey_experience_level_can_be_created_from_name():
    assert JockeyExperienceLevel.APPRENTICE == JockeyExperienceLevel["APPRENTICE"]


def test_jockey_experience_level_can_be_created_from_lowercase_name():
    assert JockeyExperienceLevel.APPRENTICE == JockeyExperienceLevel["apprentice"]


def test_jockey_experience_level_can_be_created_from_plural_name():
    assert JockeyExperienceLevel.APPRENTICE == JockeyExperienceLevel["apprentices"]
