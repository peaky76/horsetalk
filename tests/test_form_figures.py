from horsetalk import Disaster, FinishingPosition, FormBreak, FormFigures


def test_form_figures_parse_returns_list():
    expected = list
    actual = type(FormFigures.parse(""))
    assert expected == actual


def test_form_figures_parse_returns_correct_values_in_list():
    expected = [
        FinishingPosition(4),
        FormBreak.SEASON,
        FinishingPosition(0),
        FormBreak.YEAR,
        Disaster.FELL,
        FinishingPosition(0),
        FinishingPosition(2),
        Disaster.UNSEATED_RIDER,
        FinishingPosition(1),
    ]
    actual = FormFigures.parse("4/0-F02U1")
    assert expected == actual
