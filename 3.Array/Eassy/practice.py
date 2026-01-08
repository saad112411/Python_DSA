def single_number_xor(nums):
    # Start with a result of 0
    result = 0
    # XOR each number in the array with the result
    for num in nums:
        result = result ^ num
    return result

arr = [1, 2, 2, 4, 3, 1, 4,4,2]
print(single_number_xor(arr))