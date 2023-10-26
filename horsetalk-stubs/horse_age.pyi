from pendulum import DateTime as DateTime, Interval as Interval
from typing import Self

class HorseAge:
    def __init__(
        self,
        official_age: int | None = ...,
        *,
        foaling_date: DateTime | None = ...,
        birth_year: int | None = ...,
        context_date: DateTime | None = ...
    ) -> None: ...
    @property
    def official(self) -> Interval: ...
    @property
    def actual(self) -> Interval: ...
    def at(self, date: DateTime) -> Self: ...
