
#Experimenting with creating custom errors:


import math

#This will run until it hits the 'divide 50/ 0 line'. At that point it will error out and stop running.
# def fifty_by(num):
#     return 50 / num

# print(fifty_by(5))
# print(fifty_by(15))
# print(fifty_by(0))
# print(fifty_by(1))



# TRY and EXCEPT, for when to deal with the above examples:
# def fifty_by(num):
#     return 50 / num
# try:
#     print(fifty_by(5))
#     print(fifty_by(15))
#     print(fifty_by(0))
#     print(fifty_by(1))
# except ZeroDivisionError:
#     print("Error: Invalid Argument")



# #Alternative #2:
# def fifty_by(num):
#     try:
#         return 50 / num
#     except ZeroDivisionError:
#         print("Error: Invalid Argument")

# print(fifty_by(5))
# print(fifty_by(15))
# print(fifty_by(0))
# print(fifty_by(1))
# print(fifty_by('A'))



# #Alternative #3: Add another exception for 'print(fifty_by('A'))
# def fifty_by(num):
#     try:
#         return 50 / num
#     except ZeroDivisionError:
#         print("Error: Invalid Argument")
#         return math.inf
#     except TypeError:
#         print("Error: Why u do me like this??")
#         return math.nan

# print(fifty_by(5))
# print(fifty_by(15))
# print(fifty_by(0))
# print(fifty_by(1))
# print(fifty_by('A'))


# Let's add our own error-- if someone tries to divide 50 by 1:

# class OneDivisionError(RuntimeError):
#     pass

# def fifty_by(num):
# # Because this new error message we created (if num == 1) is outside the try statement, the code will execute
# # until it gets to the line to divide 50 by 1. The error message will be triggered and the script execution will stop.
#     if num == 1:
#         raise OneDivisionError
#     try:
#         return 50 / num
#     except ZeroDivisionError:
#         print("Error: Invalid Argument")
#         return math.inf
#     except TypeError:
#         print("Error: Why u do me like this??")
#         return math.nan

# print(fifty_by(5))
# print(fifty_by(15))
# print(fifty_by(0))
# print(fifty_by(1))
# print(fifty_by('A'))



# # try/ except example:
# def divide_vars(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         return 'Systems critical: a numerator will never be divisible by zero!!'

# print(divide_vars(3, 0))
