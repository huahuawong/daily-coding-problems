# Q1
# Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. 
# Create an algorithm to find the nth sevenish number.

index = 8
sevenish = []
i = 0
while len(sevenish) < index:
	#all powers of seven would be sevenish 
    sevenish.append(7**i)
    last_index = len(sevenish)-1
    if len(sevenish) == index:
        break
    for num in range(len(sevenish)-1):
    	#adding the current power of seven to all the present elements
        sevenish.append(sevenish[last_index]+sevenish[num])
        if len(sevenish) == index:
            break
    i = i + 1
print('The {} sevenish number is {}'.format(index, sevenish.pop()))
