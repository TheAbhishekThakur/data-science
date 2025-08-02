# List in Python

list = [10, 20, 30.5, "Abhishek", [5,3,5,2], True]
for i in range(len(list)):
    print("Element at index", i, "is", list[i])
print("Length of the list is", len(list)) # 6
print("List is of type", type(list)) # <class 'list'>

# print memory address of the list
print("Memory address of the list is", id(list)) # Memory address of the list variable

# Print memory address of a variable
a = 10
print("Memory address of variable 'a' is", id(a)) # Memory address of 'a' variable


# Characteristics of a list
# 1. Ordered: Elements have a defined order, and that order will not change.
# 2. Mutable: Elements can be changed, added, or removed.
# 3. Hetrogeneous: Elements can be of different data types.
# 4. Allows duplicate values: Lists can have multiple occurrences of the same value.
# 5. Dynamic: Lists can grow and shrink in size as elements are added or removed.
# 6. Nested: Lists can contain other lists as elements, allowing for complex data structures.
# 7. Indexing and Slicing: Elements can be accessed using their index, and slices of the list can be created.
# 8. Supports various methods: Lists come with built-in methods for manipulation, such as
#    append(), remove(), pop(), sort(), reverse(), and more.
# 9. Can contain any kind of object in the list


# Create a List

# Empty List
empty_list = []
print("Empty list:", empty_list)

# 1D List
one_d_list = [1, 2, 3, 4, 5]
print("1D list:", one_d_list)

# 2D List (List of Lists)
two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("2D list:", two_d_list)

# 3D List (List of Lists of Lists)
three_d_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("3D list:", three_d_list)

# Heterogeneous List
heterogeneous_list = [1, "two", 3.0, [4, 5], True]
print("Heterogeneous list:", heterogeneous_list)

# Using Type conversion to create a list
# Converting a string to a list of characters
string = "Hello"
char_list = list(string)
print("List from string:", char_list)


# Accessing items in a list
# Using indexing
list_example = [10, 20, 30, 40, 50, [80, 90]]
print("First element:", list_example[0])  # Output: 10
print("Last element:", list_example[-1])  # Output: 50
print("Nested list element:", list_example[5][0])  # Output: 80

# Using slicing
print("First three elements:", list_example[:3])  # Output: [10, 20, 30]
print("Last two elements:", list_example[-2:])  # Output: [40, 50]
print("Middle elements:", list_example[2:4])  # Output: [30, 40]
print("Reverse the list:", list_example[::-1])  # Output: [[80, 90], 50, 40, 30, 20, 10]


# Adding items to a list

# Using append() to add a single item
list_example = [10, 20, 30]
list_example.append(40)
print("After append:", list_example)  # Output: [10, 20, 30, 40]

# Using extend() to add multiple items
list_example.extend([50, 60])
print("After extend:", list_example)  # Output: [10, 20, 30, 40, 50, 60]
list_example.extend("Hello")  # Adding a string will add each character as an item
print("After extend with string:", list_example)  # Output: [10, 20, 30, 40, 50, 60, 'H', 'e', 'l', 'l', 'o']

# Using insert() to add an item at a specific index
list_example.insert(2, 25)
print("After insert:", list_example)  # Output: [10, 20, 25, 30, 40, 50, 60]


# Editing items in a list

# Using indexing to change an item
list_example = [10, 20, 30, 40, 50]
list_example[1] = 15
print("After editing index 1:", list_example)  # Output: [10, 15, 30, 40, 50]

# Using slicing to change multiple items
list_example[2:4] = [35, 45]
print("After editing slice [2:4]:", list_example)  # Output: [10, 15, 35, 45, 50]


# Deleting items from a list
# Using del to remove an item by index
list_example = [10, 20, 30, 40, 50]
del list_example[1]
print("After del index 1:", list_example)  # Output: [10, 30, 40, 50]
del list_example # to remove the entire list

# Using remove() to remove an item by value
list_example.remove(30)
print("After remove 30:", list_example)  # Output: [10, 40, 50]

# Using pop() to remove the last item or an item by index
last_item = list_example.pop()  # Removes and returns the last item
print("After pop:", list_example)  # Output: [10, 40]
print("Popped item:", last_item)  # Output: 50

# Using pop() with an index
list_example.pop(0)  # Removes the item at index 0
print("After pop index 0:", list_example)  # Output: [40]

# Using clear() to remove all items
list_example.clear()
print("After clear:", list_example)  # Output: []

# Using slice assignment to remove items
list_example = [10, 20, 30, 40, 50]
list_example[1:3] = []  # Removes items at index 1 and 2
print("After slice assignment [1:3]:", list_example)  # Output: [10, 40, 50]


# Operators on lists

# 1. Arithmetic Operators
list_example = [1, 2, 3]
list_example2 = [4, 5, 6]
list_example3 = list_example + list_example2  # Concatenation
print("Concatenated list:", list_example3)  # Output: [1, 2, 3, 4, 5, 6]
list_example4 = list_example * 2  # Repetition
print("Repeated list:", list_example4)  # Output: [1, 2, 3, 1, 2, 3]

# 2. Membership Operators
print("Is 2 in list1?", 2 in list_example)  # Output: True
print("Is 5 in list1?", 5 in list_example)  # Output: False
print("Is 10 not in list1?", 10 not in list_example)  # Output: True

# 3. Loop
list_example = [1, 2, 3, 4, 5]
for item in list_example:
    print("Item:", item)  # Output: Item: 1, Item: 2, ..., Item: 5



# Functions on lists

# Length of a list
list_example = [10, 20, 30]
print("Length of list1:", len(list_example))  # Output: 3

# Finding the maximum and minimum values in a list
numbers = [10, 20, 30, 40, 50]
print("Maximum value:", max(numbers))  # Output: 50
print("Minimum value:", min(numbers))  # Output: 10

