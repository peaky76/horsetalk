from .handedness import Handedness
from .racecourse_contour import RacecourseContour
from .racecourse_shape import RacecourseShape
from .racecourse_style import RacecourseStyle


class Racecourse:
    def __init__(self):
        self.handedness = Handedness.UNKNOWN
        self.contour = RacecourseContour.UNKNOWN
        self.shape = RacecourseShape.UNKNOWN
        self.style = RacecourseStyle.UNKNOWN
