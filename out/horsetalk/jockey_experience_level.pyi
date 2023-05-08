from .parsing_enum import ParsingEnum as ParsingEnum

class JockeyExperienceLevel(ParsingEnum):
    AMATEUR: int
    CONDITIONAL: int
    APPRENTICE: int
    PROFESSIONAL: int
    AMATEURS = AMATEUR
    CONDITIONALS = CONDITIONAL
    APPRENTICES = APPRENTICE
    PROFESSIONALS = PROFESSIONAL
