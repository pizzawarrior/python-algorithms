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


# # Run length encoding- take the following string and encode it
# # Notes: Order matters! Dictionaries are not ordered
# def encode_run(string):
#     result = ''
#     i = 0
#     while i < len(string):
#         count = 1
#         while i + 1 < len(string) and string[i] == string[i + 1]:
#             count += 1
#             i += 1
#         result += str(count) + string[i]
#         i += 1
#     return result

# run = 'aaabbbcccdabddfeeg'
# print(encode_run(run))  # Output: '3a2b3c1d1a1b2d1f2e1g'


# Run length decoding. Take the solution from above, and decode it back into the input string
# def decode_run(string):
#     result = ''
#     count = 0
#     if len(string) % 2 != 0:
#         return 'Error: string is not properly encoded'
#     for i in range(0, len(string) - 1, 2):
#         while count < int(string[i]):
#             result += string[i + 1]
#             count += 1
#         count = 0
#         i += 2
#     return result

# print(decode_run('3a3b3c1d1a1b2d1f2e1g'))


# # Return True when both arguments are arrays that have the same nesting
# #  structures and same corresponding length of nested arrays.
# # Note: using recursion and zip(), we break the lists into tuples and check the values
# def same_structure_as(original, other):
#     if isinstance(original, list) and isinstance(other, list):
#         if len(original) != len(other):
#             return False
#         return all(same_structure_as(o, e) for o, e in zip(original, other))
#     return not isinstance(original, list) and not isinstance(other, list)

# print(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )) # True
# print(same_structure_as([[[], []]], [[[], []]]))  # True
# print(same_structure_as([[[], []]], [[1, 1]]))  # False

# Write a function called sumIntervals/sum_intervals that accepts an array of intervals, and returns the sum of all the interval lengths.
# Overlapping intervals should only be counted once.
# Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value.
# Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

# def sum_intervals(list_of_intervals):
#     # sort intervals first by starting value, then ending value if the have the same starting value
#     # initialize empty list: merged_intervals
#     # for interval in merged_intervals
#         # if it's empty, or the last num of the last interval in merged_intervals is less than the first num of the current interval:
#             # append current interval
#         # else:
#             # set the last value of the last merged_interval to the max of the last value of the last merged_interval or interval[1]
#         # set total_len var to 0
#         # for start, end in merged_intervals
#             #total_len += end - start
#         # return total_len
#     sorted_intervals = sorted(list_of_intervals, key=lambda x: (x[0], x[1]))

#     merged_intervals = []

#     for interval in sorted_intervals:
#         # convert tuple to list for 'else' step below
#         interval = list(interval)
#         if not merged_intervals or merged_intervals[-1][1] < interval[0]:
#             merged_intervals.append(interval)
#         else:
#             merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
#     total_len = 0
#     for start, end in merged_intervals:
#         total_len += end - start
#     return total_len

# print(sum_intervals([
#    [1, 4],
#    [7, 10],
#    [3, 5]
# ])) # Output: 7
