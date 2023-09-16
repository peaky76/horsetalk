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


def test_race_conditions_str():
    assert (
        str(
            RaceConditions(
                datetime=pendulum.parse("2023-06-01 14:00"),
                racecourse=Racecourse("Portman Park", Surface.TURF),
                distance=RaceDistance("5f"),
                going=Going("Good"),
            )
        )
        == "1 Jun 2023, 14:00, Portman Park, 5f (Good)"
    )


def test_race_conditions_str_with_stalls_position():
    assert (
        str(
            RaceConditions(
                datetime=pendulum.parse("2023-06-01 14:00"),
                racecourse=Racecourse("Portman Park", Surface.TURF),
                distance=RaceDistance("5f"),
                going=Going("Good"),
                stalls_position=StallsPosition.INSIDE,
            )
        )
        == "1 Jun 2023, 14:00, Portman Park, 5f (Good), Stalls: Inside"
    )
