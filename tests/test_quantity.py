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

def test_horsetalk_quantity_attribute_access():
    q = HorsetalkQuantity("5kg")
    assert q.kg == 5