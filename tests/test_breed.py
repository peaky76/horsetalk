from horsetalk import Breed


def test_breed_can_be_created_from_enum():
    assert Breed(1) == Breed.THOROUGHBRED


def test_breed_can_be_created_from_name():
    assert Breed["THOROUGHBRED"] == Breed.THOROUGHBRED


def test_breed_can_be_created_from_lowercase_name():
    assert Breed["thoroughbred"] == Breed.THOROUGHBRED


def test_breed_can_be_created_from_abbreviation():
    assert Breed["TB"] == Breed.THOROUGHBRED
