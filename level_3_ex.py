# Day 1: 30 Days of python programming
# Exercise: Level 3
# 1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# 2. Find an Euclidian distance between (2, 3) and (10, 8)

# Question 1
print(type(5))
print(type(6.627))
print(type(10 - 10j))
print(type('Blood'))
print(type(True))
print(type(['To', 'Be', 'Or', 'Not', 'To', 'Be']))
print(type((5.5, 6.6, 7.7)))
print(type({5.5, 6.6, 7.7}))
print(type({'set': 'Blood Stone Villain'}))

# Question 2
import math

# Define the points
point1 = (2, 3)
point2 = (10, 8)

# Calculate the differences
x_diff = point2[0] - point1[0]
y_diff = point2[1] - point1[1]

# Calculate the Euclidean distance
distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
print(distance)