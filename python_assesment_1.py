# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N6wFQMOzwBBwUtB_QCpULuFuCGHgxIkO

Q1
"""

length = int(input("enter lenth"))
width = int(input("width"))
area = length*width
print(f"area of ractange is : {area}")

"""Q2"""

weight = int(input("enter your weight in kg"))
height = int(input("enter your height in m"))
bmi = weight/((height)**2)
print(f"your bmi is {bmi}")

"""Q3"""

students = {}
stunum = int(input("no. of students"))
for i in range(stunum):
  name = input("enter name")
  score = input("score")
  students[name] = score
print(students)

"""Q4"""

age = int(input("enter your age"))
if age < 18:
  print("you are minor")
elif  18 < age <60 :
  print("yoy are adult")
else:
  print("you are senior")



"""Q5"""

n = 50
for i in range(n):
  if i%2 == 0:
    print(i)
  else:
    continue

"""Q6"""

password = 'sanju@123'

while True:
  types = input("enter password")
  if types == password:
    print("correct password")
    break
  else:
    print("inncorect password")

"""Q7"""

def calculate_average(numbers):

    if not numbers:
        return 0

    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [5, 10, 15, 20, 25]
average = calculate_average(numbers)
print("Average:", average)

"""Q8"""

stringname = input("enter string")

def countvowel(string):
  vowels = ['a','e','i','o','u']
  total = 0
  n = len(string)
  for i in range(n):
    letter = string.pop()
    if letter  in vowels:
      total = 1 +  total
    else:
      total = total
      print(f"total no. of vowels are {total}")

countvowel(stringname)

"""Q9"""

from datetime import datetime
dt = datetime.now()
print(f"Current date and time:{dt}")

"""Q10"""

#value = int(input("enter any integer"))
try:
  values = int(input("enter values"))
  print("correct")
except:
  print("Error occured")

"""Q11"""

while True:
  try:
    value1 = input("Please enter an integer: ")
    user_integer = int(value1)
    break
  except ValueError:
     print("Invalid input. Please enter a valid integer.")

print("CORRECT INTEGER:", user_integer)

"""Q12

"""

number = int(input("enter number"))
divider  = int(input("enter number"))
def divide(num,div):
  try:
    if divider == 0:
     print("number cannot be devided by zero" )

     print("correct")
  except:
     print("Error occured")

"""Q13"""

tw = "Hello, Python!"
filename = "hello_python!.txt"
with open(filename, 'w') as file:
    file.write(tw)
print(f"Text '{tw}' has been written to '{filename}'.")

"""Q14
Text 'Hello, Python!' has been written to 'hello_python!.txt'.

"""

with open("Hello_Python!.txt", "r") as file:
 file_content = file.read()
 print("Content of "Hello, Python!.txt:", file_content)
with open("Hello_Python!.txt", "a") as file:
 file.write("\nThis is additional content.")
print("Additional content written to Hello_Python!.txt")

"""Q15"""

tw = "Hello, Python!"
filename = "hello_python!.txt"
with open(filename, 'w') as file:
    file.write(tw)
print(f"Text '{tw}' has been written to '{filename}'.")