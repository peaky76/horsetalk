from horsetalk import RaceExperienceStatus


def test_race_experience_status_can_be_created_from_enum():
    assert RaceExperienceStatus.MAIDEN == RaceExperienceStatus(1)


def test_race_experience_status_can_be_created_from_name():
    assert RaceExperienceStatus.MAIDEN == RaceExperienceStatus["MAIDEN"]


def test_race_experience_status_can_be_created_from_lowercase_name():
    assert RaceExperienceStatus.MAIDEN == RaceExperienceStatus["maiden"]


def test_race_experience_status_can_be_created_from_apostrophised_name():
    assert RaceExperienceStatus.NOVICE == RaceExperienceStatus["NOVICE'S"]
