# Q1
# This problem was asked by Palantir.
# The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. 
# For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.
# Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.

import math
from fractions import Fraction

def find_egypr_fac(fraction, frac_list = list()):
    if fraction.numerator > fraction.denominator:
        return "Invalid value of fractions. PLease try again!"

    if fraction.numerator == 1:
        frac_list.append(fraction)
        return frac_list

    egypt_fac = Fraction(1, math.ceil(fraction.denominator/ fraction.numerator))
    frac_list.append(egypt_fac)

    new_frac = fraction - egypt_fac
    return find_egypr_fac(new_frac, frac_list)


print(find_egypr_fac(Fraction(7, 13)))
