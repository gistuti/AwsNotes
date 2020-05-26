
Day4
1.Write a function to find max of three numbers.


def maximum_number(num1,num2,num3):
    list=[num1,num2,num3]
    return max(list)
print(maximum_number(13,5,9))

2.Write a Python program to detect the number of local variables declared in a function.
def localvariable():
    a = 0
    b = 2.5
    char1='a'
    str1="Hello India"
print(localvariable.__code__.co_nlocals)
3.Write a recursive function to calculate the sum of numbers from 0 to 10
Expected output: 55

def result(x):
    if x<=1:
        return x
    else:
        return x+result(x-1)
print(result(10))

4.Create a function showStudent() in such a way that it should accept student id, name, and it’s college name
and if the id and college name is missing in function call it should show it as by default id is 1 and
college name  is VITA.

def showstudent(student_name,student_id="1",college_name="VITA"):
    print(student_name,"whose",student_id,"from",college_name)

5.	Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [11,22,22,33,33,33,44,55,55,66]
Unique List : [11, 22,33, 44, 55,66]


def sortedlist(mylist1):
    mylist2 = []
    for i in mylist1:
        if i not in mylist2:
            mylist2.append(i)
    return(mylist2)
print(sortedlist([11,22,22,33,33,33,44,55,55,66]))

6.	Write a program to obtain the sum of the first and last digit of this number 2 user defined functions
1st for first digit
2nd for last digit
Example:
 Input:  5424
Output: 9

firstnumber=0
n=int(input())
l=str(n)
q=len(l)
lastdigit=n%10
n=n//10
while(n > 10):
    n = n//10 
firstDigit= n
print(firstDigit+lastdigit)  
   
      

    
