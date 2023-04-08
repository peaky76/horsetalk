from horsetalk import FinishingPosition


def test_finishing_position_can_be_created_from_enum():
    assert FinishingPosition.UNPLACED == FinishingPosition(0)


def test_finishing_position_str_returns_expected_string():
    assert "0" == str(FinishingPosition.UNPLACED)
