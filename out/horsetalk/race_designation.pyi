from .parsing_enum import ParsingEnum as ParsingEnum

class RaceDesignation(ParsingEnum):
    HANDICAP: int
    CONDITIONS: int
    AUCTION: int
    CLAIMER: int
    SELLER: int
    HCAP = HANDICAP
    AU = AUCTION
    CL = CLAIMER
    S = SELLER
    CLAIMING = CLAIMER
    SELLING = SELLER
