# Generators in Python

### To make an iterator, we need two classes:
## iterable
class my_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return my_iterator(self)

# iterator
class my_iterator:
    def __init__(self, iterable_obj):
        self.iterable = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            value = self.current
            self.current += 1
            return value

 #################################################################       

### Using Generators

def gen_demo():
    yield "first statement"
    yield "second statement"
    yield "third statement"

gen = gen_demo()
print(next(gen)) # "first statement"
print(next(gen)) # "second statement"
print(next(gen)) # "third statement"
# print(next(gen))  # This will raise StopIteration

## OR

for value in gen:
    print(value) # This will print all three statements

#################################################################

### Example: 1
def square(num):
    for i in range(num):
        yield i ** 2

gen = square(10)
print(next(gen)) # 1
print(next(gen)) # 4
print(next(gen)) # 9
print(next(gen)) # 16
print(next(gen)) # 25
print(next(gen)) # 36
print(next(gen)) # 49
print(next(gen)) # 64
print(next(gen)) # 81
# print(next(gen)) # This will raise StopIteration

## OR

for value in gen:
    print(value) # This will print remaining squares if any

#################################################################

### Example: Range function using Generators
def my_range(start, end):
    for i in range(start, end):
        yield i
    
gen = my_range(1, 10)
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
print(next(gen)) # 4
print(next(gen)) # 5
print(next(gen)) # 6
print(next(gen)) # 7
print(next(gen)) # 8
print(next(gen)) # 9
# print(next(gen)) # This will raise StopIteration


#################################################################

# Generator Expressions
L = [ i ** 2 for i in range(10) ] # List comprehension

G = ( i ** 2 for i in range(10) ) # Generator expression

for value in G:
    print(value) # This will print squares from 0 to 81


#################################################################

# Practical Example:
import os
import cv2

def image_date_reader(folder_path):
    for file in os.listdir(folder_path):
        f_array = cv2.imread(os.path.join(folder_path, file))
        yield f_array

image_gen = image_date_reader("path_to_your_image_folder")

next(image_gen) # This will read and return the first image array
next(image_gen) # This will read and return the second image array
# and so on...

#################################################################

# Benefits of Generators:

# 1. Ease of Implementation
# 2. Memory Efficiency
# 3. Represent Infinite Stream of Data
# 4. Composability
# 5. Improved Performance