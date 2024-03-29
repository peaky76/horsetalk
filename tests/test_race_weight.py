import re

import pytest

from horsetalk import RaceWeight


def test_race_weight_regex_gets_st_and_lb():
    assert re.match(RaceWeight.REGEX, "9st2lb").groups() == ("9", "2")


def test_race_weight_regex_gets_st():
    assert re.match(RaceWeight.REGEX, "9st").groups() == ("9", None)


def test_race_weight_regex_gets_lb():
    assert re.match(RaceWeight.REGEX, "140lb").groups() == (None, "140")


def test_race_weight_regex_gets_hyphenated_numbers():
    assert re.match(RaceWeight.REGEX, "9-2").groups() == ("9", "2")


def test_race_weight_can_be_initialised_with_hyphenated_input():
    assert RaceWeight("9-2").kg == pytest.approx(58.06, abs=0.01)


def test_race_weight_can_be_initialised_with_st_and_lb_input():
    assert RaceWeight("9st2lb").kg == pytest.approx(58.06, abs=0.01)


def test_race_weight_can_be_initialised_with_lb_input():
    assert RaceWeight("128lb").kg == pytest.approx(58.06, abs=0.01)


def test_race_weight_str():
    assert str(RaceWeight("9-2")) == "9st 2lb"
