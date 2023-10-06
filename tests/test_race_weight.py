from pytest import approx
from horsetalk import RaceWeight


def test_race_weight_with_hyphenated_input():
    assert RaceWeight("9-2").kg == approx(58.06, abs=0.01)


def test_race_weight_repr():
    assert repr(RaceWeight("9-2")) == "<RaceWeight: 9st 2lb>"


def test_race_weight_str():
    assert str(RaceWeight("9-2")) == "9st 2lb"
