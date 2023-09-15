from .racing_code import RacingCode


class RaceGrade:
    def __init__(self, grade: str | int, racing_code: RacingCode = RacingCode.FLAT):
        if str(grade).isdigit() and not 1 <= int(grade) < 4:
            raise ValueError(f"Grade must be between 1 and 3, not {grade}")

        if not str(grade).isdigit() and grade != "Listed":
            raise ValueError(f"Grade must be a number or 'Listed', not {grade}")

        self.grade = str(grade)
        self.racing_code = racing_code

    def __str__(self):
        title = "Grade" if self.racing_code == RacingCode.NATIONAL_HUNT else "Group"
        return "Listed" if not self.grade.isdigit() else f"{title} {self.grade}"

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        if not self.grade.isdigit():
            return other.grade.isdigit()

        return other.grade.isdigit() and self.grade > other.grade

    def __gt__(self, other):
        return self.grade.isdigit() and (
            not other.grade.isdigit() or self.grade < other.grade
        )
