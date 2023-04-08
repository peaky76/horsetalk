from horsetalk import FinishingPosition


def test_finishing_position_can_be_created_from_enum():
    assert FinishingPosition.UNPLACED == FinishingPosition(0)
