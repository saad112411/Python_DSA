#Input: nums = [,1,8, 8, 7, 6, 5]
#Output: 7
#Explanation:
#The largest value in nums is 8, the second largest is 7

def second_larg(arr):
    if len(arr)<2:
        return "Minimum arry size should be 2"
    largest=float('-inf')
    second_largest=float('-inf')

    for i in arr:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest and  i!=largest:
            second_largest =i
    return second_largest

arr=[5,1,8, 8, 7, 6, 5]
print(second_larg(arr))

        
        




"""
this is fail becuse if all number is same so other list is empthy 
def Secon_largest_element(arr):
    maximum=arr[0]
    for i in arr:
        if i>maximum:
            maximum=i
    lis=[]
    for i in arr:
        if i!=maximum:
            lis.append(i)
    print(lis)
    Second_Higest=lis[0]
    for i in lis:
        if i>Second_Higest:
            Second_Higest=i
    return Second_Higest

arr=[0,1,8, 8, 7, 6, 5]
print(Secon_largest_element(arr))
"""