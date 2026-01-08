#Counting Frequencies of Array Elements
#Input: nums = [1, 2, 2, 1, 3]
#Output: [[1, 2], [2, 2], [3, 1]]

def counting_freq(arr):
    final_arr=[]
    max_elemnt=max(arr)+1
    arr_len=len(arr)
    new_arr=[0]*max_elemnt
    for i in range(arr_len):
        new_arr[arr[i]]=new_arr[arr[i]]+1
    for i in range(len(new_arr)):
        if new_arr[i]!=0:
            result=[i,new_arr[i]]
            final_arr.append(result)
            
    
    return final_arr

arr=[5, 5, 5, 5]
print(counting_freq(arr))