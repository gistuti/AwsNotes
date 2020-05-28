
Day-5
1.Write a Python program to sort a list of elements usingthe bubble sort                                
Algorithm.
def bubble_sort(l1):
    for i in range(len(l1)-1,0,-1):
        for j in range(0,i):
            if l1[j]>l1[j+1]:
                t=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=t
    
l1=[44,23,15,98,74,12]

2.Write a Python program for sequential search (Linear search).
def linear_search(list1,num):
    i=0
    num_is_present=False
    for i in range(len(list1)):
        if not num_is_present:
            if list1[i]==num:
                num_is_present=True
            else:
                i+=1
    return num_is_present,i

3.Write a Python program for Binary search.

def binary_search(list1,num):
    start = 0
    end = len(list1)-1
    present=False
    while (start<=end and not present):
        middle= start+end//2
        if list1[middle] == num:
            present = True
        else:
            if num < list1[middle]:
                end = middle-1
            else:
                start = middle+1
    return present

4.Write a python program to concatenate two lists index-wise.
List1 = [“M”,”na”,”i”,”lak”]
List2 = [“y”,”me”,”s”,”han”]
Expected output:
[“My”,”name”,”is”,”lakhan”]

import numpy as np
def con_list(list1,list2):
    list3= np.char.add(list1, list2)
    return list3

5.Iterate a given list and check if a given element already exists in a dictionary as a key’s value if not delete it from the list.
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {“John”:47,”Peter”:64,”Mahi”:37,”Maria”:76}

sampledict ={"John":47,"Peter":64,"Mahi":37,"Maria":76}
rollnumber =[47,64,69,37,76,83,95,97]
for i in rollnumber:
    if i not in list(sampledict.values()):
        rollnumber.remove(i)
print(rollnumber)


