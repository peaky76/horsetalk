from enum import Enum, EnumMeta


class CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(cls, name):
        for member in cls.__members__:
            if member == name.upper():
                return cls.__members__[member]
        raise KeyError(name)


class CaseInsensitiveEnum(Enum, metaclass=CaseInsensitiveEnumMeta):
    pass


class SpaceAndCaseInsensitiveEnumMeta(CaseInsensitiveEnumMeta):
    def __getitem__(cls, name):
        return super().__getitem__(name.replace("-", " ").replace(" ", "_"))


class SpaceAndCaseInsensitiveEnum(
    CaseInsensitiveEnum, metaclass=SpaceAndCaseInsensitiveEnumMeta
):
    pass


class ParsingEnumMeta(EnumMeta):
    def __getitem__(cls, name):
        for member in cls.__members__:
            if member == name.replace("-", " ").replace(" ", "_").upper():
                return cls.__members__[member]
        raise KeyError(name)


class ParsingEnum(Enum, metaclass=ParsingEnumMeta):
    pass
