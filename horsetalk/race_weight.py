import re
from measurement.measures import Weight  # type: ignore


class RaceWeight(Weight):
    """
    A thin wrapper around the measurement library Weight class to allow for the creation of Weight objects
    from strings.
    """

    # REGEX = r"((?:\d+(?:m|f|y)\s*)+)"

    def __init__(self, weight: str):
        """
        Initialize a RaceWeight object from a string.
        """

        st, lbs = weight.split("-")
        super().__init__(self, lb=(int(st) * 14 + int(lbs)))  # type: ignore

    def __repr__(self) -> str:
        """
        Returns the weight as a string.
        """
        return f"<RaceWeight: {str(self)}>"

    def __str__(self) -> str:
        """
        Returns the weight as a string.
        """
        st = int(self.lb // 14)
        lb = int(self.lb % 14)
        return f"{st}st {lb}lb"
