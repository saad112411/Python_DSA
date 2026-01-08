#Input: nums = [3,4,5,1,2]
#Output: true
#Explanation: [1,2,3,4,5] is the original sorted array.
#You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
def is_arr(arr):
    n=len(arr)
    breaks=0
    for i in range(n):
        if arr[i]>arr[(i+1)%n]:
            breaks+=1
    return breaks<=1

arr=[3,4,5,1,2,2]
print(is_arr(arr))



