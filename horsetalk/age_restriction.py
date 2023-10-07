class AgeRestriction:
    def __init__(self, string: str):
        """
        Initialize an AgeRestriction instance.

        Args:
            age_restriction_string: The age restriction string.

        Returns:
            An AgeRestriction instance.
        """
        string = string.replace("yo", "")
        self.minimum = int(string[0])
        self.maximum = (
            None
            if "+" in string
            else int(string.split("-")[1])
            if "-" in string
            else int(string)
        )
