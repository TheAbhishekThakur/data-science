# Important Numpy functions

## 1. np.sort
# Return a sorted copy of an array.

import numpy as np

## 1D array sort
a = np.random.randint(1,100,15)
sorted_arr = np.sort(a)
print(sorted_arr)

## 2D array sort - row wise sorting
b = np.random.randint(1,100,24).reshape(6,4)
sorted_arr = np.sort(b)
print(sorted_arr)

## 2D array sort - column wise sorting
b = np.random.randint(1,100,24).reshape(6,4)
sorted_arr = np.sort(b, axis=0)
print(sorted_arr)

## 2D array sort - column wise sorting with desending order
b = np.random.randint(1,100,24).reshape(6,4)
sorted_arr = np.sort(b, axis=0)[::-1]
print(sorted_arr)

############################################################################

## 2. np.append
# The numpy.append() appends values along the mentioned axis at the end of the array.

## 1D array append
a = np.random.randint(1,100,15)
np.append(a, 200)
print(a)

## 2D array append
b = np.random.randint(1,100,24).reshape(6,4)
np.append(b, np.ones(b.shape[0], 1), axis=1)
print(b)

############################################################################

## 3. np.concatenate
# The numpy.concatenate() function concatenate a sequence of arrays along an existing axis.

c = np.arange(6).reshape(2, 3)
d = np.arange(6, 12).reshape(2, 3)

print(np.concatenate((c,d), axis=0)) # row wise concatenate
print(np.concatenate((c,d), axis=1)) # column wise concatenate

############################################################################

## 4. numpy.unique
# With the help of np.unique() method, we can get the unique values from an array given as parameter in np.unique() method.

e = np.array([1,1,2,2,3,3,4,4,5,5,6,6])
print(np.unique(e)) # array([1,2,3,4,5,6])

############################################################################

## 5. numpy.expand_dims
# With the help of np.expand_dims() method, we can get the expended dimensions of an array.
# You can expand 1D array to 2D, 2D array to 3D, 3D array to 4D and so on.
a = np.random.randint(1,100,15)
np.expand_dims(a, axis=0)
np.expand_dims(a, axis=1)


############################################################################

## 6. numpy.where
# The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.
a = np.random.randint(1,100,15)

## find all the indices (index position) with value greater than 50
print(np.where(a > 50)) # [1,6,7,10,20]

## replace all values > 50 with 0
np.where(a > 50, 0, a) # [11, 0, 28, 50, 38, 37, 0, 0, 5, 30, 0, 9, 0, 2, 21]

############################################################################

## 7. numpy.argmax
# The numpy.argmax() function returns the indices of the max element of the array in a particular axis.

## 1D
a = np.random.randint(1,100,15)
print(np.argmax(a)) # 6

# 2D
b = np.random.randint(1,100,24).reshape(6,4)
print(np.argsmax(b, axis=0)) # column wise 
print(np.argsmax(b, axis=1)) # row wise

############################################################################

## 8. numpy.argmin
# The numpy.argmin() function returns the indices of the min element of the array in a particular axis.

## 1D
a = np.random.randint(1,100,15)
print(np.argmin(a)) # 13

# 2D
b = np.random.randint(1,100,24).reshape(6,4)
print(np.argmin(b, axis=0)) # column wise 
print(np.argmin(b, axis=1)) # row wise

############################################################################

## 9. numpy.cumsum
# The numpy.cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis.

## 1D
a = np.random.randint(1,100,15)
print(np.cumsum(a)) # [11, 64, 92, 142, 180, 217, 311, 403, 408, 438, 506, 515, 593, 595, 616]

## 2D
b = np.random.randint(1,100,24).reshape(6,4)
print(np.cumsum(b)) # converted into 1D aaray then apply cumulative sum 
print(np.cumsum(b, axis=0)) # column wise 
print(np.cumsum(b, axis=1)) # row wise

############################################################################

