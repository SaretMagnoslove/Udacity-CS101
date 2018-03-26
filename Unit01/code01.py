# Quiz 7: Write a Python program that prints out the number of minutes in seven weeks.
print (7 * 7 * 24 * 60)
# Quiz 14:Write Python code to print out how far light travels
print(299792458 * 100 * 1.0/1000000000)
# Quiz 18: Given the variables defined here, write Python 
# code that prints out the distance, in meters, 
# that light travels in one processor cycle.
speed_of_light = 299792458.0 
cycles_per_second = 2700000000.0
print(speed_of_light/cycles_per_second)
# Quiz 22: Write python code that defines the variable 
# age to be your age in years, and then prints 
# out the number of days you have been alive
age = 42
print (age * 365)
# Quiz 26: Define a variable, name, and assign to it a string that is your name.
name = 'Saret Magnoslove'
# Quiz 31: Write Python code that prints out Udacity (with a capital U), 
# given the definition of s below.
s = 'audacity'
print ('U' + s[2:])
# Quiz 39: Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.
page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''
start_link = page.find('<a href="')

# final Quiz!

# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to

# page = '<a href="http://udacity.com">Hello world</a>'

# that your code still assigns the same value to the variable 'url', 
# and therefore still prints the same thing.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
start_url = start_link + 9
end_url = page.find('"',start_url)
url = page[start_url:end_url]
print (url)