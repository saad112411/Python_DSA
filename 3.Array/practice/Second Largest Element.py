"""
Given an array of integers nums, return the second-largest element in the array. 
If the second-largest element does not exist, return -1.
Examples:
Input: nums = [8, 8, 7, 6, 5]
Output: 7
Explanation:
The largest value in nums is 8, the second largest is 7
"""

# this code required o(n)+o(n) time comlexity
def brute_force(arr):
    largest=arr[0]
    for num in arr:
        if largest<num:
            largest=num
    current_element=-1
    for num in arr:
        if num!=largest and current_element<num:
            current_element=num
    return current_element
#arr=[8, 8, 7, 6, 5]
#print(brute_force(arr))


# this solution will run in o(n) time 
def optimal_solution(arr):
    largest_element=arr[0]
    currunt_element=float("-inf")
    for num in arr:
        if num>largest_element:
            currunt_element=largest_element
            largest_element=num

        if num!=largest_element and currunt_element<num:
            currunt_element=num
    return currunt_element

arr=[8, 8, 7, 6, 5]
print(optimal_solution(arr))