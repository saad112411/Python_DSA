"""
Given an integer array of size n containing distinct values in the range from 0 to n (inclusive),
return the only number missing from the array within this range.

Input: nums = [0, 2, 3, 1, 4]
Output: 5
Explanation:
nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]
"""
def sorting_of_arry(new_arr):
    if len(new_arr)<=1:
        return new_arr
    index=len(new_arr)//2
    piviot=new_arr[index]
    left=[x for x in new_arr if x<piviot]
    medium=[x for x in new_arr if x==piviot]
    right=[x for x in new_arr if x>piviot]

    return sorting_of_arry(left)+medium+sorting_of_arry(right)

def Find_missing_number(arr):
    After_sorting =sorting_of_arry(arr)
    for i in range(len(arr)):
        if i!=After_sorting[i]:
            return i
    return len(After_sorting)

arr=[0, 2, 3, 1, 4]
print(Find_missing_number(arr))