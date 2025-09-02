# Advanced Numpy

## Numpy array vs Python list
import numpy as np
import time

### speed of list
a = [i for i in range(10000000)]
b = [i for i in range(10000000, 20000000)]

c = []

start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])

print("Time taken by Python list: ", time.time() - start) # 3.266 seconds

### speed of numpy array
a = np.arange(10000000)
b = np.arange(10000000, 20000000)

start = time.time()
c = a + b
print("Time taken by Numpy array: ", time.time() - start) # 0.057 seconds


#####################################################################################

### memory consumption of list
import sys
a = [i for i in range(1000000)]
print("Memory consumed by Python list: ", sys.getsizeof(a)) # 8697456 bytes

### memory consumption of numpy array
a = np.arange(1000000)
print("Memory consumed by Numpy array: ", a.nbytes) # 8000000 bytes

### Reduce using dtype
a = np.arange(1000000, dtype=np.int16)
print("Memory consumed by Numpy array with int16: ", a.nbytes) # 2000000 bytes


#####################################################################################

## convenience 
a = [i for i in range(10000000)]
b = [i for i in range(10000000, 20000000)]

### using list
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])

### using numpy
a = np.arange(10000000)
b = np.arange(10000000, 20000000)
c = a + b

#####################################################################################

# Advanced Indexing

## Normal Indexing & Slicing
a = np.arange(12).reshape(4, 3)
print(a)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

# Indexing
print(a[1,2]) # 5

# Slicing
print(a[1:3, 1:3])
# [[4 5]
#  [7 8]]

#####################################################################################

## Fancy Indexing
a = np.arange(12).reshape(4, 3)
print(a)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

print(a[[0,2,3]]) 

# Output:
# [[ 0  1  2]
#  [ 6  7  8]
#  [ 9 10 11]]

print(a[:,[0,2]])
# Output:
# [[ 0  2]
#  [ 3  5]
#  [ 6  8]
#  [ 9 11]]

#####################################################################################

## Boolean Indexing
import numpy as np

a = np.random.randint(1, 100, 24).reshape(6, 4)
print(a)
# Example Output:
# [[34 67 23 89]
#  [12 45 78 56]
#  [90 11 22 33]
#  [44 55 66 77]
#  [88 99 10 20]
#  [21 31 41 51]]

## find all numbers greater than 50
print(a > 50)
# Example Output:
# [[False  True False  True]
#  [False False  True  True]
#  [ True False False False]
#  [False  True  True  True]
#  [ True  True False False]
#  [False False False  True]]
print(a[a > 50])
# Example Output:
# [67 89 78 56 90 55 66 77 88 99 51]

## find all even numbers
print(a[a % 2 == 0])
# Example Output:
# [34 12 78 56 90 22 44 66 88 10 20]

## find all numbers greater than 50 and even
print(a[(a > 50) & (a % 2 == 0)])
# Example Output:
# [56 90 66 88]

## find all numbers not divisible by 7
print(a[a % 7 != 0])
# Example Output:
# [34 67 23 89 12 45 78 56 11 22 33 44 55 88 99 10 20 21 31 41 51]


#####################################################################################

## Broadcasting - Performing operations on arrays of different shapes

### same shape
a = np.arange(6).reshape(2, 3)
b = np.arange(6, 12).reshape(2, 3)
print(a) # [[0 1 2]
         #  [3 4 5]]
print(b) # [[ 6  7  8]
         #  [ 9 10 11]]

print(a + b) # [[ 6  8 10]
             #  [12 14 16]]

### different shape
a = np.arange(6).reshape(2, 3)
b = np.arange(3).reshape(1, 3)
print(a) # [[0 1 2]
         #  [3 4 5]]
print(b) # [[0 1 2]]

print(a + b) # [[0 2 4]
             #  [3 5 7]]


### More Examples
a = np.arange(12).reshape(3,4)
b = np.arange(3)

# print(a + b) # ValueError: operands could not be broadcast together with shapes (3,4) (3,)

## Example 2:
a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(3,1)

print(a + b)
# Output:
# [[0,1,2]]
# [[0]
# [1]
# [2]]
# [[0,1,2]
# [1,2,3]
# [2,3,4]]

#####################################################################################

# Working with mathematical formulas

## sum of all the numpy array elements
a = np.arange(10)
np.sum(a) # 45

## sigmoid
def sigmoid(array):
    return 1 / (1 + np.exp(-(array)))

a = np.arange(10)
print(sigmoid(a))

# Output:
# array([0.5       , 0.73105858, 0.88079708, 0.95257413, 0.98201379,
# 0.99330715, 0.99752738, 0.99908895, 0.99966465, 0.99987661,
# 0.9999546, 0.9999833, 0.99999386, 0.99999774, 0.99999917, 
# 0.99999969, 0.99999989, 0.99999996, 0. 99999998, 0.99999999])


## mean squared error
actual = np.random.randint(1, 10, 5)
predicted = np.random.randint(1, 10, 5)

def mse(actual, predicted):
    return np.mean((actual - predicted) ** 2)

print(mse(actual, predicted))
# Output: 8.6

## categorical cross entropy
print(np.mean((actual - predicted) ** 2))
# Output: 12.6

#####################################################################################

# Working with missing values -> np.nan

a = np.array([1,2,3,4, np.nan, 6])
print(a) # array([1,2,3,4,nan,6])

## To remove missing value
b = np.isnan(a)
print(a[~b]) # [1. 2. 3. 4. 6.]


#####################################################################################

# Plotting Graph
import matplotlib.pyplot as plt

## x = y
x = np.linspace(-10, 10, 100)
print(x) # Genearte 100 numbers between -10 to 10 
y = x
plt.plot(x,y)

## y = x^2
x = np.linspace(-10, 10, 100)
y = x**2
plt.plot(x, y)

## y = sin(x)
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y)

## y = xlog(x)
x = np.linspace(-10, 10, 100)
y = x * np.log(x)
plt.plot(x, y)

## sigmoid
x = np.linspace(-10, 10, 100)
y = 1 / (1 + np.exp(-x))
plt.plot(x, y)