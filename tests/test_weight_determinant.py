from horsetalk import WeightDeterminant


def test_race_weight_status_can_be_created_from_enum():
    assert WeightDeterminant.HANDICAP == WeightDeterminant(1)


def test_race_weight_status_can_be_created_from_name():
    assert WeightDeterminant.HANDICAP == WeightDeterminant["HANDICAP"]


def test_race_weight_status_can_be_created_from_lowercase_name():
    assert WeightDeterminant.HANDICAP == WeightDeterminant["handicap"]
