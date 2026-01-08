
# pivot is in the middle 
def Quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in  arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return Quick_sort(left)+middle+Quick_sort(right)
        



arr=[1,2,5,8,9]
print(Quick_sort(arr))