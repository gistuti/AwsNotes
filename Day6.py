
Day-6
1.Python program to Swap Keys and Values in Dictionary.

mydictionary={1:"ABC",2:"DEF",3:"GHI",4:"JKL"}
mydictionary1={value:key for key,value in mydictionary.items()}
print(mydictionary1)

2.Write program to implement Selection sort.

i=0
mylist1=[3,66,11,9,0]
lowest_location=0
while i<len(mylist1):
    lowest_number=min(mylist1[i:])
    lowest_location=mylist1.index(lowest_number)
    mylist1[i],mylist1[lowest_location]=mylist1[lowest_location],mylist1[i]
    i+=1
print(mylist1)

3.Write program to implement Insertion sort.

mylist=[2,1,4,13,6,15]
for i in range(1,len(mylist)):
    x=mylist[i]
    j=i-1
    while mylist[i] < mylist[j]and j >= 0:
        mylist[i] =mylist[j]
        j=j-1
    mylist[j+1] = x

4.Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the
following list.
Given list: list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m",  "n"]
Sub List to be added = ["h", "i", "j"]
Expected output:-
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

mylist1=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
mylist2= ["h","i","j"]
mylist1[2][1][2].extend(mylist2)
print(mylist1)

5.	Access the value of key “history”
sampleDict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
#Expected output: 80
print(sampleDict['class']['student']['marks']['history'])



