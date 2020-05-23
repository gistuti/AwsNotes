'''
Day-2
1.	Python Program to Read a Number n And Print the Series “1+2+…..+n= “
          sample:
          Case 1:
	Enter a number: 4
1 + 2 + 3 + 4 = 10

Case 2:
Enter a number: 5
1 + 2 + 3 + 4 + 5 = 15

n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
    if n!=i:
        print(i,end='+')
    else:
        print(i)
print('=',sum)


2. Write a Python program to count the number of even and odd numbers from                     a series of numbers.
Sample numbers :
 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5

list1=[]
countEven=0
countOdd=0
n=int(input())
for i in range(1,n):
    list1.append(i)
print(list1)
for i in range(1,(len(list1)+1)):
    if i%2==0:
        countEven+=1
    else:
        countOdd+=1
print("Number of even numbers",countEven)
print("Number of Odd numbers",countOdd)

3.Write a Python program to create the multiplication table (from 1 to 10)
of a number.


n=int(input())
for i in range(1,11):
    print(n,'x', i, '=', n*i)


4.Given the triangle of consecutive odd  numbers
		                 
Above triangle is given Calculate Sum row wise 
Example we call function :- row_sum_odd_numbers(2)
Result will be=3 + 5 = 8
if user give 4 then ur output is 13 + 15 + 17+ 19 = 64


def row_sum_odd_number(x):
    return x*x*x

print(row_sum_odd_number(int(input("Enter a number: "))))

     
5.Write python program to print the pattern given below
Note: Take input from user
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5


for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=" ")
    print()

'''

