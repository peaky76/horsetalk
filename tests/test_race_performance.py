import pendulum
import pytest

from horsetalk import Disaster, FinishingPosition, Horselength, RacePerformance


def test_race_performance_init_with_int_sets_outcome():
    performance = RacePerformance(1)
    assert performance.outcome == FinishingPosition(1)


def test_race_performance_init_with_int_sets_official_position():
    performance = RacePerformance(1)
    assert performance.official_position == FinishingPosition(1)


def test_race_performance_init_with_digit_str_sets_outcome():
    performance = RacePerformance("1")
    assert performance.outcome == FinishingPosition(1)


def test_race_performance_init_with_digit_str_sets_official_position():
    performance = RacePerformance("1")
    assert performance.official_position == FinishingPosition(1)


def test_race_performance_init_with_disaster_sets_outcome():
    performance = RacePerformance("F")
    assert performance.outcome == Disaster.FELL


def test_race_performance_init_with_disaster_sets_official_position():
    performance = RacePerformance("F")
    assert performance.official_position is None


def test_race_performance_init_with_disaster_enum_sets_outcome():
    performance = RacePerformance(Disaster.FELL)
    assert performance.outcome == Disaster.FELL


def test_race_performance_init_with_disaster_enum_sets_official_position():
    performance = RacePerformance(Disaster.FELL)
    assert performance.official_position is None


def test_race_performance_init_with_official_position_sets_outcome():
    performance = RacePerformance("2", official_position=1)
    assert performance.outcome == FinishingPosition(2)


def test_race_performance_init_with_official_position_sets_official_position():
    performance = RacePerformance("2", official_position=1)
    assert performance.official_position == FinishingPosition(1)


def test_race_performance_init_with_time_sets_time():
    performance = RacePerformance("2", time=pendulum.duration(minutes=2, seconds=30))
    assert performance.time == pendulum.duration(minutes=2, seconds=30)


def test_race_performance_raises_error_if_str_not_valid():
    with pytest.raises(ValueError):
        RacePerformance("X")


def test_race_performace_raises_error_if_position_and_disaster_given():
    with pytest.raises(ValueError):
        RacePerformance("F", official_position="6")


def test_race_performace_raises_error_if_beaten_distance_and_disaster_given():
    with pytest.raises(ValueError):
        RacePerformance("F", beaten_distance=3)


def test_race_performance_does_not_set_beaten_distance_to_none_if_zero_beaten_distance():
    performance = RacePerformance("1", beaten_distance=0)
    assert performance.beaten_distance == 0


def test_race_performance_does_not_set_beaten_distance_to_none_if_zero_horselength_beaten_distance():
    performance = RacePerformance("1", beaten_distance=Horselength("0"))
    assert performance.beaten_distance == 0


def test_race_performance_repr_with_disaster():
    performance = RacePerformance("F")
    assert repr(performance) == "<RacePerformance: Disaster.FELL>"


def test_race_performance_repr_with_position():
    performance = RacePerformance("2")
    assert repr(performance) == "<RacePerformance: 2>"


def test_race_performance_repr_with_different_official_position():
    performance = RacePerformance("2", official_position="1")
    assert repr(performance) == "<RacePerformance: 2, placed 1>"


def test_race_performance_str_with_disaster():
    performance = RacePerformance("F")
    assert str(performance) == "Fell"


def test_race_performance_str_with_position():
    performance = RacePerformance("2")
    assert str(performance) == "2nd"


def test_race_performance_str_with_different_official_position():
    performance = RacePerformance("2", official_position="1")
    assert str(performance) == "2nd, placed 1st"


def test_race_performance_sort():
    performance_1 = RacePerformance("3", beaten_distance=Horselength("1"))
    performance_2 = RacePerformance("4", beaten_distance=Horselength("2"))
    performance_3 = RacePerformance("F")
    performance_4 = RacePerformance("1", beaten_distance=None)
    performance_5 = RacePerformance("2", beaten_distance=Horselength("1/2"))
    performances = [
        performance_1,
        performance_2,
        performance_3,
        performance_4,
        performance_5,
    ]

    performances.sort(reverse=True)

    assert performances == [
        performance_4,
        performance_5,
        performance_1,
        performance_2,
        performance_3,
    ]


def test_race_performance_is_completion_with_disaster():
    assert RacePerformance("F").is_completion is False


def test_race_performance_is_completion_with_position():
    assert RacePerformance("2").is_completion is True


def test_race_performance_is_win_with_disaster():
    assert RacePerformance("F").is_win is False


def test_race_performance_is_win_with_position():
    assert RacePerformance("2").is_win is False


def test_race_performance_is_win_with_win():
    assert RacePerformance("1").is_win is True


def test_race_performance_is_official_win_with_disaster():
    assert RacePerformance("F").is_official_win is False


def test_race_performance_is_official_win_with_position():
    assert RacePerformance("2").is_official_win is False


def test_race_performance_is_official_win_with_fptp_and_official_win():
    assert RacePerformance("1").is_official_win is True


def test_race_performance_is_official_win_when_result_downgraded():
    assert RacePerformance("1", official_position="2").is_official_win is False


def test_race_performance_is_official_win_when_result_upgraded():
    assert RacePerformance("2", official_position="1").is_official_win is True
