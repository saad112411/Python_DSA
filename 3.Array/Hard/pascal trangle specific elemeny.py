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


def get_pascal_element(row,index):
    row_val=1
    index_val=1
    row_min_ind=row-index
    min_val=1
    for i in range(2,row+1):
        row_val*=i
    for i in range(2,index+1):
        index_val*=i
    for i in range(2,row_min_ind+1):
        min_val*=i
    return int((row_val)/(index_val*min_val))

print(get_pascal_element(row=30,index=3))
    