"""Given an integer array nums of size n, return the majority element of the array.
The majority element of an array is an element that appears more than n/2 times in the array.
The array is guaranteed to have a majority element.
Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

Output: 7
Explanation:
The number 7 appears 5 times in the 9 sized array
"""

# solve also by Moore's Voting Algorithm
def majority_element_optimal(arr):
    count=0
    candidate=0
    for num in arr:
        if count==0:
            candidate=num
        if num==candidate:
            count+=1
        else:
            count-=1
    return candidate
        

arr=[7, 0, 0, 1, 7, 7, 2, 7, 7]
print(majority_element_optimal(arr))

#genral method
def Majority_element(arr):
    majority_Element=len(arr)/2
    freq={}
    for i in arr:
        freq[i]=freq.get(i,0)+1
    for key,value in freq.items():
        if value>majority_Element:
            return key
    return False



#arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]
#print(Majority_element(arr))