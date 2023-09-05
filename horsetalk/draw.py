class Draw:
    def __init__(self, value: int | str) -> None:
        """
        Initialize a Draw instance.

        Args:
            value: The stall number in which the horse is drawn.
        """
        if not str(int(value)) == str(value):
            raise ValueError("Draw must be an integer value")

        self.value = int(value)
