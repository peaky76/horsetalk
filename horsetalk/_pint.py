from pint import UnitRegistry

ureg = UnitRegistry()
ureg.define('hand = 4 * inch = hh')
ureg.define('furlong = 0.125 * mile = f')
ureg.define('@alias yard = y')
Q_ = ureg.Quantity
