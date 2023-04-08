from horsetalk import Disaster, FinishingPosition, FormBreak


class FormFigures:
    @staticmethod
    def parse(form_figures: str):
        retval = []

        for figure in form_figures:
            if figure.isdigit():
                retval.append(FinishingPosition(int(figure)))
            elif figure in [member.value for member in FormBreak]:
                retval.append(FormBreak(figure))
            else:
                retval.append(Disaster[figure])

        return retval
