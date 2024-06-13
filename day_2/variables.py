# Day 2: 30 Days of python programming
# Exercise: Level 1
# 1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# 2. Write a python comment saying 'Day 2: 30 Days of python programming'
# 3. Declare a first name variable and assign a value to it
# 4. Declare a last name variable and assign a value to it
# 5. Declare a full name variable and assign a value to it
# 6. Declare a country variable and assign a value to it
# 7. Declare a city variable and assign a value to it
# 8. Declare an age variable and assign a value to it
# 9. Declare a year variable and assign a value to it
# 10. Declare a variable is_married and assign a value to it
# 11. Declare a variable is_true and assign a value to it
# 12. Declare a variable is_light_on and assign a value to it
# 13. Declare multiple variable on one line
print()

first_name = 'Pierce'
last_name = 'Chin'
full_name = 'Pierce Chin'
country = 'U.S.A.'
city = 'Queens'
age = 40
year = 2024
is_married = False
is_true = True
is_light_on = True
first_name, last_name, country, age, is_married = 'Pierce', 'Chin', 'U.S.A.', 40, False

print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)
print(first_name, last_name, country, age, is_married)

print()

# Exercise: Level 2
# 1. Check the data type of all your variables using type() built-in function
# 2. Using the len() built-in function, find the length of your first name
# 3. Compare the length of your first name and your last name
# 4. Declare 5 as num_one and 4 as num_two
#   i. Add num_one and num_two and assign the value to a variable total
#   ii. Subtract num_two from num_one and assign the value to a variable diff
#   iii. Multiply num_two and num_one and assign the value to a variable product
#   iv. Divide num_one by num_two and assign the value to a variable division
#   v. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
#   vi. Calculate num_one to the power of num_two and assign the value to a variable exp
#   vii. Find floor division of num_one by num_two and assign the value to a variable floor_division
# 5. The radius of a circle is 30 meters.
#   i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
#   ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#   iii. Take radius as user input and calculate the area.
# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywordsCheck the data type of all your variables using type() built-in function

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))

print()

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

print()

def calculate_area_of_circle(pi, radius):
    area_of_circle = pi * radius**2
    return area_of_circle

pi = 3.14159
radius = float(input("Enter the radius of the circle: "))

area_of_circle = calculate_area_of_circle(pi, radius)
rounded_area = round(area_of_circle, 2) # Display only two dec
print(f"The area of the circle is: {rounded_area} meters")

print()

def calculate_circum_of_circle(pi, radius):
    circum_of_circle = 2 * pi * radius
    return circum_of_circle

pi = 3.14159
radius = float(input("Enter the radius of the circle: "))

circum_of_circle = calculate_circum_of_circle(pi, radius)
rounded_circum_of_circle = round(circum_of_circle, 2)
print(f"The circumference of the circle is: {rounded_circum_of_circle} meters")

print()

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
country = input('Enter the country you live in: ')
age = input('Enter your age: ')

print()

print(first_name, last_name, country, age)

print()