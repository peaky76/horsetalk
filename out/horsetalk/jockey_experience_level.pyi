from peak_utility.enumeration.parsing_enum import ParsingEnum  # type: ignore as ParsingEnum

class JockeyExperienceLevel(ParsingEnum):
    AMATEUR: int
    CONDITIONAL: int
    APPRENTICE: int
    PROFESSIONAL: int
    AMATEURS = AMATEUR
    CONDITIONALS = CONDITIONAL
    APPRENTICES = APPRENTICE
    PROFESSIONALS = PROFESSIONAL
