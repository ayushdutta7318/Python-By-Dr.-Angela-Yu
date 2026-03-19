# Type Error, Type Checking and Type Conversion:

"""
TypeError means error which is related to datatypes
"""
# print(len(123)) --> o/p --> TypeError

"""
To Check Datatype: use type() fn. This is called type_checking
"""

print(type("Hello"))
print(type(3))
print(type(3.14))
print(type(True))

# Type Conversion: To convert datatype of a variable

num = int(input("Enter a number: "))

print(f"number entered: {num} and its type is: {type(num)}")

int_num = float(3)
print(f"integer to float value: {int_num} and its type is: {type(int_num)}")

result_1 = bool(0)
result_2 = bool(1)

print(f"result_1: {result_1} and result_2: {result_2}")

