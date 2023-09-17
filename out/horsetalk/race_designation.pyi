from peak_utility.enumeration.parsing_enum import ParsingEnum  # type: ignore as ParsingEnum

class RaceDesignation(ParsingEnum):
    HANDICAP: int
    CONDITIONS: int
    MAIDEN: int
    AUCTION: int
    CLAIMER: int
    SELLER: int
    HCAP = HANDICAP
    AU = AUCTION
    CL = CLAIMER
    M = MAIDEN
    S = SELLER
    CLAIMING = CLAIMER
    SELLING = SELLER
