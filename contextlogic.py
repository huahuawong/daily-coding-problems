# 1. Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.

# Since we can't use mult, division or modulus, what we can do is simply subtracting the divisor by the dividend, and keep incrementing the count until dividend >= divisor
# The other thing to keep note is to take care of the negative sign. We can define sign as negative if either the divider or the divisor is negative, if not it is a postive 1

# Function to divide a by b and
# return floor value it
def divide(dividend, divisor):
 
    # Calculate sign of divisor i.e.,
    # sign will be negative only iff
    # either one of them is negative
    # otherwise it will be positive
    sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1
     
    # Update both divisor and
    # dividend positive
    dividend = abs(dividend)
    divisor = abs(divisor)
     
    # Initialize the quotient
    quotient = 0
    while (dividend >= divisor):
        dividend -= divisor
        quotient += 1
         
     #if the sign value computed earlier is -1 then negate the value of quotient
  
    if sign ==-1:
      quotient=-quotient
     
    return quotient
