# Dictionary
d = {}
print(d) # {}

# 1D Dictionary
d = { "name": "nitesh", "age": 33, "gender": "male" }
print(d) # { "name": "nitesh", "age": 33, "gender": "male" }

# With mixed keys
d = {(1,2,3): 1, "hello": "world"}
print(d) # {(1, 2, 3): 1, 'hello': 'world'}

# 2D Dictionary
student = {
    "name": "nitish",
    "college": "bit",
    "sem": 4,
    "subjects": {
        "dsa": 100,
        "maths": 88,
        "english": 34
    }
}
print(student)
# Output : {
#   "name": "nitish",
#    "college": "bit",
#    "sem": 4,
#    "subjects": {
#        "dsa": 100,
#        "maths": 88,
#        "english": 34
#   }
# }

# Using sequence and dict function
d4 = dict([(1,1), (2,2), (3,3)])
print(d4) # {1: 1, 2: 2, 3: 3}

# Duplicate keys
# Can't have duplicate keys, You will get last key:value

# Mutable items as keys
d6 = {"name": "nitish", [1,2,3]: 2}
print(d6) # TypeError: unhashable type: 'list'


# Accessing items
my_dict = {"name": "jack", "age": 26}
print(my_dict["name"]) # jack
print(my_dict.get("age")) # 26

# Adding key-value pair
d5 = {"name": "abhishek", "age": 27}
d5["gender"] = "Male"
print(d5) # {"name": "abhishek", "age": 27, "gender": "Male"}


## Remove key-value pair

# 1. pop
d5 = {"name": "abhishek", "age": 27}
d5.pop("name")
print(d5) # {"age":27}

# 2. popitem
d5 = {"name": "abhishek", "age": 27}
d5.popitem() # delete last key-value pair
print(d5) # {"name": "abhishek"}

# 3. del
d5 = {"name": "abhishek", "age": 27}
del d5 # delete whole dict
del d5["name"] # delete only name key-value pair
print(d5) # { "age": 27}

# 4. clear
d5 = {"name": "abhishek", "age": 27}
d5.clear() # Removed all the key-value pairs


## Dictionary Operations

# 1. Membership
d5 = {"name": "abhishek", "age": 27}
print("abhishek" in d5) # False
print("abhishek" not in d5) # True
print("name" in d5) # True

# 2. Iteration
d5 = {"name": "abhishek", "age": 27, "gender": "male"}
for key in d5:
    print(key) # "name, age, gender"
    print(d5[key]) # abhishek, 27, male


## Dictionary Functions

# 1. len
d6 = {"name": "abhishek", "age": 27, "gender": "male"}
print(len(d6)) # 3

# 2. sorted
d6 = {"name": "abhishek", "age": 27, "gender": "male"}
print(sorted(d6)) # Sorted all keys and return a list :- ["age", "gender", "name"]

# 3. items
d6 = {"name": "abhishek", "age": 27, "gender": "male"}
print(d6.items()) # Converted in array of tuples :- [("name", "abhishek"), ("gender", "male"), ("age", 27)]

# 4. keys
d6 = {"name": "abhishek", "age": 27, "gender": "male"}
print(d6.keys()) # ["name", "age", "gender"]

# 5. values
d6 = {"name": "abhishek", "age": 27, "gender": "male"}
print(d6.values()) # ["abhishek", 27, "male"]

# 6. update
d1 = {"name": "abhishek", "age": 27, "gender": "male"}
d2 = {"name": "sachin", "phone": "9999999999"}
print(d1.update(d2)) # {"name": "sachin", "age": 27, "gender": "male", "phone": "9999999999"}


## Dictionary Comprehension
# {key: value for vars in iterable}

# Print 1st 10 numbers and their squares
{i: i ** 2 for i in range(1,11)}
# Output - {1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}


# Convert kilometers into miles using existing dictionary
distances = {"delhi":1000, "mumbai":2000, "banglore": 3000}

{key:value*0.62 for (key, value) in distances.items()}
# Output - {"delhi":120.0, "mumbai":1240.0, "banglore": 1860.0}

# Using zip
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday"]
temp_C = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]

{key:value for (key, value) in zip(days,temp_C)}
# Output - {"Sunday":30.5, "Monday":32.6, "Tuesday": 31.8, "Wednesday":33.4, "Thrusday": 29.8, "Friday": 30.2, "Saturday": 29.9}

# Using if condition
products = {"phone": 10, "laptop": 0, "charger": 32, "tablet": 0}
{key:value for (key, value) in products.items() if value > 0}
# Output - {"phone": 10, "charger": 32}


# Nested Comprehension
# Print tables of number from 2 to 4
# {
#    2: {1:2,2:4,3:6,4:8,5:10,6:12,7:14,8:16,9:18,10:20},
#    3: {1:3,2:6,3:9,4:12,5:15,6:18,7:21,8:24,9:27,10:30},
#    4: {1:4,2:8,3:12,4:16,5:20,6:24,7:28,8:32,9:36,10:40},
# }

{i: {i*j for j in range(1,11)} for i in range(2, 5)}