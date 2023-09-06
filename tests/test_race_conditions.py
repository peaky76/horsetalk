import pendulum
from horsetalk import (
    Going,
    Racecourse,
    RaceConditions,
    RaceDistance,
    StallsPosition,
    Surface,
)


def test_race_conditions_can_be_initialized_with_date_racecourse_distance_going():
    assert RaceConditions(
        datetime=pendulum.parse("2023-06-01 14:00"),
        racecourse=Racecourse("Portman Park", Surface.TURF),
        distance=RaceDistance("5f"),
        going=Going("Good"),
    )


def test_race_conditions_can_be_initialized_with_date_racecourse_distance_going_stalls_position():
    assert RaceConditions(
        datetime=pendulum.parse("2023-06-01 14:00"),
        racecourse=Racecourse("Portman Park", Surface.TURF),
        distance=RaceDistance("5f"),
        going=Going("Good"),
        stalls_position=StallsPosition.INSIDE,
    )
