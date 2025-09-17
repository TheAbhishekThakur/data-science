import numpy as np
import pandas as pd

## Series from lists

### string
country = ["India", "Pakistan", "USA", "Nepal", "Srilanka"]
pd.Series(country)
## Output:
# 0 India
# 1 Pakistan
# 2 USA
# 3 Nepal
# 4 Srilanka
# dtype: object (string) 

### integers
runs = [50, 54, 23, 48]
pd.Series(runs)
## Output:
# 0 50
# 1 54
# 2 23
# 3 48
# dtype: int

### custom index
marks = [67, 57, 89, 100]
subjects = ["maths", "english", "science", "hindi"]

pd.Series(marks, index=subjects)
## Output:
# maths 67
# english 57
# science 89
# hindi 100
# dtype: int64

### setting a name
marks = [67, 57, 89, 100]
subjects = ["maths", "english", "science", "hindi"]

pd.Series(marks, index=subjects, name="Abhishek's marks")
## Output:
# maths 67
# english 57
# science 89
# hindi 100
# Name: Abhishek's marks, dtype: int64

#################################################################################

## Series from dict
marks = {
    "math": 67,
    "english": 57,
    "science": 89,
    "hindi": 100
}

marks_series = pd.Series(marks)
marks_series_name = pd.Series(marks, name="Abhishek's marks")
print(marks_series)
## Output:
# maths 67
# english 57
# science 89
# hindi 100
# dtype: int64

#################################################################################

## Series Attributes
marks = {
    "math": 67,
    "english": 57,
    "science": 89,
    "hindi": 100
}

marks_series = pd.Series(marks, name="marks series")

# size - find number of items of series
print(marks_series.size) # 4

# dtype - return datatype
print(marks_series.dtype) # int64

# name - return the series name
print(marks_series.name) # marks series

# is_unique - check all items are unique or not
print(marks_series.is_unique) # True

# index - return all index of series
print(marks_series.index) # Index(['maths', 'english', 'science', 'hindi'])

# values
print(marks_series.values) # array([67, 57, 89, 100])

#################################################################################

# Series using read_csv

## with one column
data = pd.read_csv('./subs.csv')
print(type(data)) # pandas.core.frame.DataFrame

data = pd.read_csv('./subs.csv', squeeze=True)
print(type(data)) # pandas.core.frame.Series
print(data)
## Output: Print whole series data with name, length, and data type
# 0     48
# 1     57
# 2     40
# .......
# Name: Subscribers gained, Length: 365, dtype: int64


## with two column
data = pd.read_csv('./kohli_ipl.csv', index_col="match_no", squeeze=True)
## Output: Print whole series data with name, length, and data type
# match_no
# 1     1
# 2     23
# 3     13
# .......
# Name: runs, Length: 215, dtype: int64


data = pd.read_csv('./bollywood.csv', index_col="movie", squeeze=True)
print(data)
## Output: Print whole series data with name, length, and data type
# movie
# Uri: The Surgical Strike      Vicky Kaushal     1
# Battalion 609                 Vicky Ahuja
# .......
# Name: lead, Length: 1500, dtype: object


#################################################################################

# Series methods

## 1. head and tail
data = pd.read_csv('./subs.csv', squeeze=True)
print(data.head())
## Output: Return top 5 rows
# 0     48
# 1     57
# 2     40
# 3     43
# 4     44
# Name: Subscribers gained, dtype: int64

print(data.head(3)) # Return 3 rows

print(data.tail()) # Return last 5 rows
print(data.tail(3)) # Return last 3 rows



## 2. sample: Return randomally 1 row
print(data.sample())
print(data.sample(3)) # Return random 3 row


## 3. value_counts: Return frequency of data
data = pd.read_csv('./subs.csv', squeeze=True)
print(data.value_counts())
# Output:
# Akshay Kumar       48
# Amitabh Bachchan   45
# Ajay Devgn         38
# ....
# ....
# Name: lead, length: 566, dtype: int64


## 4. sort_values: inplace
data = pd.read_csv('./kohli_ipl.csv', squeeze=True)
print(data.sort_values())
# Output:
# match_no
# 87      0
# 211     0
# 207     0
# ....
# 164     100
# 120     100
# ....
# Name: runs, length: 215, dtype: int64

print(data.sort_values(ascending=False)) # Return descending order values
print(data.sort_values(ascending=False).head(1).values[0]) # 113 - Highest score of virat kohli
print(data.sort_values(inplace=True)) # Change orginal array values


## 5. sort_index: inplace 
data = pd.read_csv('./kohli_ipl.csv', squeeze=True)
print(data.sort_index()) # Sorted by alphabetacally
print(data.sort_index(inplace=True)) # Sorted by alphabetacally -> Changed in orignal array values


#################################################################################

# Series Math Methods

## 1. count
data = pd.read_csv('./kohli_ipl.csv', squeeze=True)
print(data.count()) # 215 (Return only non missing values)

## 2. sum
data = pd.read_csv('./subs.csv', squeeze=True)
print(data.sum()) # 49510 (sum of numbers)

## 3. product
data = pd.read_csv('./subs.csv', squeeze=True)
print(data.product()) # 0 (multiply all nums)

## 4. mean
data = pd.read_csv('./subs.csv', squeeze=True)
print(data.mean()) # 135.64383561643837

## 5. median
data = pd.read_csv('./subs.csv', squeeze=True)
print(data.median()) # 24.0

## 6. mode
data = pd.read_csv('./bollywood.csv', squeeze=True)
print(data.mode()) # Akshay Kumar

## 7. std
data = pd.read_csv('./subs.csv', squeeze=True)
print(data.std()) # 62.6750230372527

## 8. var
data = pd.read_csv('./kohli_ipl.csv', squeeze=True)
print(data.var()) # 688.0024777222343

## 9. min
data = pd.read_csv('./subs.csv', squeeze=True)
print(data.min()) # 33

## 10. max
data = pd.read_csv('./subs.csv', squeeze=True)
print(data.max()) # 396

## 11. describe
data = pd.read_csv('./kohli_ipl.csv', squeeze=True)
print(data.describe())
# Output:
# count     215.000000
# mean      30.855814
# std       26.229801
# min       0.000000
# 25%       9.000000
# 50%       24.000000
# 75%       48.000000
# max       113.000000
# Name: runs, dtype: float64


#################################################################################

# Series Indexing

## integer indexing
x = pd.Series([12, 13, 14, 35, 46, 57, 58, 79, 9])
print(x[0]) # 12
print(x[1]) # 13
print(x[-1]) # Note: Negative indexing will not work on pandas series

## slicing
data = pd.read_csv('./kohli_ipl.csv', squeeze=True)
print(data[5:8])
# Output:
# 6     9
# 7     34
# 8     0

## negative slicing
data = pd.read_csv('./kohli_ipl.csv', squeeze=True)
print(data[-5]) # return last five values

## fancy indexing
data = pd.read_csv('./kohli_ipl.csv', squeeze=True)
print(data[[1,3,4,5]])
# Output:
# match_no
# 1     1
# 3     13
# 4     12
# 5     1
# Name: runs, dtype: int64

## indexing with labels - fancy indexing
data = pd.read_csv('./bollywood.csv', squeeze=True)
print(data['2 states (2014 film)']) # Arjun Kapoor
