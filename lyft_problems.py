# Q1
# Given a list of integers and a number K, return which contiguous elements of the list sum to K.
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

# The idea is to utilise the window subarray technique, we will iterate from the start to the end
# At the same time, we initilized a variable named curr_sum to keep track of the sum every time we iterate through the array. If the curr_sum exceeds the target, then
# we would have to minus the curr_sum with the element at the begingging of the subarray. This process is repeated until the target value is found or there are just simply
# no solutions to the question.

def find_contiguous(arr, target):
    subarr = []
    n = len(arr)
    curr_sum = 0
    start = 0
    i = 0
    
    while i <= n - 1:
        curr_num = arr[i]
        curr_sum += arr[i]
        subarr.append(curr_num)
        
        if curr_sum == target:
                return subarr
                
        while curr_sum > target:
            curr_sum -= subarr[start]
            subarr.pop(start)
            # Update starting index of the array
            # start += 1
            if curr_sum == target:
                return subarr
            i += 1
            continue
        
        i += 1
    
    return ("No subarrays found")
        

arr = [1, 2, 3, 4, 5] 
k = 15
print(find_contiguous(arr, k))







