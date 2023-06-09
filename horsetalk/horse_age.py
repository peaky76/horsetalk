from typing import Self
import pendulum
from pendulum import DateTime, Period


class HorseAge:
    """
    A class representing the age of a horse.

    Attributes:
        _official_dob (DateTime): The official date of birth of the horse.
        _actual_dob (DateTime): The actual date of birth of the horse.
        _context_date (DateTime): The context date for calculating the age of the horse.

    """

    def __init__(
        self,
        official_age: int | None = None,
        *,
        foaling_date: DateTime | None = None,
        birth_year: int | None = None,
        context_date: DateTime | None = None
    ):
        """
        Initializes a new instance of the HorseAge class with the specified parameters.
        If official_age and either foaling_date or birth_year are both provided, a ValueError is raised.
        If no arguments are provided, a ValueError is raised.

        Args:
            official_age (int | None): The official age of the horse.
            foaling_date (DateTime | None): The actual date of birth of the horse.
            birth_year (int | None): The birth year of the horse.
            context_date (DateTime | None): The context date for calculating the age of the horse.

        Returns:
            None

        Raises:
            ValueError: If invalid arguments are provided.

        """
        if official_age is not None and (foaling_date or birth_year):
            raise ValueError(
                "Cannot initialize HorseAge with both official_age and keyword"
            )

        if not (official_age or foaling_date or birth_year):
            raise ValueError(
                "Cannot initialize HorseAge without official_age, foaling_date, or birth_year"
            )

        self._actual_dob = foaling_date
        self._context_date = context_date

        year = (
            birth_year
            if birth_year
            else self._base_date.year - official_age
            if official_age
            else foaling_date.year
            if foaling_date
            else None
        )

        self._official_dob = pendulum.datetime(year, 1, 1) if year else None

    @property
    def official(self) -> Period:
        """
        Calculate the official age of the horse based on its birth year or foaling date.

        Raises:
            ValueError: if the official date of birth is unknown

        Returns:
            A Period object representing the horse's official age in years, months, and days.
        """
        if not self._official_dob:
            raise ValueError("Cannot calculate official age as official dob is unknown")
        return self._calc_age(self._official_dob)

    @property
    def actual(self) -> Period:
        """
        Calculate the actual age of the horse based on its actual date of birth.

        Raises:
            ValueError: if the actual date of birth is unknown

        Returns:
            A Period object representing the horse's actual age in years, months, and days.
        """
        if not self._actual_dob:
            raise ValueError("Cannot calculate actual age as actual dob is unknown")
        return self._calc_age(self._actual_dob)

    @property
    def _base_date(self) -> DateTime:
        """
        Get the base date for calculating the age of the horse.

        Returns:
            A DateTime object representing the current date if the context date is not set,
            otherwise the context date.
        """
        return self._context_date if self._context_date else pendulum.now()

    def at(self, date: DateTime) -> Self:
        """
        Set the context date for calculating the age of the horse.

        Args:
            date: A DateTime object representing the date to set the context to.

        Returns:
            A HorseAge object with the context date set.
        """
        self._context_date = date
        return self

    def _calc_age(self, dob: DateTime) -> Period:
        """
        Calculate the age of the horse based on its date of birth.

        Args:
            dob: A DateTime object representing the date of birth of the horse.

        Returns:
            A Period object representing the age of the horse in years, months, and days.
        """
        return (
            self._base_date - dob
            if dob < self._base_date
            else self._base_date - self._base_date
        )
