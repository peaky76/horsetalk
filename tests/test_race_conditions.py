import pendulum
from horsetalk import Going, RaceConditions, RaceDistance, StallsPosition, Surface


def test_race_conditions_can_be_initialized_with_date_distance_going_surface():
    assert RaceConditions(
        datetime=pendulum.parse("2023-06-01 14:00"),
        distance=RaceDistance("5f"),
        going=Going("Good"),
        surface=Surface.TURF,
    )


def test_race_conditions_can_be_initialized_with_date_distance_going_stalls_position_surface():
    assert RaceConditions(
        datetime=pendulum.parse("2023-06-01 14:00"),
        distance=RaceDistance("5f"),
        going=Going("Good"),
        surface=Surface.TURF,
        stalls_position=StallsPosition.INSIDE,
    )
