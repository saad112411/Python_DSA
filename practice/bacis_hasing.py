
#print the hashing arry 
def counting_freq(arr):
    max_elemnt=max(arr)+1
    arr_len=len(arr)
    new_arr=[0]*max_elemnt
    for i in range(arr_len):
        new_arr[arr[i]]=new_arr[arr[i]]+1
    return new_arr

  
arr=[1,2,2,1,3,5]
print(counting_freq(arr))