# Sorting a list
unsorted_list = [30, 10, 20, 50, 40]
unsorted_list.sort()
print("Sorted list:", unsorted_list)  # Output: [10, 20, 30, 40, 50]

# Reversing a list
reversed_list = unsorted_list[::-1]
print("Reversed list:", reversed_list)  # Output: [50, 40, 30, 20, 10]
reversed_list2 = sorted(unsorted_list, reverse=True) 
print(reversed_list2) # Output: [50, 40, 30, 20, 10]

# Counting occurrences of an item in a list
count_list = [1, 2, 2, 3, 3, 3, 4]
count_of_2 = count_list.count(2)
print("Count of 2 in count_list:", count_of_2)  # Output: 2

# Finding the index of an item in a list
index_of_3 = count_list.index(3)
print("Index of first occurrence of 3:", index_of_3)  # Output: 3

# Reversing a list in place
list_example = [1, 2, 3, 4, 5]
list_example.reverse()
print("Reversed list in place:", list_example)  # Output: [5, 4, 3, 2, 1] (note: this modifies the original list)

# Sorting a list in place
list_example = [30, 10, 20, 50, 40]
list_example.sort()
print("Sorted list in place:", list_example)  # Output: [10, 20, 30, 40, 50] (note: this modifies the original list)

# Copying a list
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print("Original list:", original_list)  # Output: [1, 2, 3, 4, 5]
print("Copied list:", copied_list)  # Output: [1, 2, 3, 4, 5]


# List Comprehensions

# List Comprehensions provides a concise way to create lists.
# new_list = [expression for item in iterable if condition]

# Advantages of List Comprehensions:
# 1. More time efficient and space efficient than traditional loops.
# 2. More readable and concise, making the code easier to understand.
# 3. Transforms iterative statement into a formula.

# Creating a list of squares using list comprehension
squares = [x**2 for x in range(10)]
print("List of squares:", squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Add 1 to 10 numbers to a list
# Traditional method
list = []
for i in range(1, 11):
    list.append(i + 1)
print("List after adding 1 to each number from 1 to 10:", list)

# Using list comprehension
list = [i for i in range(1, 11)]
print("List after adding 1 to each number from 1 to 10 using list comprehension:", list) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Scaler multiplication on a vector
vector = [1, 2, 3, 4, 5]
scaler = -3

scaled_vector = [i * scaler for i in vector]
print("Scaled vector:", scaled_vector)  # Output: [-3, -6, -9, -12, -15]


# Add squares of numbers from 1 to 10 to a list
squares = [i**2 for i in range(1, 11)]
print("Squares numbers from 1 to 10:", squares) # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Print all numbers divisible by 5 in the range of 1 to 50
divisible_by_5 = [i for i in range(1, 51) if i % 5 == 0]
print("Numbers divisible by 5 from 1 to 50:", divisible_by_5) # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Find languages which start with letter 'P'
languages = ["Python", "Java", "C++", "Perl", "PHP", "JavaScript"]
p_languages = [lang for lang in languages if lang.startswith('P')]
print("Languages starting with 'P':", p_languages)  # Output: ['Python', 'Perl', 'PHP']

# Nested if with list comprehension
# Add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'
basket = ["apple", "gauva", "cherry", "banana"]
my_fruits = ["apple", "kiwi", "grapes", "banana"]

my_fruits_in_basket = [fruit for fruit in my_fruits if fruit in basket and fruit.startswith('a')]
print("Fruits in basket that start with 'a':", my_fruits_in_basket)  # Output: ['apple']

# Print a (3,3) matrix using list comprehension -> Nested List Comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("3x3 Matrix:")
for row in matrix:
    print(row)  # Output: [1, 2, 3], [2, 4, 6], [3, 6, 9]

# Cartesian Products -> List Comprehension on 2 lists together
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
cartesian_product = [(x, y) for x in list1 for y in list2]
print("Cartesian Product:", cartesian_product)  
# Output: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]


# Two Ways to traverse a list

# 1. Itemwise
list_example = [10, 20, 30, 40, 50]
for item in list_example:
    print("Item:", item)  # Output: Item: 10, Item: 20, ..., Item: 50

# 2. Indexwise
list_example = [10, 20, 30, 40, 50]
for index in range(0, len(list_example)):
    print("Item at index", index, "is", list_example[index])  # Output: Item at index 0 is 4, ..., Item at index 4 is 50

# Zip function

# The zip() function returns a zip object, which is an iterator of tuples where the first
# item in each passed iterator is paired together.
# If the passed iterators have lengths, the iterator with the least items decides the length of the new iterator.

l1 = [1, 2, 3]
l2 = [-1, -2, -3]

zipped = list(zip(l1, l2))
print("Zipped list:", list(zipped))  # Output: [(1, -1), (2, -2), (3, -3)]


# Disadvantages of Lists
# 1. Slow Performance: Lists can be slower for certain operations compared to other data structures like sets or dictionaries, especially for large datasets.
# 2. Memory Overhead: Lists can consume more memory than necessary, especially if they contain a mix of data types or if they are resized frequently.
# 3. Inefficient Search: Searching for an item in a list can be inefficient, as it requires a linear search (O(n) time complexity) unless the list is sorted.
# 4. Lack of Built-in Hashing: Lists do not support hashing, which means they cannot be used as keys in dictionaries or stored in sets.
# 5. No Direct Support for Mathematical Operations: Unlike arrays in libraries like NumPy, lists do not support direct mathematical operations on


# Can contain any kind of object in the list
list_example = [1, print, type, input]
print(list_example[0])  # Output: [1, <built-in function print>, <class 'type'>, <built-in function input>]