import pytest

from horsetalk.quantity import HorsetalkQuantity


def test_horsetalk_quantity_creation_from_string():
    q = HorsetalkQuantity("10km")
    assert q.magnitude == 10
    assert str(q.units) == "kilometer"

def test_horsetalk_quantity_creation_from_tuple():
    q = HorsetalkQuantity(5, "kg")
    assert q.magnitude == 5
    assert str(q.units) == "kilogram"

def test_horsetalk_quantity_creation_from_kwargs():
    q = HorsetalkQuantity(kg=5)
    assert q.magnitude == 5
    assert str(q.units) == "kilogram"

def test_horsetalk_quantity_representation():
    q = HorsetalkQuantity("3km")
    assert repr(q) == "<HorsetalkQuantity: 3 kilometres>"

def test_horsetalk_quantity_attribute_accesswith_legitimate_unit():
    q = HorsetalkQuantity("5kg")
    assert q.kg == 5

def test_horsetalk_quantity_attribute_access_with_illegitimate_unit():
    q = HorsetalkQuantity("5kg")
    with pytest.raises(AttributeError):
        q.smidgen


def test_horsetalk_quantity_subclass_can_have_extra_attributes():

    class MyQuantity(HorsetalkQuantity):
        
        _extra_attr = None

        @property
        def extra_property(self):
            return 42

        def extra_method(self):
            return str(self)

    q = MyQuantity("5kg")

    assert q._extra_attr is None
    assert q.extra_property == 42
    assert q.extra_method() == "5 kilograms"