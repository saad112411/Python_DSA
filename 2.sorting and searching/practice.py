# bubble sor works on swapping addjusent element and in lasst of each iteration
# the it sorted form right to left 

def buble_sort(arr):
    arr_size=len(arr)
    for i in range(arr_size):
        flag=False
        minimun=i
        for j in range(0,arr_size-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True
        if not flag:
            break
    return arr



arr =[5,10,12,18,9,60,7]
print(buble_sort(arr))