from .race_class import RaceClass as RaceClass
from .race_grade import RaceGrade as RaceGrade
from _typeshed import Incomplete

class RaceLevel:
    grade: Incomplete
    class_: Incomplete
    def __init__(self, value: str | RaceGrade | RaceClass) -> None: ...
    def __eq__(self, other): ...
    def __gt__(self, other): ...
    def __lt__(self, other): ...