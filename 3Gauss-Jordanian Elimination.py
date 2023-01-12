def swap(a,b):
    c=a
    a=b
    b=c
    print("A swan of rows has been made")
    
import numpy as np 


i1=(input("enter the first row"))

i2=(input("Enter the second row"))

i3=(input ("Enter the third row"))


a1=i1.split(",")
a2=i2.split(",")
a3=i3.split(",")


for n in range(0,4):
    a1[n]=float(a1[n])
    a2[n]=float(a2[n])
    a3[n]=float(a3[n])



print(a1, a2, a3) 
if a1[0]==0:
    if a2[0]==0:
        if a3[0]!=0:
            swap(a1,a3)
        else:
            print("You may have a zero problem")
            exit
    else:
        swap(a1,a2)     
if a1[0]!=1:
    i=a1[0]
    for n in range(0,len(a1)):
        a1[n]=(a1[n]/i)
print("a1=",a1)
if a2[0]!=0:
    i=a2[0]
    for n in range(0,len(a2)):
        a2[n]=a2[n]-(i*a1[n])
print("a2=",a2)
if a3[0]!=0:
    i=a3[0]
    for n in range(0,len(a3)):
        a3[n]=a3[n]-(i*a1[n])
print("a3=", a3)
if a2[1]==0:
    if a3[1]!=0:
        swap(a2,a3)
    else:
        print("You may have a zero problem")
        exit
if a2[1]!=1:
    i=a2[1]
    for n in range(0,len(a2)):
        a2[n]=(a2[n]/i)
print("a2=",a2)
if a3[1]!=0:
    i=a3[1]
    for n in range(0,len(a3)):
        a3[n]=a3[n]-(i*a2[n])
print("a3=", a3)
if a3[2]==0:
    print();
else:
    if a3[2]!=1:
        i=a3[2]
        for n in range(0,len(a3)):
            a3[n]=(a3[n]/i)
print("a3=",a3)
if a2[2]!=0:
    i=a2[2]
    for n in range(0,len(a2)):
        a2[n]=a2[n]-(i*a3[n])
print("a2=", a2)
if a1[1]!=0:
    i=a1[1]
    for n in range(0,len(a1)):
        a1[n]=a1[n]-(i*a2[n])
print("a1=",a1)
if a1[2]!=0:
    i=a1[2]
    for n in range(0,len(a1)):
        a1[n]=a1[n]-(i*a3[n])
print("a1=",a1)

arr=np.array([a1,a2,a3])
print(arr)





    


