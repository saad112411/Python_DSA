"""
Given an integer array nums, find the subarray with the largest sum and return the sum of the 
elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.
Examples:
Input: nums = [2, 3, 5, -2, 7, -4]
Output: 15
Explanation:
The subarray from index 0 to index 4 has the largest sum = 15
"""
#using kadanes Algoritham its time complexity is O(n)
def Kadanes_algorithm(arr):
    current_sum=arr[0]
    Largest_sum=arr[0]
    for i in arr[1:]:
        current_sum=max(i,current_sum+i)
        Largest_sum=max(current_sum,Largest_sum)
    return Largest_sum
arr=[-2, -3, -7, -2, -10, -4]
print(Kadanes_algorithm(arr))

# it is a better a better Solution its time complexity is O(n^2)
def print_all_subarry_better_sol(arr):
    n=len(arr)
    maximum=0
    Largest_sum=0
    for i in range(n):
        Largest_sum=0
        for j in range(i,n):
            Largest_sum+=arr[j]
            maximum=max(maximum,Largest_sum)
    return maximum

#arr=[2, 3, 5, -2, 7, -4]
#print(print_all_subarry_better_sol(arr))

# this is the brute force Method its time complexity is O(n^3)
def print_all_subarry_brute_force_sol(arr):
    n=len(arr)
    current_sum=0
    sum=0
    for i in range(n):
        for j in range(i,n):
            current_sum=0
            for k in range(i,j+1):
                current_sum+=arr[k]
            sum=max(current_sum,sum)
    return sum
    

#arr=[0, 1, 4, 0,2,-15, 5, 2,-2]
#print(print_all_subarry_brute_force_sol(arr))