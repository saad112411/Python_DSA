
#Input: nums = [3, 3, 0, 99, -40]
#Output: 99
#Explanation: The largest element in array is 99
def Largest_arr(arr):
    if not arr:
        return []
    Lenth=len(arr)
    maximum=arr[0]
    for i in arr:
        if i>maximum:
            maximum=i
    return maximum

arr = [3, 3, 0, 99, -40]
print(Largest_arr(arr))

