import numpy as np 

i1=(input("enter the first row"))

i2=(input("Enter the second row"))

i3=(input ("Enter the third row"))

i4=input("Enter answer row")



a1=i1.split(",")
a2=i2.split(",")
a3=i3.split(",")
ans=i4.split(",")

for n in range(0,3):
    a1[n]=float(a1[n])
    a2[n]=float(a2[n])
    a3[n]=float(a3[n])
    ans[n]=float(ans[n])
if ans[0]==0:
    if ans[1]==0:
        if ans[2]!=0:
            a4=a1
            a1=a3
            a3=a4
            ans[0]=ans[2]
            ans[2]=0
        else:
            print("You may encounter a zero problem")
    else:
        a4=a1
        a1=a2
        a2=a4
        ans[0]=ans[1]
        ans[1]=0


print(a1, a2, a3)



arr=np.array([(a1),(a2),(a3)])

arr1=np.array(arr)
arr2=np.array(arr)
arr3=np.array(arr)

print(arr)

det=np.linalg.det(arr)

print(det)

for n in range(0,5):
    arr1[n][0]=ans[n]
    arr2[n][1]=ans[n]
    arr3[n][2]=ans[n]

print(arr1)
print("")
print(arr2) 
print("")
print(arr3)

d1=np.linalg.det(arr1)
d2=np.linalg.det(arr2)
d3=np.linalg.det(arr3)
print(d1,d2,d3)

solutions=np.array([d1/det,d2/det,d3/det])
print("Solution=",solutions)