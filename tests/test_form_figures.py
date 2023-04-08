from horsetalk import Disaster, FinishingPosition, FormBreak, FormFigures


def test_form_figures_parse_returns_list():
    expected = list
    actual = type(FormFigures.parse(""))
    assert expected == actual


def test_form_figures_parse_returns_correct_enums_in_list():
    expected = [
        FinishingPosition.FOURTH,
        FormBreak.SEASON,
        FinishingPosition.UNPLACED,
        FormBreak.YEAR,
        Disaster.FELL,
        FinishingPosition.UNPLACED,
        FinishingPosition.SECOND,
        Disaster.UNSEATED_RIDER,
        FinishingPosition.FIRST,
    ]
    actual = FormFigures.parse("4/0-F02U1")
    assert expected == actual
