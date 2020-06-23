# Q1 This problem was asked by Twitter.

# A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. For example, 
# 16891 is strobogrammatic.

# Create a program that finds all strobogrammatic numbers with N digits.
def get_strob(n_digits):
    if not n_digits:
        return [""]
    elif n_digits == 1:
        return ['0', '1', '8']
        
    small_numbers = get_strob(n_digits-2)
    list_of_small = list()
    for num in small_numbers:
        list_of_small.extend([
            "1" + num + "1",
            "6" + num + "9",
            "9" + num + "6",
            "8" + num + "8",
        ])
    return list_of_small
    
print(get_strob(3))
        
