#Input: nums = [1, 2, 3, 4, 5, 6], k = 2
#Output: nums = [3, 4, 5, 6, 1, 2]
#Explanation:
#rotate 1 step to the left: [2, 3, 4, 5, 6, 1]
#rotate 2 steps to the left: [3, 4, 5, 6, 1, 2]
def reotate_by_k(arr,k):
    if len(arr)==0:
        return "array is empty "
    for i in range(0,k):
        arr.append(arr.pop(0))
    return arr

arr=[1, 2, 3, 4, 5, 6]
k = 2
print(reotate_by_k(arr,k))
