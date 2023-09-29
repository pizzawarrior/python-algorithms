# my_list = ["Evander", 22, True]
# print(my_list)


# favorite_foods = []
# food = input("what is your fave food? ")
# favorite_foods.append(food)

# food = input("what is another of your fave foods? ")
# favorite_foods.append(food)

# food = input("what is your LAST and FINAL fave food? ")
# favorite_foods.append(food)

# # print("Your fave foods are", favorite_foods)

# num_foods = len(favorite_foods)
# # print("That's", num_foods, "of your favorite foods.")
# # or
# print(f"That's {num_foods} of your favorite foods")



# days_of_week = [
#     "Sunday",
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday"
# ]

# # days_of_week[3] = 'Hump day!'
# # print(days_of_week)

# days_of_week[5] = 'Fri-YAY!'
# print(days_of_week)

# #List comprehensions:
# wow_list = [char for char in 'hello']
# print(wow_list)

# #RANGE:
# wow_list2= [num for num in range(0, 100)]
# print(wow_list2)

# wow_list3 = [num * 3 for num in range(0, 33)]
# print(wow_list3)

# #add conditional
# wow_list4 = [num for num in range(0, 50) if num % 2 == 0]
# print(wow_list4)

# #check for duplicates in list:
# some_list = ['a', 'b', 'c', 'd', 'b', 'b', 'n', 'm', 'n']
# duplicates = []
# for char in some_list:
#     if some_list.count(char) > 1 and char not in duplicates:
#         duplicates.append(char)
# print(duplicates)


#another test:
# #create a tree:
# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]
# # print(picture)
# for row in picture:
#     line = ''
#     for pixel in row:
#         if pixel:
#             line += '*'
#         else: line += ' '
#     #inside loop: print each line
#     print(line)
#     #inside loop: create a new line with empty string, repeat process
#     # line = ''

# # Alternative:
# for row in picture:
#     for pixel in row:
#         if pixel == 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')


# #Fun exercise:
# a, b, c, *other, d = [1,2,3,4,5,6,7,8,8,9]
# # print(a)
# print(other)
# # print(d)



##Practice Probs:

# 1: Reverse a list
# list1 = [100, 200, 300, 400, 500]
# print(list1[::-1])

#2. Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# for num in numbers:
#     print(num ** 2)

# 3. Add new item to a list after a specified item
# Task: Add item 7000 after 6000 in the following list
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].insert(2, 7000)
# print(list1)


# List Comprehension:::

# def multiply_by_two(numbers):
#     return [num * 2 for num in numbers]

# def add_by_two(numbers):
#     return [num + 2 for num in numbers]

# def to_uppercase(strings):
#     return [s.upper() for s in strings]

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name


# def get_first_names(people):
#     return [person.first_name for person in people]

# LIST OF DICTIONARIES::::::

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name


# def get_names(people):

#     return [
#         {'first_name': person.first_name, "last_name": person.last_name}
#             for person in people
#     ]
