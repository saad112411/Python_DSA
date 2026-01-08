"""
Given an array of nums of n integers. Every integer in the array appears twice except one integer.
Find the number that appeared once in the array.

Input : nums = [1, 2, 2, 4, 3, 1, 4]
Output : 3
Explanation : The integer 3 has appeared only once.
"""
def Single_number(arr):
    freq={}
    for i in arr:
        freq[i]=freq.get(i,0)+1
    minimum=min(freq.values())
    return [key for key,value in freq.items() if value==minimum][0]


arr=[1, 2, 2, 4, 3, 1, 4,3,-1]
print(Single_number(arr))
