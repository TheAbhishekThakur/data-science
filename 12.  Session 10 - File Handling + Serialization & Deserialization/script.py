# File Handling + Serialization & Deserialization

## Writing to a file

### Case 1: if the file is not present
file = open("sample.txt", "w")
file.write("Hello World")
file.close()

### Write multiple line string
file2 = open("sample2.txt", "w")
file2.write("Hello World")
file2.write("\n")
file2.write("How are you?")
file2.close()


### Case 2: if the file is already present
file3 = open("sample.txt", "w") # sample.txt is a file path
file3. write("Abhishek Thakur")


### How exactly open() works?
# Python checks if the file exists (for reading).
# It opens a connection (file descriptor) to the file.
# If opening for writing and the file doesn’t exist, it creates it.
# The file object manages reading/writing and buffering.
# When you’re done, closing the file releases system resources.


### Problem with "w" mode
# 1. Accidental Data Loss:
# If you open an existing file in "w" mode, all its previous contents are erased. This can lead to accidental data loss if you meant to add to the file instead of overwriting it.

# 2. Cannot Read:
# You cannot read from a file opened in "w" mode. If you try f.read(), you’ll get an error.

# 3. File Not Created in Non-Existent Directory:
# If you specify a path to a directory that doesn’t exist, Python will raise a FileNotFoundError.



### Introducing "append" mode
file4 = open("sample2.txt", "a")
file4.write("\n")
file4.write("I am fine")
file4.close()


### Write lines
file5 = open("sample3.txt", "w")
L = ["Hello\n", "Hi\n", "How are you\n", "I am fine\n"]
file5.writelines(L)
file5.close()


### Reading from files
data = open("sample3.txt", "r")
str_data = data.read()
print(str_data)
# Output:
# Hello
# Hi
# How are you
# I am fine


### Reading upto "n" characters
data = open("sample3.txt", "r")
str_data = data.read(10)
print(str_data)
# Output:
# Hello
# Hi
# H

### readline() -> To read line by line
data = open("sample3.txt", "r")
str_data1 = data.readline()
str_data2 = data.readline()

print(str_data1) # Hello
print(str_data2) # Hi


### Reading entire using readline()
data = open("sample3.txt", "r")
while True:
    data2 = data.readline()
    if data2 == "":
        break
    else:
        print(data2)
data.close()




##############################################################################

# Using Context Manager (With)

with open("sample3.txt", "w") as f:
    f.write("Hello")

# try f.read() now
with open("sample.txt", "r") as f:
    print(f.read())

# Moving within a file -> 10 char then 10 char
with open("sample2.txt", "r") as f:
    print(f.read(5)) # Hello
    print(f.read(5)) #  Worl

# Benifit? -> To load a big file in memory
big_l = ["Hello world " for i in range(1000)]

with open("big.txt", "w") as f:
    f.writelines(big_l)

with open("big.txt", "r") as f:
    chunk_size = 100

    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size), end="**")
        f.read(chunk_size)

# seek() and tell() function
with open("sample2.txt", "r") as f:
    print(f.read(5)) # Hello
    print(f.tell()) # 5 - Check the index of next character after process
    f.seek(2) # 2 - It will 2th index again
    print(f.read(5)) # llo W

# seek() during write
with open("sample4.txt", "w") as f:
    f.write("Hello")
    f.seek(0)
    f.write("X")

# Output: Xello

#######################################################################################

## Working with binary file

### Problem:
# with open("pythonvsjavascript.jpg", "r") as f:
#     f.read() # Error: Can't read binary files

### Solution:
with open("pythonvsjavascript.jpg", "rb") as f:
    with open("pythonvsjavascript_copy.jpg", "wb") as wf:
        wf.write(f.read())

## Working with a big binary file

## Working with other data types
# with open("sam1.txt", "w") as f:
#     f.write(5) # TypeError: write() argument must be str, not int


#######################################################################################

# Serialization and Deserialization

## Serialization using JSON module
### list
import json
L = [1,2,3,4]
with open("demo.json", "w") as f:
    json.dump(L, f)

### dict
import json
d = {
    "name": "Abhishek",
    "age": 27,
    "gender": "Male"
}
with open("demo1.json", "w") as f:
    json.dump(d, f, indent=4)


## Deserialization using JSON module
import json
with open("demo1.json", "r") as f:
    d = json.load(f)
    print(d) # {'name': 'Abhishek', 'age': 27, 'gender': 'Male'}
    print(type(d)) # <class 'dict'>


## Serialization and Deserialization Tuple

### Serialization: If you Serialization tuple, it will return list
import json
t = (1,2,3,4,5)

with open("demo_tuple.json", "w") as f:
    json.dump(t, f) # [1,2,3,4,5]


## # Serialization and Deserialization a nested dict

d = {
    "student": "nitish",
    "marks": [23, 14, 34, 45, 56]
}

with open("demo_dict.json", "w") as f:
    json.dump(d, f) # {"student": "nitish", "marks": [23, 14, 34, 45, 56]}



## Serialization and Deserialization Custom Objects

#### Format to print in: Nitish Singh age -> 33 gender -> male
import json
class Person:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

person = Person("Nitish", "Singh", 33, "male")

# def show_object(per):
#     if isinstance(per, person):
#         return "{} {} age -> {} gender -> {}".format(person.fname, person.lname, person.age, person.gender)

# with open("custom_obj.json", "w") as f:
#     json.dump(person, f, default=show_object)

# Deserialization

# import json
# with open("custom_obj.json", "r") as f:
#     d = json.load() 
#     print(d) # Nitish Singh age -> 33 gender -> male
#     print(type(d)) # <class 'str'>


#######################################################################################

### Pickling
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Hi my name is", self.name, 'an I am', self.age, 'years old')

person = Person("Abhishek", 27)
 
import pickle # pickle dump
with open("person.pkl", "wb") as f:
    pickle.dump(person, f)


import pickle # pickle read
with open("person.pkl", "rb") as f:
    data = pickle.load(f)
    print(data)

person.display_info()