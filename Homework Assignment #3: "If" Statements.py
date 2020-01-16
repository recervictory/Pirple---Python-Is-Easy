"""
Homework Assignment #3: "If" Statements

Details:

Create a function that accepts 3 parameters and checks for equality between any two of them.

Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.


Extra Credit:

Modify your function so that strings can be compared to integers if they are equivalent. For example, if the following values are passed to your function:

6,5,"5"

You should modify it so that it returns true instead of false.

Hint: there's a built in Python function called "int" that will help you convert strings to Integers.

"""
def if_statements(a,b,c):
  if int(a) == int(b):
    return True
  elif int(b) == int(c):
    return True
  elif int(c) == int(a):
    return True
  else:
    return False


def if_statements(a,b,c):
  if int(a) == int(b) or int(b) == int(c) or int(c) == int(a):
    return True
  else:
    return False

#Test 1
if if_statements(4,1,"4"):
  print("True")
else:
  print("False")

#Test 2
if if_statements(3,1,3):
  print("True")
else:
  print("False")