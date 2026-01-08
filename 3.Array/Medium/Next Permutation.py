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
def Next_prmutaion(arr):
    #find the index
    n=len(arr)
    my_index=0
    for i in range(n-1,-1,-1):
        if arr[i-1]<arr[i]:
            my_index=i-1
            break

    # find the larger element form right side 
    
    if my_index!= (-1):
        swap_index=my_index
        for i in range(n-1,my_index,-1):
            if arr[i]>arr[my_index]:
                swap_index=i
                break
    # swap that my_index to Swap_index
        arr[my_index],arr[swap_index],arr[swap_index],arr[my_index]
    
    # now revesrse the arry after my index
    left=my_index+1
    right=n-1
    while(right>left):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr

arr=[1,2,3]
print(Next_prmutaion(arr))
