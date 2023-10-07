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

    def __repr__(self):
        """
        Returns the age restriction as a repr.

        Returns:
            The age restriction as a repr.
        """
        return f"<AgeRestriction: {str(self)}>"

    def __str__(self):
        """
        Returns the age restriction as a string.

        Returns:
            The age restriction as a string.
        """
        if self.minimum == self.maximum:
            return f"{self.minimum}yo"
        elif self.maximum:
            return f"{self.minimum}-{self.maximum}yo"
        else:
            return f"{self.minimum}yo+"
