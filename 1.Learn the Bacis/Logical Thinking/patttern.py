"""
create the horizangtal tringle 
"""
def reactangel(num):
    for i in range(num):
        print("*"*num)
#reactangel(5)

"""
print the right angel tringle from left side
"""
def RATL(num):
    for i in range(1,num+1):
        print("*"*i)

#RATL(5)

"""
right angle tringle but using the number each row statrt from its 1 
"""
def RATN(num):
    s=""
    for i in range(1,num+1):
        s=s+str(i)
        print(s)
#RATN(5)

"""
print the Right angle tringle which each row value is same as its index 
"""
def R_A_T_Same_row(num):
    for i in range(1,num+1):
        print(f"{i}"*i)

#R_A_T_Same_row(5)

"""
print the invese right angle tringle using stars
"""
def Reverse_RAT(num):
    for i in range(num,0,-1):
        print("*"*i)

#Reverse_RAT(5)


"""
right angle tringle but using the number each row statrt from its 1 
"""
def inverse_RAT(num):
    for i in range(num,0,-1):
        for j in range(1,i+1):
            print(j,end="")
        print()
       
#inverse_RAT(5)

"""
print the paramid 
"""
def paramid(num):
    space =num-1
    star=1
    for i in range(1,num+1):
        print(" "*space,"*"*star)
        space-=1
        star+=2
#paramid(5)


"""
print the reverse pyramid 
"""
def revese_pyramid(num):
    star=num*2-1
    space=0
    for i in range(num):
        print(" "*space,"*"*star)
        star-=2
        space+=1

#revese_pyramid(5)

"""
print the alternate(0,1) right angle trangel
"""
def Al_RAT(num):
    for i in range(1,num+1):
        start= 0 if i%2==0 else 1
        for j in range(0,i):
            start=start%2
            print(start,end="")
            start+=1
        print()

#Al_RAT(5)

"draw a patten that represent the hallow dimond:"
def hallow_dimond(num):
    space=0
    star=num
    for i in range(1,2*num):
        print("*"*star+" "*space+"*"*star)
        if i<num:
            star-=1
            space+=2
        else:
            star+=1
            space-=2


hallow_dimond(4)

