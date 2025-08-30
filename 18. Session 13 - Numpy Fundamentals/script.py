# Creating Numpy Arrays

## np.array()
import numpy as np

npArray = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", npArray) # Output: [1 2 3 4 5]
print("Type of npArray:", type(npArray)) # Output: <class 'numpy.ndarray'>

##################################################################################

## 2D numpy array
np2DArray = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Numpy Array:\n", np2DArray)
# Output:
# [[1 2 3]
#  [4 5 6]]

##################################################################################

## 3D numpy array
np3DArray = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Numpy Array:\n", np3DArray)
# Output:
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]

##################################################################################

## dtype: Specifying data type of array elements
np.array([1, 2, 3], dtype=float) # Output: array([1., 2., 3.])

np.array([1.5, 2.5, 3.5], dtype=int) # Output: array([1, 2, 3])

np.array([1, 0, 1], dtype=bool) # Output: array([ True, False,  True])

np.array(['1', '2', '3'], dtype=complex) # Output: array([1.+0.j, 2.+0.j, 3.+0.j])

## npm.arange(): Creating arrays with a range of values
np.arange(0, 5) # Output: array([0, 1, 2, 3, 4])
np.arange(1, 10, 2) # Output: array([1, 3, 5, 7, 9])

##################################################################################

## np.arange() with reshape
np.arange(1, 11).reshape(2, 5)
# Output:
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10]])

np.arange(1, 11).reshape(5, 2)
# Output:
# array([[ 1,  2],
#        [ 3,  4],
#        [ 5,  6],
#        [ 7,  8],
#        [ 9, 10]])

##################################################################################

## np.ones() and np.zeros()
np.ones((2, 3)) 
# Output: array([[1., 1., 1.],
#                [1., 1., 1.]])

np.zeros((3, 2)) 
# Output: array([[0., 0.],
#                [0., 0.],
#                [0., 0.]])


##################################################################################

## np.random.rand() and np.random.randint()
np.random.rand(2, 3)
# Output: array([[0.5488135 , 0.71518937, 0.60276338],
#                [0.54488318, 0.4236548 , 0.64589411]])

np.random.randint(1, 10, size=(2, 3))
# Output: array([[3, 7, 2],
#                [4, 6, 8]])

##################################################################################

## np.linspace(): Creating arrays with evenly spaced values
np.linspace(0, 1, 5) # Output: array([0.  , 0.25, 0.5 , 0.75, 1. ])
np.linspace(1, 10, 4) # Output: array([ 1.,  4.,  7., 10.])

##################################################################################

# np.identity(): Creating identity matrices
np.identity(3)
# Output: array([[1., 0., 0.],
#                [0., 1., 0.],
#                [0., 0., 1.]])

# Note: default dtype is float

##################################################################################

## Array Attributes
a1 = np.arange(10) # 1D array
a2 = np.arange(12, dtype=float).reshape(3, 4) # 2D array
a3 = np.arange(8).reshape(2, 2, 2) # It is also called as Tensor

print("Array a1:", a1) # Output: [0 1 2 3 4 5 6 7 8 9]
print("Array a2:\n", a2)
# Output:
# [[ 0.  1.  2.  3.]
#  [ 4.  5.  6.  7.]
#  [ 8.  9. 10. 11.]]
print("Array a3:\n", a3)
# Output:
# [[[0 1]
#   [2 3]]
#  [[4 5]
#   [6 7]]]


## ndim: Number of dimensions
print("Dimensions of a1:", a1.ndim) # Output: 1
print("Dimensions of a2:", a2.ndim) # Output: 2
print("Dimensions of a3:", a3.ndim) # Output: 3


##################################################################################

## shape: Shape of the array
print("Shape of a1:", a1.shape) # Output: (10,)
print("Shape of a2:", a2.shape) # Output: (3, 4)
print("Shape of a3:", a3.shape) # Output: (2, 2, 2)

##################################################################################

## size: Total number of elements in the array
print("Size of a1:", a1.size) # Output: 10
print("Size of a2:", a2.size) # Output: 12
print("Size of a3:", a3.size) # Output: 8

##################################################################################

## itemsize: Size (in bytes) of each element in the array
print("Item size of a1:", a1.itemsize) # Output: 4 (for int32)
print("Item size of a2:", a2.itemsize) # Output: 8 (for float64)
print("Item size of a3:", a3.itemsize) # Output: 4 (for int32)

##################################################################################

## dtype: Data type of the array elements
print("Data type of a1:", a1.dtype) # Output: int32
print("Data type of a2:", a2.dtype) # Output: float64
print("Data type of a3:", a3.dtype) # Output: int32

##################################################################################

### Changing Data Types

