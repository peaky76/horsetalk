import re
from .racing_code import RacingCode


class RaceGrade:
    def __init__(self, grade: str | int | None, racing_code: RacingCode = None):
        if not grade:
            self.value = None
            code_from_grade = None
        else:
            stripped_grade = re.sub(r"G(?:roup|rade|)\s*", "", str(grade).title())

            if not stripped_grade.isdigit() and stripped_grade != "Listed":
                raise ValueError(f"Grade must be a number or 'Listed', not {grade}")

            if stripped_grade.isdigit() and not 1 <= int(stripped_grade) < 4:
                raise ValueError(f"Grade must be between 1 and 3, not {grade}")

            self.value = stripped_grade

            code_from_grade = (
                RacingCode.NATIONAL_HUNT
                if "grade" in str(grade).lower()
                else RacingCode.FLAT
                if "group" in str(grade).lower()
                else None
            )

        if code_from_grade and racing_code and code_from_grade != racing_code:
            raise ValueError(
                f"{grade} conflicts with value for racing code: {racing_code.value}"
            )

        self.racing_code = code_from_grade or racing_code or RacingCode.FLAT

    def __repr__(self):
        return f"<RaceGrade: {self.value}>"

    def __str__(self):
        if not self.value:
            return ""

        title = "Grade" if self.racing_code == RacingCode.NATIONAL_HUNT else "Group"
        return "Listed" if not self.value.isdigit() else f"{title} {self.value}"

    def __bool__(self):
        return bool(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        if not self.value:
            return other.value

        if not self.value.isdigit():
            return other.value.isdigit()

        return other.value.isdigit() and self.value > other.value

    def __gt__(self, other):
        if not self.value:
            return False

        return self.value.isdigit() and (
            not other.value or not other.value.isdigit() or self.value < other.value
        )