## 10. numpy.cumprod
# The numpy.cumprod() function is used when we want to compute the cumulative multiply of array elements over a given axis.


## 1D
a = np.random.randint(1,100,15)
print(np.cumprod(a)) # 

## 2D
b = np.random.randint(1,100,24).reshape(6,4)
print(np.cumprod(b)) # converted into 1D aaray then apply cumulative multiply 
print(np.cumprod(b, axis=0)) # column wise 
print(np.cumprod(b, axis=1)) # row wise

############################################################################

## 11. numpy.percentile
# The numpy.percentile() function is used to compute the nth percentile of the given data (array element) along the specified axis.
a = np.random.randint(1,100,15)

print(np.percentile(a, 100)) ## 94 - return 100 percentile
print(np.percentile(a, 0)) ## 2 - return 0 percentile
print(np.percentile(a, 50)) ## 37 - return 50 percentile

############################################################################

## 12. numpy.histogram
# Numpy has a built-in numpy.histogram() function which represents the frequency of data distribution in the graphical form.
a = np.random.randint(1,100,15)

np.histogram(a, bins=[0,10,20,30,40,50,60,70,80,90,100])
## Output:
## [3, 1, 2, 3, 0, 2, 1, 1, 0, 2]

############################################################################

## 13. numpy.corrcoef
# Return Pearson product-moment correlation coefficients.

salary = np.array([20000, 40000, 25000, 35000, 60000])
experience = np.array([1,3,2,4,2])

print(np.corrcoef(salary, experience))

############################################################################

## 14. numpy.isin
# With the help of numpy.isin(), we can see that one array having values are checked in a different numpy array having different elements with different sizes.

a = np.random.randint(1,100,15)

items = [10,20,30,40,50,60,70,80,90,100]
print(np.isin(a, items))
## Output : array([False, False, False, True, False, False, False, False, True, False, False, False, False, False])

############################################################################

## 15. numpy.flip
# The numpy.flip() function reverses the order of array elements along the specified axis, preserving the shape of the array.

## 1D
a = np.random.randint(1,100,15)
print(np.flip(a)) # array([21, 2, 78, 9, 68, 30, 5, 92, 94, 37, 38, 50, 28, 53, 11])

## 2D
b = np.random.randint(1,100,24).reshape(6,4)
print(np.flip(b)) 
print(np.flip(b, axis=0)) # column wise
print(np.flip(b, axis=1)) # row wise

############################################################################

## 16. numpy.put
# The numpy.put() function replaces specific elements of an array with given values of p_array.
# Array indexed works on flattened array.

a = np.random.randint(1,100,15)
print(a) #
print(np.put(a, [0, 1], [110, 530]))

############################################################################

## 17. numpy.delete
# The numpy.delete() function returns a new array with the deletion of sub-arrays along with the mentioned axis.

a = np.random.randint(1,100,15)
np.delete(a, 0) # delete 0 index item

np.delete(a, [0, 3, 4]) # delete multiple index items

############################################################################

## 18. Set functions
m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])

## 1. np.union1d
print(np.union1d(m,n)) # array([1,2,3,4,5,6,7])

## 2. np.intersect1d
print(np.intersect1d(m,n)) # array([3,4,5])

## 3. np.setdiff1d
print(np.setdiff1d(m,n)) # array([1,2])
print(np.setdiff1d(n,m)) # array([6,7])

## 4. np.setxor1d
print(np.setxor1d(m,n)) # array([1, 2, 6, 7])

## 5. np.in1d
print(np.in1d(m,1)) # array([True, False, False, False, False])

############################################################################

## 19. numpy.clip
# The numpy.clip() function is used to Clip (limit) the values in an array.

a = np.random.randint(1,100,15)
print(np.clip(a_min=25, a_max=75))
## Output: array([75, 75, 28, 50, 38, 37, 75, 75, 25, 30, 68, 25, 75, 25, 25])