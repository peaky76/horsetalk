from horsetalk import FormBreak


def test_obstacle_can_be_created_from_enum():
    assert FormBreak.YEAR == FormBreak("-")
