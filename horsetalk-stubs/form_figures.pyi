
from horsetalk import (
    Disaster as Disaster,
)
from horsetalk import (
    FinishingPosition as FinishingPosition,
)
from horsetalk import (
    FormBreak as FormBreak,
)

class FormFigures:
    @staticmethod
    def parse(form_figures: str) -> list[FinishingPosition | FormBreak | Disaster]: ...
