
def Merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    Left_arr=Merge_sort(arr[:mid])
    right_arr=Merge_sort(arr[mid:])
    return merge(Left_arr,right_arr)



def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



arr=[1,7,8,2,3]
#print(Merge_sort(arr)) 




def divide(num):
    if len(num)<2:
        return num
    mid=len(num)//2
    left_arr=divide(num[:mid])
    right_arr=divide(num[mid:])
    return conqure(left_arr,right_arr)

def conqure(left,right):
    result=[]
    i=j=0
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


num=[7, 4, 1, 5, 3]
print(divide(num)) 