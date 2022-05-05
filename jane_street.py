# Q1 
# The United States uses the imperial system of weights and measures, which means that there are many different,
# seemingly arbitrary units to measure distance. There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain,
# and so on. Create a data structure that can efficiently convert a certain quantity of one unit to the correct amount
# of any other unit. You should also allow for additional units to be added to the system.


class UnitConverter:
    # intiializations for the Unit converter class function
    def __init__(self):
        self.conv_unit = None
        self.units = dict()

    # add the source units and target units to the dictionary
    def add_units(self, unit_array, conversion):
        (known_unit, new_unit) = unit_array
        if not self.conv_unit:
            self.conv_unit = known_unit
            self.units[known_unit] = 1

        assert known_unit in self.units or unit_array[1] in self.units
        self.units[new_unit] = \
            (conversion[1] / conversion[0]) * \
            self.units[known_unit]

    def convert(self, source_unit, source_quantity, target_unit):
        assert source_unit in self.units and target_unit in self.units
        source_conv = source_quantity / self.units[source_unit]
        return round(source_conv * self.units[target_unit], 2)


# Testing code
uc = UnitConverter()
# Add the unit conversion to the dictionary
uc.add_units(("inch", "foot"), (12, 1))
uc.add_units(("foot", "yard"), (3, 1))
uc.add_units(("yard", "chain"), (22, 1))

# Testing to see if the unit converter works
uc.convert("inch", 24, "foot")

# Alternatively
class UnitConverter:
    def __init__(self):
        self.metrics = {
            "inch": 1,
            "foot": 1 * 12,
            "yard": 3 * 1 * 12,
            "chain": 22 * 3 * 1 * 12,
        }

    def add_converts(self, new_unit, current_unit, value):
        if current_unit not in self.metrics:
            print(f"This unit {current_unit} does not exist")
        self.metrics[new_unit] = self.metrics[current_unit] * value

    def convert(self, orig_unit, result_unit, value):
        if orig_unit not in self.metrics:
            raise ValueError(f'{orig_unit} not found in the list')
        if result_unit not in self.metrics:
            raise ValueError(f'{result_unit} not found in the list')
        return round(value * self.metrics[orig_unit] / self.metrics[result_unit], 5)


if __name__ == "__main__":
    uc = UnitConverter()
    print(uc.convert("inch", "foot", 24))
    print(uc.convert("inch", "yard", 36))
    uc.add_converts("furlong", "chain", 10)
    print(uc.convert("furlong", "yard", 36))
    
    
    

# Q2
# Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:
# a + b = M
# a XOR b = N

# Question is a little unclear, do (1, 5) and (5, 1) count as 2 or 1.
def find_pairs(m, n):
    count = 0
    # reason we use range(m //2 + 1) is because this will ensure that a + b always equal to m and we only have to check
    # it for (half the length) times
    for a in range(m//2 + 1):
        b = m - a 
        if a ^ b == n:
            count += 1
    return count


m = 6
n = 4
print(find_pairs(m, n))



