# -*- coding: utf-8 -*-
"""Py_Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1taGjUTm9CF6s5r7SpDqN8Trfpf3PtLsa
"""

# print your name 

print("SURAJ")

# print your hobbies 

print("Photography, Guitar")

# print your registration number

print("211047012")

# how to get more information about print functions 

help(print)

# how to get more infromation about math module 


import math
help(math)

# how to get more information about symbols


help('symbols')

#If your run a 1000 Kilo Meter race in 143 minutes 30 seconds, what is your average time per mile? What is your average speed in miles per hour? 



total_km = 1000

total_time_in_min = 143

total_time_in_seonds = 30

seconds_to_minutes = total_time_in_seonds/60

total_time = total_time_in_min + seconds_to_minutes

kilometer_to_mile = 0.621371 * total_km

average_time_per_mile_in_min = kilometer_to_mile/total_time

print(average_time_per_mile_in_min)

# Suppose the cover price of a python book  is  577.95, but bookstores get a 40% discount.


price_of_python_book = 577.95
discount = 40/100
the_price_of_book_after_discount = price_of_python_book * discount 
print(the_price_of_book_after_discount)

# Shipping costs  150 for the first copy and 50 Rupees for each additional copy. What is the total wholesale cost for 60 copies?


price_after_first_copy = 0
sum = 150

for i in range(1,60):
  sum_for_2_to_60_copies = 150
  sum_for_2_to_60_copies = sum_for_2_to_60_copies + (i * 50)
  #print(sum_for_2_to_60_copies)

total_sum = sum + sum_for_2_to_60_copies
print(total_sum)

# write a python code to convert Centrigrade to Fahrenheit , get the value Centrigrade from the user. 

temp_in_centi = float(input("Enter the temperature in  centrigrade "))
temp_in_fahren = (temp_in_centi * 1.8) + 32
print(temp_in_fahren)

# write a python code to convert Fahrenheit to Centrigrade, get the value Fahreheit from the user. 

temp_in_fahren = float(input("Enter the temperature in  Fahreheit "))
temp_in_cent = ((temp_in_fahren - 32) * (5/9))
print(temp_in_cent)

# Write a python program of your choice which uses arithmetic operations (use both operators and functions ) with meaningful application 


a = float(input("number1: ")) 
b = float(input("number2: "))
addition = a + b 
print(addition)
substraction = a - b
print(substraction)
multiplication = a * b
print(multiplication)
division = a / b
print(division)

# create a variable called my_neg to store  negative value 

my_neg = float(input("enter negative value"))
print(my_neg)

# create a variable called my_float to store float value 

my_float = float(input("enter float value"))
print(my_float)


# create a variable called my_complex to store complex value 
my_complex = complex(6,5)
print(my_complex)
print()


# perform mathematical operations on complex numbers 
print()

a = complex(6,5)
b = complex(6,8)

addition = a+ b
print(addition)

substraction = a - b
print(substraction)

multiplication = a * b
print(multiplication)

division = a/ b
print(division)

# create a variable called break and assign it a value of 15. what is the response and find the reason behind the behaviour.  

 break = 15 # since break is a inbuilt function we cannot assign anything to "break".

#Write a program to get the name of the guest , then greet the user using their name as part of greeting 

guest_name = input("")
print("I am extremly hounor to welcome ",guest_name)

import string

quotes  = "Don't judge each day by the harvest you reap but by the seeds that you plant."

# count the total number of characters in the variable quotes 



# convert the smaller case to upper case, upper case to smaller case 

print()
swap = quotes.swapcase()
print(swap)

# check whether the numeric value is present or not 

print()
check_num = quotes.isalnum()
print(check_num)

# Check whether the word "harvest" present in the string or not 

print()
check = quotes.count("harvest")
print(check)

# replace the (.) with (!) 
print()
replace = quotes.replace(".","!")
print(replace)

# Explore any 5 string build-in functions which is not discussed in the class
# provide with suitable examples 


test = " Testing the Functions  "

# isspace() checks if all the characters are whitespaces
check = test.isspace()
print(check)

#isupper() checks if all the letters in the sentence is upper case
check_2 = test.isupper()
print(check_2)

#isprintable() checks if the string is printable
check_3 = test.isprintable()
print(check_3)

#lower() returns the string into lower case
check_4 = test.lower()
print(check_4)

