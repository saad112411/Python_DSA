#Input: nums = [1, 2, 3, 4, 5]
#Output: [2, 3, 4, 5, 1]
#Explanation:
#Initially, nums = [1, 2, 3, 4, 5]
#Rotating once to left -> nums = [2, 3, 4, 5, 1]
def one_rotet(arr):
    first_element=arr[0]
    del arr[0]
    arr.append(first_element)
    return arr

arr = [1, 2, 3, 4, 5]
print(one_rotet(arr))