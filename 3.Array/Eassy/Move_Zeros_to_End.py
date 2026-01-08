#Move all Zeros to End
#Input: nums = [0, 1, 4, 0, 5, 2]
#Output: [1, 4, 5, 2, 0, 0]
#Explanation:
#Both the zeroes are moved to the end and the order of the other elements stay the same

def move_zero_to_last(arr):
    print("the orignal arry is :",arr)
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
        print(f"in the {i}th iteration ",arr)
    return "the final result is ",arr

arr  = [0, 1, 4, 0, 5, 2]
print(move_zero_to_last(arr))

"""
def move_zero_to_last(arr):
    no_of_zero=0
    lenth=len(arr)
    zeros=arr.count(0)
    for i in range(lenth-zeros):
        if arr[i]==0:
            arr.pop(i)
            no_of_zero+=1
    for k in range(no_of_zero):
        arr.append(0)
    return arr

"""

