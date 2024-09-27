from enum import Enum


class Country(Enum):
    """
    An enumeration representing a country.

    """

    ARG = "Argentina"
    AUS = "Australia"
    AUT = "Austria"
    AZE = "Azerbaijan"
    BHR = "Bahrain"
    BAR = "Barbados"
    BEL = "Belgium"
    BOS = "Bosnia"
    BRZ = "Brazil"
    BUL = "Bulgaria"
    CAN = "Canada"
    CHI = "Chile"
    CHN = "China"
    COL = "Colombia"
    CRO = "Croatia"
    CYP = "Cyprus"
    CZE = "Czech Republic"
    DEN = "Denmark"
    DOM = "Dominican Republic"
    ECU = "Ecuador"
    FIN = "Finland"
    FR = "France"
    GER = "Germany"
    GB = "Great Britain"
    GR = "Greece"
    HER = "Herzegovina"
    HUN = "Hungary"
    IND = "India"
    IRE = "Ireland"
    IRN = "Iran"
    ITY = "Italy"
    JAM = "Jamaica"
    JPN = "Japan"
    KEN = "Kenya"
    KOR = "Korea"
    LEB = "Lebanon"
    LTU = "Lithuania"
    LUX = "Luxembourg"
    MAL = "Malaysia"
    MEX = "Mexico"
    MOR = "Morocco"
    HOL = "Netherlands"
    NZ = "New Zealand"
    NOR = "Norway"
    OM = "Oman"
    PAK = "Pakistan"
    PRY = "Paraguay"
    PER = "Peru"
    PHI = "Philippines"
    POL = "Poland"
    POR = "Portugal"
    PR = "Puerto Rico"
    QA = "Qatar"
    RUM = "Romania"
    RUS = "Russia"
    KSA = "Saudi Arabia"
    SER = "Serbia"
    SVK = "Slovakia"
    SVN = "Slovenia"
    SAF = "South Africa"
    SPA = "Spain"
    SWE = "Sweden"
    SWI = "Switzerland"
    SY = "Syria"
    TRI = "Trinidad and Tobago"
    TUN = "Tunisia"
    TUR = "Turkey"
    UAE = "United Arab Emirates"
    USA = "United States of America"
    URU = "Uruguay"
    UZB = "Uzbekistan"
    VEN = "Venezuela"
    ZIM = "Zimbabwe"

    def __str__(self):
        return self.value