## astype(): Convert array to a different data type
a1_float = a1.astype(float)
print("a1 as float:", a1_float) # Output: [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
print("Data type of a1_float:", a1_float.dtype) # Output: float64

a2_int = a2.astype(int)
print("a2 as int:\n", a2_int)
# Output:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print("Data type of a2_int:", a2_int.dtype) # Output: int32

a3_float = a3.astype(float)
print("a3 as float:\n", a3_float)
# Output:
# [[[0. 1.]
#   [2. 3.]]
#  [[4. 5.]
#   [6. 7.]]]
print("Data type of a3_float:", a3_float.dtype) # Output: float64

##################################################################################

## Array Operations

arr1 = np.arange(12).reshape(3,4)
arr2 = np.arange(12, 24).reshape(3,4)

### Scalar Operations
# 1. Arithmetic Operations
# 2. Relational Operations

### 1. Arithmetic Operations
arr1 * 2 ## +, -, /, //, **, %
# Output:
# array([[ 0,  2,  4,  6],
#        [ 8, 10, 12, 14],
#        [16, 18, 20, 22]])

##################################################################################

### 2. Relational Operations
arr1 > 5 ## <, <=, >=, ==, !=
# Output:
# array([[False, False, False, False],
#        [ True,  True,  True,  True],
#        [ True,  True,  True,  True]])


##################################################################################

### Vector Operations

# 1. Arithmetic Operations

arr1 + arr2 ## +, -, /, //, **, %
# Output:
# array([[12, 14, 16, 18],
#        [20, 22, 24, 26],
#        [28, 30, 32, 34]])

# 2. Relational Operations

##################################################################################

## Numpy Array Functions

arr1 = np.random.randint((3,3))
arr1 = np.round(arr1 * 100)

print("Array arr1:\n", arr1)
# Example Output:
# [[12 45 78]
#  [34 56 23]
#  [89 67 98]]

### max() - maximum value
print("Max of arr1:", arr1.max()) # Output: Max of arr1: 98

### min() - minimum value
print("Min of arr1:", arr1.min()) # Output: Min of arr1: 12

### sum() - addition of all elements
print("Sum of arr1:", arr1.sum()) # Output: Sum of arr1: 498

### prod() - multiplication of all elements
print("Product of arr1:", arr1.prod()) # Output: Product of arr1: 12345678901234567890 (example value)

### Find the minimum value of each row
print("Min of each row in arr1:", arr1.min(axis=1)) # Output: Min of each row in arr1: [12 23 67]

### Find the maximum value of each column
print("Max of each column in arr1:", arr1.max(axis=0)) # Output: Max of each column in arr1: [89 67 98]

### mean() - average of all elements
print("Mean of arr1:", arr1.mean()) # Output: Mean of arr1: 55.333333333333336

### median() - median of all elements
print("Median of arr1:", np.median(arr1)) # Output: Median of arr1: 56.0

### std() - standard deviation of all elements
print("Standard Deviation of arr1:", arr1.std()) # Output: Standard Deviation of arr1: 28.345678901234567

### var() - variance of all elements
print("Variance of arr1:", arr1.var()) # Output: Variance of arr1: 567.5555555555555

##################################################################################

### trigonometric functions
angles = np.array([0, 30, 45, 60, 90], dtype=float) # Convert degrees to radians
print("Sine of angles:", np.sin(angles)) # Output: Sine of angles: [ 0.          0.49999999  0.70710678  0.8660254   1.        ]
print("Cosine of angles:", np.cos(angles)) # Output: Cosine of angles: [ 1.          0.8660254   0.70710678  0.49999999  0.        ]
print("Tangent of angles:", np.tan(angles)) # Output: Tangent of angles: [ 0.          0.57735027  1.          1.73205081        inf]

### dot() - dot product of two arrays

arr3 = np.arange(12).reshape(3, 4)
arr4 = np.arange(12, 24).reshape(4, 3)

print("Dot product of arr3 and arr4:\n", np.dot(arr3, arr4))
# Output:
# [[  56  62  68]
#  [ 152 174 196]
#  [ 248 286 324]]

### log() - natural logarithm of each element
arr5 = np.random.randint((3,3))
print("Array arr5:\n", arr5)
# Example Output:
# [[12 45 78]
#  [34 56 23]
#  [89 67 98]]
print("Natural Log of arr5:\n", np.log(arr5))
# Output:
# [[2.48490665 3.80666249 4.35670883]
#  [3.52636126 4.02535169 3.13549421]
#  [4.48863637 4.20469262 4.58496748]]


### exp() - exponential of each element
print("Exponential of arr5:\n", np.exp(arr5))
# Output:
# [[1.62754791e+05 3.49342711e+19 1.13031883e+34]
#  [5.83461743e+14 2.09101525e+24 9.74480345e+09]


