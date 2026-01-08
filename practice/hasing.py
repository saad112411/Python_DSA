n= int(input("Enter a size of arr :"))
#Input: nums = [1, 2, 2, 1, 3]
#Output: [[1, 2], [2, 2], [3, 1]]
arr=[]
for i in range(n):
    x=int(input(f"Enter a {i}th index : "))
    arr.append(x)
#m=int(input("enter the size of hash index we want :"))
hash_arr=[0]*20
for i in range(n):
    hash_arr[arr[i]]+=1

print(hash_arr)
    