#title() returns the first vlaue of each case into upper case
check_5 = test.title()
print(check_5)

num_int =55
num_str =int("34")               # since num_str is a string value insted of a integer we cannot add them without chaging the data type
int(num_str)                      # so we can just change the string type into a data type using int data type function.
total = num_int + num_str
print (total)
print (type(num_int))
print (type(num_str))

#Find potential sources of runtime errors in this code snippet:
import math
dividend = float(input("Please enter the dividend: "))
divisor = float(input("Please enter the divisor: "))
quotient = dividend / divisor
quotient_rounded = math.ceil(quotient)      # math function does not have any function named round insted of round we can use ceil() or floor)() function.
print(quotient_rounded)

# print the quotes : Don't judge each day by the harvest you reap but by the seeds that you plant.
# Example for syntax Error 

primt Don't judge each day by the harvest you reap but by the seeds that you plant

# print the Quotes :Don't judge each day by the harvest you reap but by the seeds that you plant.
print ("Don't judge each day by the harvest you reap but by the seeds that you plant")

# identify the error, label the type of error and correct the error 
class plant:
  crop_name ="Brinjal"
  yeid = "20kg"
# print name of the class, crop name and yeid 
print(plant)
p1 = plant()
print(p1.crop_name,p1.yeid)

x=10
print (x)
print ("the value of x :",x )

# Find the errors in the coding and correct 
# formula to convert centrigrade to fahr


C = 21; F = ((9/5)*C) + 32     # since programming uses bodams brackets are necessary
print(F)
C = 21.0; F = ((9/5)*C) + 32
print(F)

#Explain why the code is not working 
c= a+ b       # we cannot execute a operation before declating the variables, though the code gets executed we wont get the desired results as it contains junk vlaue
a =10                 
b = 5 
print(c)

# Find the bugs in the below code, correct the mistakes and comment suggestions 
from math import pi
h = 5.0 # height
b = 2.0 # base
r = 1.5 #radius
area_parallelogram = h*b
print("The area of the parallelogram is %.3f" % area_parallelogram)
area_square = b**2
print("The area of the square is %g" % area_square)
area_circle = pi*r**2
print ("The area of the circle is %.3f" % area_circle)
volume_cone = 1.0/3*pi*r**2*h
print("The volume of the cone is %.3f" % volume_cone)

# This code shows the use math module 
# Run time error and Logical Error 
import math
from math import sin
c = 0
r = sin(c)

x=2.4
y = 2.5 + 3j
y_new = float(abs(y))
print(y_new)

math.sin(x)

#math.sin(y) we cannot use a complex number in sin

math.sin(y_new)

print("Hello, World!")
print(5 + 2)
print("All finished!")

# Print the statement, Kindly help me!
print ("Kindly help me!")

# print the value of the course 
course = "Programming with Python"
print ("course")

#store the size of the land in the variable size  in square feet 
size = 200 
#store the income as in
#print the value of  both size and income 
income= 9000
cropName="Drumstick"
year_2021 = "Drumstick"
print(size,income)

print ("Don't eat those cookies before dinner.")

print ("Hello \t \t \t world ")

print ("I like Python Programming!")

print ("The first program in any programming language is 'Hello World'.")

cropname = "Onions"
print (cropname)

# find the bug
1/2  # the bug was unappropiate space known as IndentationError

profit = 1000
#increment profit by 1
profit+=1
print(profit)

import math
print(math.log(10))

import math
print(math.sin(2))

num_int =55
num_str =float("34") 
total = num_int + num_str # since we cant add string and int we can just convert the string into a float value.
print (total)
print (type(num_int))
print (type(num_str))

# Trying to print the multiplication entry, but it throws error 

#  5*6 =30  cannot assign values to operands

c = 5 * 6
print(c)

# Trying to find the round of 10.2 
import math
round =  math.floor(10.2)
print(round)

import math
round =  math.ceil(10.2)
print(round)

import math
math.pow(2,5)

#Trying to multiply 5 
5 * 5

# Trying to print the text message Hello 

print("Hello")

#store the size of the land in the variable size  in square feet 
size = 200 
#store the income as in
#print the value of  both size and income 


income  = 9000 # since in is a inbuilt function we cannot assign anything to " in ".
cropName="Drumstick"
year_2021 = 'Drumstick'
print(size,income)