import re
from peak_utility.number import RepresentationalInt
from .racing_code import RacingCode


class RaceGrade(RepresentationalInt):
    REGEX = r"G(?:roup|rade|)\s*"

    def __new__(cls, grade: str | int | None, racing_code: RacingCode = None):
        grade_value = re.sub(RaceGrade.REGEX, "", str(grade or "").title())

        if grade_value.isdigit() and 1 <= int(grade_value) < 4:
            grade_value = int(grade_value)
        elif grade_value == "Listed":
            grade_value = 4
        elif int(bool(grade_value)) == 0:
            grade_value = 5
        else:
            raise ValueError(f"{grade} is not a valid RaceGrade")

        code_from_grade = {
            "grade": RacingCode.NATIONAL_HUNT,
            "group": RacingCode.FLAT,
            "default": None,
        }[
            next(
                (x for x in ["grade", "group"] if x in str(grade).lower()),
                "default",
            )
        ]

        if code_from_grade and racing_code and code_from_grade != racing_code:
            raise ValueError(
                f"{grade} conflicts with value for racing code: {racing_code.value}"
            )

        instance = super().__new__(cls, grade_value)
        instance.racing_code = code_from_grade or racing_code or RacingCode.FLAT
        return instance

    def __repr__(self):
        return f"<RaceGrade: {str(int(self)) or 'None'}>"

    def __str__(self):
        if super().__eq__(5):
            return ""
        if super().__eq__(4):
            return "Listed"
        if self.racing_code == RacingCode.NATIONAL_HUNT:
            return "Grade " + str(int(self))

        return "Group " + str(int(self))

    def __bool__(self):
        return self != 5

    def __eq__(self, other):
        if isinstance(other, RaceGrade) or (isinstance(other, int) and other < 4):
            return super().__eq__(other)

        return False

    def __lt__(self, other):
        return super().__gt__(other)

    def __gt__(self, other):
        return super().__lt__(other)
