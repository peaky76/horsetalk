from horsetalk import RaceAgeStatus


def test_race_age_status_can_be_created_from_enum():
    assert RaceAgeStatus.JUVENILE == RaceAgeStatus(1)


def test_race_age_status_can_be_created_from_name():
    assert RaceAgeStatus.JUVENILE == RaceAgeStatus["JUVENILE"]


def test_race_age_status_can_be_created_from_lowercase_name():
    assert RaceAgeStatus.JUVENILE == RaceAgeStatus["juvenile"]


def test_race_age_status_can_be_created_from_apostrophised_name():
    assert RaceAgeStatus.VETERAN == RaceAgeStatus["VETERAN'S"]
