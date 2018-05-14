# Quize 12: Define a procedure, square, that takes one number 
# as its input, and returns the square of that 
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

def sum(a,b):
    c = a + b
    return c

def square(num):
    return num * num

# To test your procedure, uncomment the print 
# statement below, by removing the hash mark (#) 
# at the beginning of the line.

# Do not remove the # from in front of the line 
# with the arrows (>>>). Lines which begin like 
# this (#>>>) are included to show the results
# you should see when run your procedure.

print (square(5))
#>>> 25

# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.
# To help you out, the code for sum(a,b) is below.

# def sum(a,b):
#     return a + b

def sum3(num1, num2, num3):
    return num1 + num2 + num3

print (sum3(1,2,3))
#>>> 6

print (sum3(93,53,70))
#>>> 216

# Quize 14: Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.

def abbaize(str1, str2):
    return str1 + str2*2 + str1

print (abbaize('a','b'))
#>>> 'abba'

print (abbaize('dog','cat'))
#>>> 'dogcatcatdog'

# Quize 15: Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second(search, target):
    inx = search.find(target)
    return search[inx+1:].find(target) + inx+1

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print (find_second(danton, 'audace'))
#>>> 25

twister = "she sells seashells by the seashore"
print (find_second(twister,'she'))
#>>> 13

# Quize 17: Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(x,y):
    if x>=y:
        return x
    else:
        return y
    
print (bigger(2,7))
#>>> 7

print (bigger(3,2))
#>>> 3

print (bigger(3,3))
#>>> 3

# Quize 18: Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

def is_friend(name):
    if name[0] == 'D': return True
    else: return False

print (is_friend('Diane'))
#>>> True

print (is_friend('Fred'))
#>>> False

# Quize 19: Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(name):
    return name[0] == 'D' or name[0] == 'N'

print (is_friend('Diane'))
#>>> True

print (is_friend('Ned'))
#>>> True

print (is_friend('Moe'))
#>>> False

# Quize 21: Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(x, y, z):
    if x >= y and x >= z: return x
    elif y >= x and y >= z: return y
    else: return z

# Quiz 24: Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(num):
  x = 1 
  while x <= num:
      print (x)
      x += 1

# Quize 25: Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    x = 1
    while n >= 1:
        x *= n
        n -= 1
    return x
