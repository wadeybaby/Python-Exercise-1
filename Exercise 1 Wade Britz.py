# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
print("Hello User. What is your name? ")
name = input("name:")
username = name
# TODO: Ask the user for their age and store it in a variable
print(name + ", What is your age?")
age= input("age:")
userage = age
# TODO: Print a greeting using the name and age variables
print("Hello, " + username + ", " + userage)
#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
print("What is the length of a rectangle?")
length = int (input('length:') )

# TODO: Ask the user for the width of a rectangle and store it as an integer
print("What is the width of a rectangle?")
width = int (input('width:'))

# TODO: Calculate the area of the rectangle
print('Calculate the area of the rectangle')
area = length * width
# TODO: Print the result
print('Area:' , str(area))
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
print(name +'.' + ' What is the temperature in Celcius?')
temp_cel = float(input('temperature:'))
letter = '°F'
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
print('Convert the temperature in Celcius to Fahrenheit')
temp_fah = str((temp_cel * 9/5) + 32) + letter
# TODO: Print the result rounded to two decimal places
print(int(round(temp_fah , 2)))