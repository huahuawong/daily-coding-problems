# 1 Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the
# equation a^2+ b^2= c^2.

def find_pythagoras(num1, num2, num3):
    return (num1 ** 2) + (num2 ** 2) == (num3 ** 2)
    
print(find_pythagoras(3, 4, 5))

