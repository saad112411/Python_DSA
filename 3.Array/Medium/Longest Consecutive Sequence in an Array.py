"""
Given an array nums of n integers.
Return the length of the longest sequence of consecutive integers. 
The integers in this sequence can appear in any order.
Examples:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation:
The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4. 
This sequence can be formed regardless of the initial order of the elements in the array.
"""
# this will take(nlogn)
def LOngest_sequemnce(arr):
    arr.sort()
    count_before=1
    count_after=1
    n=len(arr)
    for i in range(n-1):
        if arr[i+1]==arr[i]:
            continue
        elif arr[i+1]-arr[i]==1 or 0:
            count_before+=1
        else:
            count_before=1
        count_after=max(count_before,count_after)
    return count_after
#arr= [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
#print(LOngest_sequemnce(arr))


#optimal solution that take O(n)
def Longest_sequnce_optimal(arr):
    pass
    # we can only iterate if the min elemet

arr= [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

