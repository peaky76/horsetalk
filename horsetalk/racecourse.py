from .handedness import Handedness
from .racecourse_contour import RacecourseContour
from .racecourse_shape import RacecourseShape
from .racecourse_style import RacecourseStyle
from .surface import Surface


class Racecourse:
    def __init__(self, name: str, surface: Surface, **kwargs):
        self.name = name
        self.surface = surface
        self.handedness = Handedness[kwargs.get("handedness", "unknown")]
        self.contour = RacecourseContour[kwargs.get("contour", "unknown")]
        self.shape = RacecourseShape[kwargs.get("shape", "unknown")]
        self.style = RacecourseStyle[kwargs.get("style", "unknown")]
