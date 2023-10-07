import re


class AgeRestriction:
    REGEX = (
        r"(\d{1,2})[-]?(\d{1,2})?\s?y(?:ear)?(?:\s|-)?o(?:ld(?:s)?)?(?:\sonly)?(\+)?"
    )

    def __init__(self, string: str):
        """
        Initialize an AgeRestriction instance.

        Args:
            age_restriction_string: The age restriction string.

        Returns:
            An AgeRestriction instance.
        """
        groups = re.search(self.REGEX, string).groups()
        self.minimum = int(groups[0])
        self.maximum = (
            int(groups[1]) if groups[1] else None if groups[2] else self.minimum
        )
