# Q1 :- Print the given strings as per stated format.
# "Data" "Science" "Mentorship" "Program" "By" "CampusX"

print("Data","Science","Mentorship","Program","By","CampusX", sep="-")
# Data-Science-Mentorship-Program-By-CampusX



# Q2:- Write a program that will convert celsius value to fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")



# Q3:- Take 2 numbers as input from the user. Write a program to swap the numbers without using any special python syntax.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# Swapping without using a temporary variable
a = a + b
b = a - b
a = a - b
print(f"After swapping: a = {a}, b = {b}")



# Q4:- Write a program to find the euclidean distance between two coordinates. Take both the coordinates from the user as input.
import math
x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")


# Q5:- Write a program to find the simple interest when the value of principle, rate of interest and time period is provided by the user.
principle = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))
simple_interest = (principle * rate_of_interest * time_period) / 100
print(f"The simple interest is: {simple_interest:.2f}")

# Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
# For example: Input: heads -> 4 legs -> 12
# Output: dogs -> 2 chicken -> 2
heads = int(input("Enter the total number of heads: "))
legs = int(input("Enter the total number of legs: "))




# Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.

# Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.

# Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.

# Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
# Input: Dimensions of the milk tank
# H = 20cm, L = 20cm, B = 20cm

# Dimensions of the glass
# h = 3cm, r = 1cm