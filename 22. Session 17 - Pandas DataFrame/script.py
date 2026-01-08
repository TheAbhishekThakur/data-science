import numpy as np
import pandas as pd

############ Creating DataFrame ############

## Using lists
student_data = [[100,80,10],[90,70,7],[120,100,14], [80,50,2]]
pd.DataFrame(student_data, columns=['IQ','Marks','Package'])
# Output:
#     IQ  Marks  Package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     50        2



## Using dictionary
student_dict = {
    'Name': ['A', 'B', 'C', 'D'],
    'IQ': [100,90,120,80],
    'Marks': [80,70,100,50],
    'Package': [10,7,14,2]
}
student_dict.set_index('Name', inplace=True) # Setting 'Name' column as index
pd.DataFrame(student_dict)
# Output:
#     IQ  Marks  Package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     50        2


############# DataFrame Attributes and Methods #############

## Using read_csv
movies = pd.read_csv('./files/movies.csv')
print(movies)

ipl = pd.read_csv('./files/ipl.csv')
print(ipl)

## shape
movies.shape
# Output: (1629, 18)
ipl.shape
# Output: (950, 20)

## dtypes
movies.dtypes
# Output: Printing data types of each column
# title                object
# genre                object
# director             object

# ........

## index
movies.index
# Output: RangeIndex(start=0, stop=1629, step=1)


## columns
movies.columns
# Output: Index(['title', 'genre', 'director', 'actors', 'year', 'runtime',
#        'rating', 'votes', 'revenue', 'metascore', 'color', 'language',
#        'country', 'content_rating', 'budget', 'gross', 'company', 'released'],
#       dtype='object')


## values
movies.values
# Output: 2D array of all values in the DataFrame

## head
movies.head()
# Output: First 5 rows of the DataFrame
movies.head(2)
# Output: First 2 rows of the DataFrame

## tail
movies.tail(3)
# Output: Last 3 rows of the DataFrame


## sample
movies.sample(4)
# Output: Random 4 rows from the DataFrame, if no number is specified, it returns 1 random row


## info
movies.info()
# Output: Summary of the DataFrame including index dtype and columns, non-null values and memory usage.

## describe
movies.describe() # Show only numerical columns
# Output: Statistical summary of numerical columns in the DataFrame (excludes NaN values by default)

## isnull
movies.isnull() # Check for null values in the DataFrame and return boolean values
# Output: DataFrame of same shape with boolean values indicating if the value is null or not

## duplicated
movies.duplicated() # Check for duplicate rows in the DataFrame and return boolean values
# Output: Series indicating if a row is a duplicate of a previous row or not (First occurrence is marked as False)

## rename
movies.rename(columns={'title': 'movie_title', 'rating': 'IMDB_rating'}, inplace=True) # inplace=True to make changes in the original DataFrame
movies.head(2)
# Output: First 2 rows of the DataFrame with renamed columns
#    movie_title  genre         director                     actors  year  \
# 0  Avatar      Action  James Cameron  Sam Worthington, Zoe Saldana  2009
# 1  Pirates of the Caribbean: At World's End  Action  Gore Verbinski  Johnny Depp, Orlando Bloom  2007
# ......
#    runtime  IMDB_rating  votes  revenue  metascore  color language country  \
# 0      162          7.9  890617    760.5       83  Color  English     USA
# 1      169          7.1  471220    309.4       63  Color  English     USA
# ......


################ Math Methods #############

## sum -> axis argument
student_data.sum() # Default axis=0, sum of each column
# Output: Series with sum of each column (for numerical columns only)
student_data.sum(axis=1) # sum of each row
# Output: Series with sum of each row (for numerical columns only)


## mean -> axis argument
student_data.mean() # Default axis=0, mean of each column
# Output: Series with mean of each column (for numerical columns only)
student_data.mean(axis=1) # mean of each row
# Output: Series with mean of each row (for numerical columns only)

## min -> axis argument
student_data.min() # Default axis=0, min of each column
# Output: Series with min of each column (for numerical columns only)
student_data.min(axis=1) # min of each row
# Output: Series with min of each row (for numerical columns only)


## max -> axis argument
student_data.max() # Default axis=0, max of each column
# Output: Series with max of each column (for numerical columns only)
student_data.max(axis=1) # max of each row
# Output: Series with max of each row (for numerical columns only)


## median -> axis argument
student_data.median() # Default axis=0, median of each column
# Output: Series with median of each column (for numerical columns only)
student_data.median(axis=1) # median of each row
# Output: Series with median of each row (for numerical columns only)


## std -> axis argument
student_data.std() # Default axis=0, standard deviation of each column
# Output: Series with standard deviation of each column (for numerical columns only)
student_data.std(axis=1) # standard deviation of each row
# Output: Series with standard deviation of each row (for numerical columns only)


## var -> axis argument
student_data.var() # Default axis=0, variance of each column
# Output: Series with variance of each column (for numerical columns only)
student_data.var(axis=1) # variance of each row
# Output: Series with variance of each row (for numerical columns only)


################# Selecting cols from a DataFrame #################

## single column
movies['movie_title'] # returns a Series
# Output: Series with all movie titles

## multiple columns
movies[['movie_title', 'IMDB_rating', 'year']] # returns a DataFrame, order of columns will be same as specified
# Output: DataFrame with selected columns


################# Selecting rows from a DataFrame #################

## 1. iloc (index based indexing)
## 2. loc (label based indexing)

## single row - iloc (index based indexing)
movies.iloc[0] # first row
# Output: Series with first row

## multiple rows - iloc (index based indexing)
movies.iloc[0:3] # first 3 rows (exclusive of last index)
# Output: DataFrame with first 3 rows

## fancy indexing - iloc (index based indexing)
movies.iloc[[0,2,5]] # rows at index 0, 2 and 5
# Output: DataFrame with rows at index 0, 2 and 5

## single row - loc (label based indexing)
movies.loc["A"] # first row (index label A)
# Output: Series with first row

## multiple rows - loc (label based indexing)
movies.loc["A":"C"] # rows from index label A to C (inclusive of last label)
# Output: DataFrame with rows from index label A to C

## fancy indexing - loc (label based indexing)
movies.loc[["A","C","E"]] # rows at index labels A, C and E
# Output: DataFrame with rows at index labels A, C and E


################# Selecting rows and columns from a DataFrame #################