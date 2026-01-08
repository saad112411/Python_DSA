#Input: nums = [4, 4, 5, 5,5, 6]
#Output: 4
#Explanation: Both 4 and 5 appear twice, but 4 is smaller. So, 4 is the most frequent element.
def Most_occuring_element(arr):
    arr_length=len(arr)
    largest_element=max(arr)+1
    hash_arr=[0]*largest_element
    for i in range(arr_length):
        hash_arr[arr[i]]= hash_arr[arr[i]]+1
    higest_occring=max(hash_arr)
    for i in range(len(hash_arr)):
        if hash_arr[i]!=0:
            if hash_arr[i]==higest_occring:
                return i


arr=[ 5, 5,5, 4, 4, 6]
print(Most_occuring_element(arr))
