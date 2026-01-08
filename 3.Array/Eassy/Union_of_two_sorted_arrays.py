"""
Union of two sorted arrays
Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
Output: [1, 2, 3, 4, 5, 7]
Explanation:
The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2
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

def Distinct_element(sorted_arr):
    i=0
    while(i<len(sorted_arr)-1):
        if sorted_arr[i+1]==sorted_arr[i]:
            sorted_arr.pop(i+1)
        else:
            i+=1
    return sorted_arr


def Unioin_of_arry(arr1,arr2):
    new_arr=arr1+arr2
    sorted_arr=sorting_of_arry(list(new_arr))
    return Distinct_element(sorted_arr)

nums1 = [1, 2, 3, 4, 5,2]
nums2 = [1, 2, 7]
print(Unioin_of_arry(nums1,nums2))
