"""
A permutation of an array of integers is an arrangement of its members into a sequence 
or linear order.
For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of 
its integers.
More formally, if all the permutations of the array are sorted in lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted order.
If such arrangement is not possible (i.e., the array is the last permutation), 
then rearrange it to the lowest possible order (i.e., sorted in ascending order).
You must rearrange the numbers in-place and use only constant extra memory.
Input: nums = [3,2,1]
Output: [1,2,3]
Explanation:
[3,2,1] is the last permutation. So we return the first: [1,2,3].
"""

def next_permutation(arr):
    pivot=-1
    n=len(arr)
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            pivot=i
            break
    if pivot==-1:
        arr.reverse()
        return arr
    # we need to find the element that is greether than pivot but it is min from right till pivot.
    swaped_index=pivot
    for i in range(n-1,pivot,-1):
        if arr[i]>arr[pivot]:
            swaped_index=i
            break
    arr[swaped_index],arr[pivot]=arr[pivot],arr[swaped_index]
    left= pivot+1
    Right=n-1
    while(left<Right):
        arr[left],arr[Right]=arr[Right],arr[left]
        left+=1
        Right-=1

    # then we swaped that element swap
    return arr



arr=[1,3,2]
print(next_permutation(arr))
