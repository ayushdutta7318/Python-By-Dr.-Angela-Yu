# Introduction:

# print is a fn which prints to the console and inside parentheses comes what you wanna print.

print("Hello World!")

# escape char

print("Hello, Ayush\nHow are you?")

# str concatenation

print("hello" + " I am concatenated " + "string")

    # print("") indentation error

# print("Hello world) syntax error

# Assignment

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a '\' and the letter n")

####################################################################
# python input fn:

print("Hello " + input("Please enter your name: ") + "!")


name = input("Enter your name: ")

print(f"My name is {name}")

####################################################################

# Variables in Python:

num = int(input("Enter a number: "))

print(f"You entered number: {num}")

print(len(name))


# Assignment:

username = input("Enter your username: ")

length = len(username)

print(f"The length if the username is {length}")

# Assignment: Swap values

glass1 = "milk"
glass2 = "juice"

print(f"glass1: {glass1}")
print(f"glass2: {glass2}")

temp = glass1
glass1 = glass2
glass2 = temp

print(f"glass1: {glass1}")
print(f"glass2: {glass2}")

"""
Rules to name Variables:

1. no space in b/w
2. should not start with number
3. can contain an underscore in b/w 2 words: eg user_name

"""

time_until_midnight = "5"
print("There are "+time_until_midnight+" hours until midnight")














