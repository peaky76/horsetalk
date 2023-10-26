import pendulum
from horsetalk import (
    Going,
    Racecourse,
    RaceClass,
    RaceConditions,
    RaceDesignation,
    RaceDistance,
    RaceLevel,
    StallsPosition,
    Surface,
)


def test_race_conditions_can_be_initialized_with_date_racecourse_distance_going():
    assert RaceConditions(
        datetime=pendulum.parse("2023-06-01 14:00"),
        racecourse=Racecourse("Portman Park", Surface.TURF),
        distance=RaceDistance("5f"),
        race_designation=RaceDesignation["Maiden"],
        race_level=RaceLevel(RaceClass(5)),
        going=Going("Good"),
    )


def test_race_conditions_can_be_initialized_with_date_racecourse_distance_going_stalls_position():
    assert RaceConditions(
        datetime=pendulum.parse("2023-06-01 14:00"),
        racecourse=Racecourse("Portman Park", Surface.TURF),
        distance=RaceDistance("5f"),
        going=Going("Good"),
        race_designation=RaceDesignation["Maiden"],
        race_level=RaceLevel(RaceClass(5)),
        stalls_position=StallsPosition.INSIDE,
    )


def test_race_conditions_repr():
    assert (
        repr(
            RaceConditions(
                datetime=pendulum.parse("2023-06-01 14:00"),
                racecourse=Racecourse("Portman Park", Surface.TURF),
                distance=RaceDistance("5f"),
                going=Going("Good"),
                race_designation=RaceDesignation["Maiden"],
                race_level=RaceLevel(RaceClass(5)),
            )
        )
        == "<RaceConditions: datetime=2023-06-01 14:00:00+00:00, racecourse=<Racecourse: Portman Park, Surface.TURF>, distance=5f, going=Good, race_designation=Maiden, race_level=Class 5, stalls_position=None>"
    )


def test_race_conditions_str():
    assert (
        str(
            RaceConditions(
                datetime=pendulum.parse("2023-06-01 14:00"),
                racecourse=Racecourse("Portman Park", Surface.TURF),
                distance=RaceDistance("5f"),
                going=Going("Good"),
                race_designation=RaceDesignation["Maiden"],
                race_level=RaceLevel(RaceClass(5)),
            )
        )
        == "1 Jun 2023, 14:00, Portman Park, 5f (Good), Maiden (5)"
    )


def test_race_conditions_str_with_stalls_position():
    assert (
        str(
            RaceConditions(
                datetime=pendulum.parse("2023-06-01 14:00"),
                racecourse=Racecourse("Portman Park", Surface.TURF),
                distance=RaceDistance("5f"),
                going=Going("Good"),
                race_designation=RaceDesignation["Maiden"],
                race_level=RaceLevel(RaceClass(5)),
                stalls_position=StallsPosition.INSIDE,
            )
        )
        == "1 Jun 2023, 14:00, Portman Park, 5f (Good), Maiden (5), Stalls: Inside"
    )
