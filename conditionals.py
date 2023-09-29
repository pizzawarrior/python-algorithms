## Join test:
# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"
# x = mySeparator.join(myDict)
# print(x)



# user_input = input("Choose a color: Red, Yellow, or Green: ")
# print(user_input)
# if user_input.lower() == "Red":
#     print("Stop!")
# elif user_input.lower() == "Green":
#     print("Go!")
# elif user_input.lower() == "Yellow":
#     print("Slow Down!")
# else:
#     print(f"Go Home!! The color {user_input} is not a choice!")


# age_guesser = input("What year were you born? ")
# age = 2023 - int(age_guesser)
# print(f"User age is: {age}.")


# Exercises

# # 1. Write a program to check whether a number entered is three digit number or not.
# num_entered = input("Enter a number! ")
# print(num_entered)
# if len(num_entered) == 3:
#     print("You entered a 3 digit number!")
# else:
#     print(f"You entered a {len(num_entered)} digit number!")



# # 2. Write a program to find the lowest number out of two numbers inputed by a user.

# first_num_input = input("Enter your first number! ")
# second_num_input = input("Enter your second number! ")
# print(f"{int(min(first_num_input, second_num_input))} is the lower number")



# # 3. Write a program to check whether a number (inputed by the user) is divisible by both 2 and 3.

# divide_num = input("Please enter a number ")
# if int(divide_num) % 6 == 0:
#     print(f"{divide_num} is divisible by both 2 and 3.")
# else:
#     print(f"{divide_num} is NOT divisible by both 2 and 3.")


# 4. Accept as input three sides of a triangle and check whether it is an equilateral, isosceles, or scalene triangle

# first_side = int(input("Please enter a number "))
# second_side = int(input("Please enter a second number "))
# third_side = int(input("Please enter a third number "))
# if first_side == second_side & second_side == third_side:
#     print("Equilateral")
# elif first_side == second_side or first_side == third_side or second_side == third_side:
#     print('Isosceles')
# else:
#     print("Scalene")

# 5. Accept three numbers from the user and display the second largest number

# first_num = int(input("Please enter a number "))
# second_num = int(input("Please enter a second number "))
# third_num = int(input("Please enter a third number "))
# ##add nums to list, sort, then pull num at position1
# new_list = [first_num, second_num, third_num]
# sorted_list = (sorted(new_list))
# print(sorted_list[1])


# 6. Write a program to convert temperatures to and from Celsius and Fahrenheit -
# take user input - "Input the temperature you would like to convert? (e.g, 45F, 102C, etc..")
# sample output will look like:
# Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : 104f
# The temperature in Celsius is 40 degrees.

# user_temp = input("Enter a temp in F or C you would like to convert: ")
# convert_temp = user_temp.rstrip(user_temp[-1])
# #convert_temp = user_temp.removesuffix('f')
# if user_temp[-1].lower() == 'f':
#     print(f"The temperature in Celsius is {(int(convert_temp) - 32) / 1.8} degrees.")
# elif user_temp[-1].lower() == 'c':
#     print(f"The temperature in Fahrenheit is {(int(convert_temp) + 32) * 1.8} degrees.")
# else:
#     print("Please enter a temperature followed by F for Fahrenheit, or C for Celsius")

# Alternative methods for the challenge above: removesuffix(), and endswith()


# 7. Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years.
# After that, each dog year equals 4 human years.
# sample output:
# Input a dog's age in human years: 12
# The dog's age in dog's years is 61

# human_years = int(input("Enter your Dog's name in hooman years: "))
# if human_years <= 2:
#     print(f"Your dog is {human_years * 10.5} years old in dog years")
# else:
#     print(f"Your dog is {(human_years -2) * 4 + 21} years old in dog years")


# 8. Write a Python program to check whether a letter  is a vowel or consonant.

# letter_check = input("Please enter a letter to check if it is a vowel or consonant ")
# vowels = 'aeiou'
# if letter_check.lower() in vowels:
#     print("Your letter is a vowel")
# else:
#     print("Your letter is a consonant")


# 9.Write a Python program to convert a month name to a number of days.
# sample output:
# List of months: January, February, March, April, May, June, July, August, September, October, November, December
# Input the name of Month: April
# No. of days: 30 days

# Assuming an actual month is spelled and input correctly:
# month_input = input("Please add the month you would like to convert to days: ")
# thirty_days = ['april', 'june', 'september', 'november']
# if month_input.lower() == 'february':
#     print(f"The month of {month_input.capitalize()} has 28 days")
# elif month_input.lower() in thirty_days:
#     print(f"The month of {month_input.capitalize()} has 30 days")
# else:
#     print(f"The month of {month_input.capitalize()} has 31 days")




# 10. Write a Python program to display the astrological sign for a given date of birth.
# sample output:
# Input birthday: 18
# Input month of birth (e.g. march, july etc): january
# Your Astrological sign is : Capricorn
