from horsetalk import ExperienceLevel


def test_race_experience_status_can_be_created_from_enum():
    assert ExperienceLevel.MAIDEN == ExperienceLevel(1)


def test_race_experience_status_can_be_created_from_name():
    assert ExperienceLevel.MAIDEN == ExperienceLevel["MAIDEN"]


def test_race_experience_status_can_be_created_from_lowercase_name():
    assert ExperienceLevel.MAIDEN == ExperienceLevel["maiden"]


def test_race_experience_status_can_be_created_from_apostrophised_name():
    assert ExperienceLevel.NOVICE == ExperienceLevel["NOVICE'S"]