### round() - round each element to the nearest integer
arr6 = np.random.rand(2, 3) * 100
print("Array arr6:\n", arr6)
# Example Output:
# [[12.3456789  45.67891234 78.91234567]
#  [34.56789123 56.78912345 23.45678912]]
print("Rounded arr6:\n", np.round(arr6))
# Output:
# [[12. 46. 79.]
#  [35. 57. 23.]]

### floor() - floor value of each element
print("Floor of arr6:\n", np.floor(arr6))
# Output:
# [[12. 45. 78.]
#  [34. 56. 23.]]

### ceil() - ceiling value of each element
print("Ceil of arr6:\n", np.ceil(arr6))
# Output:
# [[13. 46. 79.]
#  [35. 57. 24.]]


##################################################################################

### indexing
arr1 = np.arange(10)
arr2 = np.arange(12).reshape(3, 4)
arr3 = np.arange(8).reshape(2, 2, 2)

# 1D array indexing and slicing
print("Element at index 3 in arr1:", arr1[3]) # Output: Element at index 3 in arr1: 3
print("Elements from index 2 to 5 in arr1:", arr1[2:6]) # Output: Elements from index 2 to 5 in arr1: [2 3 4 5]

# 2D array indexing and slicing
print("Element at row 1, column 2 in arr2:", arr2[1, 2]) # Output: Element at row 1, column 2 in arr2: 6
print("Elements in row 0 of arr2:", arr2[0, :]) # Output: Elements in row 0 of arr2: [0 1 2 3]
print("Elements in column 1 of arr2:", arr2[:, 1]) # Output: Elements in column 1 of arr2: [1 5 9]


# 3D array indexing and slicing
print("Element at depth 1, row 0, column 1 in arr3:", arr3[1, 0, 1]) # Output: Element at depth 1, row 0, column 1 in arr3: 5
print("Elements in depth 0 of arr3:\n", arr3[0, :, :])
# Output:
# Elements in depth 0 of arr3:
# [[0 1]
#  [2 3]]

##################################################################################

# Iterating - Looping through array elements

## Iterating over 1D array
arr = np.arange(6).reshape(2, 3)
print("Array arr:\n", arr)
# Output:
# [[0 1 2]
#  [3 4 5]]

for element in arr:
    print(element)
# Output:
# [0 1 2]
# [3 4 5]

## Iterating over 2D array
arr = np.arange(12).reshape(3, 4)
print("Array arr:\n", arr)
# Output:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

for row in arr:
    for element in row:
        print(element, end=' ')
    print()
# Output:
# 0 1 2 3
# 4 5 6 7
# 8 9 10 11

## Iterating over 3D array
arr = np.arange(8).reshape(2, 2, 2)
print("Array arr:\n", arr)
# Output:
# [[[0 1]
#   [2 3]]
#  [[4 5]
#   [6 7]]]

for matrix in arr:
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()
    print()
# Output:
# 0 1
# 2 3
#
# 4 5
# 6 7


## Using nditer for multi-dimensional arrays
arr = np.arange(12).reshape(3, 4)
print("Array arr:\n", arr)
# Output:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

for element in np.nditer(arr):
    print(element, end=' ')
# Output:
# 0 1 2 3 4 5 6 7 8 9 10 11

##################################################################################

# Reshaping - Changing the shape of an array

## reshape(): Change the shape of an array without changing its data
arr = np.arange(1, 11).reshape(2, 5)
# Output:
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10]])

## transpose(): Transpose the dimensions of an array
arr = np.arange(12).reshape(3, 4)
# Output:
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
np.transpose(arr)
# Output:
# array([[ 0,  4,  8],
#        [ 1,  5,  9],
#        [ 2,  6, 10],
#        [ 3,  7, 11]])

## ravel(): Flatten a multi-dimensional array into a 1D array
arr = np.arange(12).reshape(3, 4)
# Output:
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
arr.ravel()
# Output: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])


##################################################################################

# Stacking - Combining multiple arrays into one

## Horizontal Stacking
arr4 = np.arange(12).reshape(3, 4)
arr5 = np.arange(12, 24).reshape(3, 4)

print("Array arr4:\n", arr4)
# Output:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print("Array arr5:\n", arr5)
# Output:
# [[12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]

np.hstack((arr4, arr5))
# Output:
# array([[ 0,  1,  2,  3, 12, 13, 14, 15],
#        [ 4,  5,  6,  7, 16, 17, 18, 19],
#        [ 8,  9, 10, 11, 20, 21, 22, 23]])

## Vertical Stacking
arr4 = np.arange(12).reshape(3, 4)
arr5 = np.arange(12, 24).reshape(3, 4)
np.vstack((arr4, arr5))
# Output:
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11],
#        [12, 13, 14, 15],
#        [16, 17, 18, 19],
#        [20, 21, 22, 23]])