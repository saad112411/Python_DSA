def pascal_tringle_sol(row_num):
    final_result=[]
    for i in range(row_num):
        row=[1]
        if i>0:
            privouse_row=final_result[-1]
            for j in range(len(privouse_row)-1):
                row.append(privouse_row[j]+privouse_row[j+1])
            row.append(1)
        final_result.append(row)
    return final_result
            
row_num=int(input("Enter a row :"))
print(pascal_tringle_sol(row_num))

def pascal_trinagle_brute_force(n):
    My_list=[1]*n*2
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j==1 or j==i:
                print(1,end="")
            else:
                My_list[j-1]=My_list[j]+My_list[j-1]
                print(My_list[j-1],end="")
        print()
    return 
#print(pascal_trinagle_brute_force(6))

