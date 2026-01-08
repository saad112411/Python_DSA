""" in dict if i itrate only by one parameter then we accsess key only """
def brute_force(arr,k):
    # it take o(n*n) time comlexity 
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==k:
                return [i,j]

def optinmal_solution(arr,k):
    #using hashig it take o(n) time complexity 
    n=len(arr)
    my_dict={}
    for i,num in enumerate(arr):
        diff=k-num
        if diff in my_dict:
            return[my_dict[diff],i]
        my_dict[num]=i
        


arr=[2,3,3,5]
#print(brute_force(arr,6))
print(optinmal_solution(arr,6))
