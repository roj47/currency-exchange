class Currency:

    currencies =  {'CHF': 0.930023, # swiss franc 
                   'CAD': 1.264553, # canadian dollar
                   'GBP': 0.737414, # british pound
                   'JPY': 111.019919, # japanese yen
                   'EUR': 0.862361, # euro
                   'USD': 1.0}      # us dollar
      
    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def changeTo(self, new_unit):
        """
        A Currency object is transformed from the unit "self.unit" to "new_unit"
        """
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit
  
    # add magic methods here
    def __repr__(self):
        return f"{self.value:.2f} {self.unit}"
  
    def __str__(self):
        return self.__repr__()
  
    def __add__(self, other):
        if isinstance(other, Currency):
            other_value_in_self_unit = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
            return Currency(self.value + other_value_in_self_unit, self.unit)
        elif isinstance(other, (int, float)):
            other_value_in_self_unit = other * Currency.currencies["USD"] / Currency.currencies[self.unit]
            return Currency(self.value + other_value_in_self_unit, self.unit)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Currency):
            other_value_in_self_unit = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
            return Currency(self.value - other_value_in_self_unit, self.unit)
        elif isinstance(other, (int, float)):
            other_value_in_self_unit = other * Currency.currencies["USD"] / Currency.currencies[self.unit]
            return Currency(self.value - other_value_in_self_unit, self.unit)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            other_value_in_self_unit = other * Currency.currencies["USD"] / Currency.currencies[self.unit]
            return Currency(other_value_in_self_unit - self.value, self.unit)
        else:
            return NotImplemented

# Example usage
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3)  # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3)  # an int or a float is considered to be a USD value
print(30 - v2)
