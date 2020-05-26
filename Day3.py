DAY-3
1.	You are given with a list of integer elements.
Make a new list which will store square of elements of previous list.

import numpy as np
mylist1=[2,4,6,8,9]
mylist2=np.square(mylist1)
print(mylist2)

2.  From a list containing ints, strings and floats,
make three lists to store them separately. 

mylist1=['c','HEllo India',100,679.45,71]
l1_int=[]
l2_str=[]
l3_flo=[]
for i in mylist1:
    if type(i)==int:
        l1_int.append(i)
    if type(i)==str:
        l2_str.append(i)
    if type(i)==float:
        l3_flo.append(i)
print(l1_int)
print(l2_str)
print(l3_flo)
        
    3.	Print the pattern
1
1 2 
1 2 3
1 2 3 4
1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

4.Accept data in two 3*3  matrix and calculate the sum of
the matrices.

import numpy as np
mylist=[]
mylist2=[]
l1=[]
l2=[]


n=int(input("enter the number of elements n:",))
m=int(input("enter the number of elements m:",))
for i in range(1,n+1):
    mylist.append(i)
print(mylist)
l1=np.reshape(mylist,(3,3))
print("l1---->",l1)
for j in range(1,m+1,2):
    mylist2.append(j)
l2=np.reshape(mylist2,(3,3))
print("l2---->",l2)

result = [[l1[i][j] + l2[i][j] for j in range(len(l1[0]))] for i in range(len(l1))]
print("result",result)

5.	Write a Python program to check whether a given number is a narcissistic number or not
For example, 371 is a narcissistic number; it has three digits, and if we cube each digits  33 + 73 + 13 the sum is 371. Other 3-digit narcissistic numbers are
153 = 13 + 53 + 33
370 = 33 + 73 + 03
407 = 43 + 03 + 73.
There are also 4-digit narcissistic numbers, some of which are 1634, 8208, 9474 since
1634 = 14+64+34+44
8208 = 84+24+04+84
9474 = 94+44+74+44


n=int(input())
q=n
l=str(n)
t=1
result=0
print(len(l))
for i in range(1,(len(l)+1)):
    t=n%10
    n=n//10
    k=t**len(l)
    result+=k
print(result)
if result == q:
    print("no. is narcissistic")
else:
    print("no. is not narcissistic")

