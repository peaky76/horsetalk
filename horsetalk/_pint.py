from pint import UnitRegistry

ureg = UnitRegistry()
ureg.define('hand = 4 * inch = hh')
Q_ = ureg.Quantity
