from horsetalk import Breed


def test_breed_can_be_created_from_enum():
    assert Breed.THOROUGHBRED == Breed(1)


def test_breed_can_be_created_from_name():
    assert Breed.THOROUGHBRED == Breed["THOROUGHBRED"]


def test_breed_can_be_created_from_abbreviation():
    assert Breed.THOROUGHBRED == Breed["TB"]
