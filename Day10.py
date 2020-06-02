DAY-10
1.Write a NumPy program to get the numpy version and show numpy build configuration.
import numpy as np
print(np.__version__)
print(np.show_config())
2.Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not.

import numpy as np
l=np.array([2,5,2+7j,1-1j,7j,0])
print(np.iscomplex(l))
print(np.isreal(l))
n=3.2
print(np.isscalar(n))
3.Write a NumPy program to test whether none of the elements of a given array is zero.

import numpy as np
l=np.array([2,5,7,1,9,8])
print(np.all(l))

4.Write a NumPy program to test whether any of the elements of a given array is non-zero.

import numpy as np
l=np.array([2,3,1,5,6,2,7])
print(np.any(l))

5.Write a NumPy program to test element-wise for NaN(not a number) of a given array.

import numpy as np
l=np.array([2,1,0,'a'])
print(np.isnan(l))

6.Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arr

import numpy as np
l1=np.array([2,7,3,5,1,9])
l2=np.array([2,9,1,6,4,10])
print("greater",np.greater(l1,l2))
print("greater_equal",np.greater_equal(l1,l2))
print("less",np.less(l1,l2))
print("less_equal",np.less_equal(l1,l2))

7.Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
Input:

import numpy as np
x =np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y =np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print("equal",np.equal(x,y))
print("equal_within_range",np.allclose(x,y))

8.Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.
import numpy as np
l=np.array([1,7,13,105])
print(l)
print("%d bytes" % (l.size *l.itemsize))
9.Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.

import numpy as np
l=np.zeros(10)
print(l)
l1=np.ones(10)
print(l1)
l2=np.ones(10)*5
print(l2)
10.Write a NumPy program to create an array of the integers from 30 to 70.

import numpy as np
l=np.arange(30,71)
print(l)

11.Write a NumPy program to create an array of all the even integers from 30 to 70.

import numpy as np
l=np.arange(30,70,2)
print(l)

12.Write a NumPy program to create a 3x3 identity matrix.

import numpy as np
l=np.identity(3)
print(l)

13.Write a NumPy program to generate a random number between 0 and 1.
import numpy as np
ran_number=np.random.normal(0,1)
print(ran_number)

14.Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.

import numpy as np
ran_number= np.random.normal(0,1,15)
print(ran_number)

15.Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.

import numpy as np
l=np.arange(15,56)
print(l)
x=l[(l>15) &(l<55)]
print(x)
