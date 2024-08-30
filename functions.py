# # With renamed parameter and variables
# def get_color(fav_number):
#     num = str(fav_number + 1)
#     prompt = "What is your #" + num + " fav color? "
#     answer = input(prompt)
#     return answer

# # With renamed variables
# def get_num_colors():
#     response = input("How many fav colors do you have? ")
#     response_num = int(response)
#     return response_num

# print("Hi, I'd like to ask you about your fav colors.")
# num_colors = get_num_colors()
# print("Thanks! I will now ask you for each of those.")
# favorite_colors = []

# for color_number in range(num_colors):
#     color = get_color(color_number)
#     favorite_colors.append(color)

# sorted_colors = sorted(favorite_colors)
# print("Thank you! I have your fav colors as:")
# for color in sorted_colors:
#     print("  ", color)


# def is_too_fast(current_speed, max_speed):
#     if current_speed <= max_speed:
#         return False
#     else:
#         return True

# print(is_too_fast(55, 55))


# def add(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total  # This line changed

# result = add(1, 2, 3, 4)
# print(result)  # We expect 10


# def double_splat(**mystery):
#     print(mystery)

# double_splat()
# double_splat(name="Noor")
# double_splat(first_name="Baz", last_name="Sayid")


# def super_func(*args):
#     return sum(*args)

# print(super_func({1, 2, 3, 4, 5}))


# # Find missing number in list:
# from functools import reduce
# def find_missing_num(nums):
#     # result = sorted(nums)
#     res = reduce(lambda x, y: x if y - x > 1 else y, sorted(nums))
#     return res + 1
# print(find_missing_num([4, 5, 3, 2, 8, 1, 6]))


# # Alternative
# # find min and max, range then return missing num not in other list:
# def find_missing_num(nums):
#     range_nums = list(range(min(nums), max(nums) + 1))
#     result = [i for i in range_nums if i not in nums]
#     return result

# print(find_missing_num([4, 5, 3, 2, 8, 1, 6]))


# # return longest string from list:
# from functools import reduce
# def find_longest(strings):
#     res = reduce(lambda x, y: x if len(x) > len(y) else y, strings)
#     return res
# print(find_longest(['a', 'cat', 'train', 'crocodile', 'pig', 'snake']))


# def find_longest(strings):
#     max_len = -1
#     for ele in strings:
#         if len(ele) > max_len:
#             max_len = len(ele)
#             res = ele
#     return res


# print(find_longest(["a", "bbb", "cc"]))


# Given a person's name and age, "check_age" returns one of two messages:
# Go home, <insert_name_here>!, if they're younger than 21.
# Welcome, <insert_name_here>!, if they're 21 or older.
# Naturally, replace <insert_name_here> with the given name.
# def check_age(name, age):
#     if age < 21:
#         return f'Go home, {name}!'
#     return f'Welcome, {name}!'

# print(check_age('Adrian', 22))


# def make_description(name, attributes):
#     result = name
#     for k, v in attributes.items():
#         result += f", {v} {k}"
#     return result

# print(make_description('lulu', {'hair': 'red', 'eyes': 'blue', 'cape': 'green'}))
# # Output: lulu, red hair, blue eyes, green cape


# reverse the keys and values in a dictionary:
# def reverse_entries(dictionary):
#     d_swap = {v: k for k, v in dictionary.items()}
#     return d_swap

# print(reverse_entries({'hair': 'red', 'eyes': 'blue'}))


# def arg_demo(pos1,pos2, *args, **kwargs):
#     print(f"positional params: {pos1}{pos2}")
#     print('*args')
#     print(args)
#     for arg in args:
#         print(" ", arg)
#     print('**kwargs')
#     print(kwargs)
#     for keyword, value in kwargs.items():
#         print(f'{keyword}: {value}')

# arg_demo('A', 'B', 1, 2, 3, color='purple', shape = 'circle')


# #map:
# #map transforms the items and returns the same num of items
# my_list = [5, 6, 7]

# def mulitply_by_two(item):
#     return item * 2
# print(list(map(mulitply_by_two, my_list)))


# #filter:
# def only_odd(item):
#     return item % 2 != 0

# print(list(filter(only_odd, my_list)))


# #zip:
# your_list = [10, 20, 30]
# print(list(zip(my_list, your_list)))


# #reduce
# from functools import reduce
# #functools = tool belt for functional tools that aren't native to the python installation
# # reduce(action, sequence or data, and initial value)
# # note that we do not prepend this function with list. list is BUILT INTO this one

# new_list = [7, 8, 9]

# def accumulator(acc, item):
#     return (acc + item)

# print(reduce(accumulator, new_list, 0))


# #LAMBDA EXPRESSIONS:
# # lambda in python are one-time anonymous functions that you only need once
# # lambda param: action(param)

# a_list = [7, 8, 9]

# #map:
# # print(list(map(lambda item: item*3, a_list)))

# #reduce:
# print(reduce(lambda acc, item: acc + item, a_list))


# DECORATORS:
# adds juice to another function

# def my_decorator(func):
#     def wrap_func():
#         print('****')
#         func()
#         print('***')
#     return wrap_func

# @my_decorator
# def regilar_function():
#     their_list = [5, 6, 7]
#     print(their_list)

# regilar_function()


# def my_decorator(func):
#     def wrap_func(param):
#         print('************')
#         func(param)
#         print('************')
#     return wrap_func


# @my_decorator
# def hay(name):
#     print(f'hay there! {name}')

# hay("Marcio")


# def yas(num_a):
#     input = [*'Yas!']
#     for i in range(num_a -1):
#         input.insert(1, 'a')
#     return ''.join(input)

# print(yas(5))
# # add in letter 'a' after input[0] until count('a') == num-a


# def new_hope(num_fars):
#     input = "A long time ago in a galaxy far away"
#     sep_input = input.split()
#     first_part = sep_input[:7]
#     last_part = sep_input[-2:]
#     middle_part = []
#     for i in range(num_fars -1):
#         middle_part.append('far,')
#     return ' '.join(first_part + middle_part + last_part)

# print(new_hope(2))


# CUPCAKE PROBLEMS::::
# def profit(num_cupcakes, num_tubes_frosting, tubes_per_cupcake):
#     # use // to return whole nums
#     #set initial profit to 0
#     total = 0
#     #what do we know:
#     frosted_cupcake_price = 10
#     unfrosted_cupcake_price = 4
#     leftover_tube_price = 1
# # calc frosted cupcakes first
#     frosted_cupcakes = min(num_tubes_frosting // tubes_per_cupcake, num_cupcakes)
# # unfrosted cupcakes next
#     unfrosted_cupcakes = num_cupcakes - frosted_cupcakes
# #add totals
#     total += frosted_cupcakes * frosted_cupcake_price
#     total += unfrosted_cupcakes * unfrosted_cupcake_price
#     total += (num_tubes_frosting - (frosted_cupcakes * tubes_per_cupcake)) * leftover_tube_price

#     return total


# print(profit(10, 5, 2))


# #String can only have 31 words
# #Words are defined by a char separated by a space
# #Use split(' ') to split into list
# #count words in list, if <= 30 return True
# # return False
# def count_words(message):
#     cleaned_msg = message.split()
#     return len(cleaned_msg) > 30


# print(count_words("  my     friend  is so c s v b   "))


# def calories(entree_num, side_num, dessert_num, drink_num):
#     sum = 0

#     match entree_num:
#         case 0:
#             sum += 0
#         case 1:
#             sum += 522
#         case 2:
#             sum += 399
#         case 3:
#             sum += 501

#     match side_num:
#         case 0:
#             sum += 0
#         case 1:
#             sum += 130
#         case 2:
#             sum += 125
#         case 3:
#             sum += 72

#     match dessert_num:
#         case 0:
#             sum += 0
#         case 1:
#             sum += 222
#         case 2:
#             sum += 391
#         case 3:
#             sum += 100

#     match drink_num:
#         case 0:
#             sum += 0
#         case 1:
#             sum += 10
#         case 2:
#             sum += 8
#         case 3:
#             sum += 120

#     return sum


# print(calories(0, 0, 0, 3))
# # should = 591


# def skating_day_message(month_num, day_num):
#     if month_num and day_num < 4:
#         return 'World Ice Skating Day is coming up!'
#     elif month_num == 12 and day_num > 4:
#         return "You just missed it. There's another next year!"
#     elif month_num == 12 and day_num == 4:
#         return "YAY! It's World Ice Skating Day!"


# print(skating_day_message(1, 3))


# def sentiment(message):
#     sad = ":-("
#     happy = ":-)"

#     happy_ct = message.count(happy)
#     # print(happy_ct)
#     sad_ct = message.count(sad)
#     # print(sad_ct)

#     if happy_ct > sad_ct: return 'happy'
#     elif sad_ct > happy_ct: return'sad'
#     elif sad_ct == 0 and happy_ct == 0: return 'none'
#     elif sad_ct == happy_ct: return 'unsure'

# #Does not work for special chars:
# # import re
# # Look if stringB is in stringA
#     # match = [re.search(sad, str) for str in message]
#     # match = re.search(ello, message)
#     # if match: print('Yes')


# print(sentiment('hellooo:-(:-(:-(:-:-(:-):-):-(:-):-):-:-:(:-):-)'))


# # count matches in 2 lists:
# a = [1, 2, 3, 4, 5]
# b = [9, 8, 4, 7, 6, 5]
# print(set(a) & set(b))

# # Alternative to count matches in 2 lists:
# a = [1, 2, 3, 4, 5]
# b = [9, 8, 4, 7, 6, 5]
# # list comprehension
# print ([x for x in a if x in b])


# def pizza_satisfaction(pizza_size, cheese_multiplier):
#     if pizza_size >= 12 and cheese_multiplier == 3:
#         return 'maximally satisfied'
#     elif pizza_size >= 10 and cheese_multiplier >= 2:
#         return 'really satisfied'
#     else: return 'very satisfied'

# print(pizza_satisfaction(12, 3))


# Given a phone number as a ten digit number (1234567890, for example),
# complete the function scammer to return the message ignore--
# if the number satisfies all four of the following properties:
# The first digit is a 2 or 4
# The fifth digit is a 2 or 4
# The seventh and eight digits are the same
# The last digit is a 0
# If the phone number does not satisfy all four of those properties, then return accept.

# #INDENTATION IS LIFE
# def scammer(number):
#     num_string = str(number)
#     if num_string[0] == '2' or num_string[0] == '4':
#         print('check1')
#         if num_string[4] == '2' or num_string[4] == '4':
#             print('check2')
#             if num_string[6] == num_string[7]:
#                 print('check3')
#                 if num_string[9] == '0':
#                     print('check4')
#                     return 'ignore'
#     return 'accept'

# # print(scammer(2814257721))

# L = swap the left and middle cards ==\\
# R = swap the right and middle cards
# O = swap the left and right cards, the outside cards

# def monty(swaps):
#     #Q starts in middle
#     #Q can only move +1, -1, or 0
#     #Q range = range(0,4)
#     #return num, convert to Left, Right, Middle
#     Q_value = 1
#     for el in swaps:
#         if el == 'L' and Q_value == 0: Q_value = 1
#         elif el == 'L' and Q_value == 1: Q_value = 0
#         elif el == 'L' and Q_value == 2: Q_value = 1
#         elif el == 'R' and Q_value == 0: Q_value = 1
#         elif el == 'R' and Q_value == 1: Q_value = 2
#         elif el == 'R' and Q_value == 2: Q_value = 1
#         elif el == 'O' and Q_value == 0: Q_value = 2
#         elif el == 'O' and Q_value == 1: Q_value = 1
#         elif el == 'O' and Q_value == 2: Q_value = 0

#     if Q_value == 0: return 'left'
#     elif Q_value == 1: return 'middle'
#     elif Q_value == 2: return 'right'
#     else: return Q_value

# print(monty('LL'))

# # LRORRLOLLLRROOLRORRLOLLLRROOLRORRLOLLLRROOL
# # LRORRLOLLLRROO- middle
# # LRORRLOLLLRROOLRORRLOLLLRROOLRORRLOLLLRROOR


# find matches in 2 lists at same index
# def num_same_spaces(yesterday, today):
#     # compare 2 strings,
#     # return count of matches at matched index
#     count_spaces = 0
#     for i in range(len(yesterday)):
#         if today[i] == 'C' and yesterday[i] == 'C':
#             count_spaces += 1
#     return count_spaces

# print(num_same_spaces('CCEEECCECECECCCCECECCCE', 'CECECECECCEEECCCECECEEC'))


# def cash_on_hand(expenses):
#     #expenses is a list
#     #length of expenses = number of months
#     #expenses length(+1) * 30 = total money (the +1 is to start the next month with)
#     #print balance vailable for next month
#     total_cash = (len(expenses)+1) * 30
#     total_expenses = reduce(lambda a, b: a +b, expenses, 0)
#     return total_cash - total_expenses

# print(cash_on_hand([10, 20, 30, 40, 45]))


# Given an input string password, complete the function valid_password
# to return the string GOOD if it's a valid password, or to return the string BAD if it's an invalid password.

# The criteria for the password are:

# It must be have 8, 9, 10, 11, or 12 characters
# It must have at least two lowercase letters (a … z)
# It must have at least three uppercase letters (A … Z)
# It must have at least two digits (0 … 9)

# def valid_password(password):
#     lower_counter = 0
#     upper_counter = 0
#     num_counter = 0

#     for i in password:
#         if i.islower():
#             lower_counter += 1
#         if i.isupper():
#             upper_counter += 1
#         if i.isnumeric():
#             num_counter += 1

#     # print(lower_counter)
#     # print(num_counter)
#     # print(upper_counter)
#     # print(len(password))

#     if len(password) in range(8, 13):
#         if lower_counter >= 2:
#             if num_counter >= 2:
#                 if upper_counter >= 3:
#                     return 'good'
#     return 'bad'

# print(valid_password('83FSizI'))


# count matches at specific index in 2 lists
# def grade_scantron(submission, answer_key):
#     count = 0
#     for i in range(len(submission)):
#         if submission[i] == answer_key[i]:
#             count += 1
#     return count


# Given a string input text that contains some text in English or German,
# complete the function language so that it returns "German", "English", or "Maybe French?" given the following conditions:

# If the text has more "ei" than "ie" sequences in it, then respond with "German"
# If the text has more "ie" than "ei" sequences in it, then respond with "English"
# If the text has an equal number of "ie" and "ei" sequences in it, then respond with "Maybe French?"

# def language(text):
#     try_text = text.lower()
#     ie_count = try_text.count('ie')
#     ei_count = try_text.count('ei')

#     print(ie_count)
#     print(ei_count)

#     if ie_count > ei_count: return 'English'
#     elif ei_count > ie_count: return 'German'
#     else: return 'Maybe French?'

# print(language('My friend tried to touch the ceiling. \
# Auf ein einziges Abkommen haben sich die Kriegsparteien verständigt: \
# Funktioniert der Getreidedeal? An Bord eines Frachters, der ukrainischen Weizen in die Welt bringt. \
# This is a great day. EIEIO or IEIEO. ieieieieie'))


# Given the input list of button numbers pressed button_pushes,
# complete the function calculate_playlist to figure out the final state of the playlist and
# return the episode labels in a list.

# Button 1: swaps the first two songs of the playlist
# Button 2: moves the first song to the end of the playlist
# Button 3: moves the last song of the playlist to the start of the playlist
# def calculate_playlist(button_pushes):
#     playlist = ["A", "B", "C", "D", "E"]

#     for i in button_pushes:
#         if i == 1:
#             playlist[0], playlist[1] = playlist[1], playlist[0]
#         if i == 2:
#             playlist.append(playlist.pop(0))
#         if i == 3:
#             playlist.insert(0, playlist.pop(len(playlist)-1))

#     return playlist

# print(calculate_playlist([1, 2, 1, 3, 1, 2, 1, 3, 1, 2]))


# eg. FAVE COLOR = GREEN
# 17 seconds to eat all the non-green candy
# 23 seconds to eat the first pieces of green candy
# 23 seconds to eat the second pieces of green candy
# 23 seconds to eat the third pieces of green candy

# def nia_eat(favorite_color, candy):
#     num_fave_candy = candy.count(favorite_color)
#     favorite_candy_time = num_fave_candy * 23
#     if len(candy) > num_fave_candy:
#         favorite_candy_time += 17
#     return favorite_candy_time

# print(nia_eat('blue', ['brown', 'brown', 'brown', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'red', 'red']))


# def half_time_scores(
#     game_length,  # in minutes
#     team_1_score_times,  # each value is seconds
#     team_2_score_times   # each value is seconds
# ):

#     #convert game time:
#         #cut in half, multiply by 60 seconds
#     #count num in team1scoretimes < game_time_seconds
#     #count num in team2scoretimes < game_time_seconds
#     #add both counts, return
#     game_time_seconds = game_length * 60 / 2

#     team_1_scores_filtered = list(filter(lambda i: i < game_time_seconds, team_1_score_times))
#     team_2_scores_filtered = list(filter(lambda a: a < game_time_seconds, team_2_score_times))
#     return len(team_1_scores_filtered) + len(team_2_scores_filtered)


# print(half_time_scores( 1, [1, 5, 10, 33, 45, 50], [2, 3, 4]))


# # Return mode of list:: the numbers that appear the most in a list
# # (should be able to return a list of several nums if there are more than 1 match)
# def mode(numbers):
#     max_count = 0
#     for i in numbers:
#         if numbers.count(numbers[i]) > max_count:
#             max_count = numbers.count(numbers[i])

#     # if any el's have count == max_count and NOT IN result:
#     # add them to a list
#     result = []
#     for i in range(len(numbers)):
#         if numbers[i] not in result:
#             if numbers.count(numbers[i]) == max_count:
#                 result.append(numbers[i])
#     return result

# print (mode([1, 2, 1, 3, 3, 4]))


# Find the runner who registered for the race but did not finish:
# def find_missing_registrant(registrants, finishers):
#     for el in registrants:
#         if el not in finishers:
#             return el

# print(find_missing_registrant(['leo', 'karl', 'eden'], ['eden', 'karl']))


# #List comprehension alternative:
# def find_missing_registrant(registrants, finishers):
#     return [el for el in registrants if el not in finishers]

# print(find_missing_registrant(['leo', 'karl', 'eden'], ['eden', 'karl']))


# def total_song_knowers(num_villagers, attendees_lists):
# # minstrel's list = count num of 0's in attendees_list (obvi we need to loop through) inner lists) to check against at end
# # will have to make lists = num_villagers
# # When 0 is present in attendees list, other villager nums in list get list.append(1)
# # When MINSTREL(0) NOT IN LIST, aka loop through lists, and O not in list : if ANY num in VILLAGER list has len(villager_list) > 0 & OTHER NUMS len(villager_list) == 0, villager_list.append(1)
#     lists = []
#     for i in range(num_villagers):
#         lists.append([])


# # return count of those who know all songs
# print(total_song_knowers(3, [[0, 1], [1, 2, 3], [3, 1, 0]]))
# # #should print: 2


# # Complete the function horizontal_bar_chart below that takes in a string and
# # creates a horizontal bar chart made out of the instances of the letters in that string based on the number of each letter.
# # The return value is a list of the strings of the letters in alphabetical order.
# # For example, given the sentence "abba has a banana", it would return this list of
# # strings because there are seven "a", three "b", one "h", two "n", and one "s" letters in it:

# input: string
# output: list of strings in alphabetical order
# can be based off of count of letters
# create dictionary with each key a unique letter, the values will be accumulated, then returned
# return sorted values of keys in dictionary-- dictionary is prefered because it can only have UNIQUE keys!!!

# def horizontal_bar_chart(sentence):
#     result = {}
#     for el in sentence.replace(" ", ""):
#         if el in result:
#             result[el] += el
#         else:
#             result[el] = el
#     return sorted(result.values())

# print(horizontal_bar_chart("abba has a banana"))

# Alternative: Dictionary comprehension:: use this when we do not want duplicates
# def horizontal_bar_chart(sentence):
#     cleaned = sentence.replace(' ', '')
#     result = {el: el * cleaned.count(el) for el in cleaned}
#     return sorted(result.values())

# print(horizontal_bar_chart("abba has a banana"))


# # Alternative:
# def horizontal_bar_chart(sentence):
#     # make a SET of each letter off the bat: GENIUS. Also: dictionary comprehension
#     byletter = {i for i in sentence}
#     out = []
#     for letter in byletter:
#         if letter == " ": continue
#         j = letter * sentence.count(letter)
#         out.append(j)
#     out.sort()
#     return out

# print(horizontal_bar_chart("abba has a banana"))

# # alternative:
# def horizontal_bar_chart(sentence):
#     result = []
#     cleaned = sentence.replace(' ', '')
#     set_letters = list(set(cleaned))

#     for el in set_letters:
#         i = el * cleaned.count(el)
#         result.append(i)
#     return sorted(result)

# print(horizontal_bar_chart("abba has a banana"))


# # generator comprehension:
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # generator:
# mygen = (element ** 2 for element in myList if element % 2 == 0)
# print("Elements obtained from the generator are:")
# for ele in mygen:
#     print(ele)


# # Another generator comprehension:
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # assign generator to a variable as a tuple:
# newTuple = tuple((el * el for el in myList))
# print (newTuple)


# TEST Q'S::::::

# def partition(list, size):
#     chunks = []
#     in_progress = []
#     for item in list:
#         if len(in_progress) == size:
#             chunks.append(in_progress)
#             in_progress = []
#         in_progress.append(item)
#     return chunks

# input = [0, 1, 2, 3, 4, 5, 6]

# result = partition(input, 2)
# print(result)


# def count_matches(items, param2=None):
#     matches = []
#     for item in items:
#         if(item.get("color") == param2):
#             matches.append(item)
#     return len(matches)

# input = [
#     {"background": "green",  "size": 5,  "color": "blue"},
#     {"background": "yellow", "size": 5,  "color": "green"},
#     {"background": "blue",   "size": 25, "color": "green"},
#     {"background": "yellow", "size": 5,  "weight": "light"},
# ]

# result = count_matches(input)
# print(result)


# def divide_bill(bill, num_diners, tip):
#     # your code here
#     total = bill * (1 + tip)
#     return total / num_diners

# print(divide_bill(100, 4, 0.1))


# def c_to_f(degrees_celsius):
#     # your code here
#     f = (degrees_celsius * (9/5)) + 32
#     return f

# print(c_to_f(100))


# def find_shipment_weight(shipment):
#     # your code here
#     total = 0
#     for item in shipment:
#         weight = item.get('product_weight_pounds')
#         quant = item.get('quantity')
#         total += weight * quant
#     return total


# print(find_shipment_weight(
#     shipment = [
#     {
#         "product_name": "beans",
#         "product_weight_pounds": 2,
#         "quantity": 5,
#     },
#     {
#         "product_name": "rice",
#         "product_weight_pounds": 1.5,
#         "quantity": 7,
#     },
# ]))

# Return longest string in list
# def find_longest(strings):
#     # your code here
#     longest = -1
#     for el in strings:
#         if len(el) > longest:
#             longest = len(el)
#             res = el
#     return res

# print(find_longest(['a', 'cat', 'train', 'crocodile', 'pig', 'snake']))

# # Alternative, best: Look at the second arg of the max function!!!!
# def find_longest(strings):
#     res = max(strings, key = len)
#     return res

# print(find_longest(['a', 'cat', 'train', 'crocodile', 'pig', 'snake']))


# # This function returns True if number is an integer multiple of base where number and base are both integers.
# # If number is an integer multiple of base, then number/base is an integer.
# # Here are some examples:
# def is_multiple_of(number, base):
#     # your code here
#     if int(number) == number:
#         if int(base) == base:
#             if number % base == 0:
#                 return True
#     return False


# print(is_multiple_of(6, 2))


# def shift_cipher(message, shift):
#     # your code here
#     result = ''
#     for letter in message:
#         value = ord(letter) + shift
#         letter = chr(value)
#         result += letter
#     return result

# print(shift_cipher('Raining-Frogs', -10))


# def read_delimited(line, separator):
#     # your code here
#     if line == '':
#         return ['']
#     cleaned = line.replace(separator, ' ')
#     return cleaned.split()

# print(read_delimited("bat##cat##rat", "##"))

# Alternative, better:
# def read_delimited(line, separator):
#     return line.split(separator)

# print(read_delimited("bat##cat##rat", "##"))


# # Return lists of specific length
# def pair_up(items):
#     result = []
#     temp = []
#     for item in items:
#         temp.append(item)
#         if len(temp) == 2:
#             result.append(temp)
#             temp = []
#     return result

# print(pair_up([1, 2, 3, 4, 5]))
# output: [[1,2], [3, 4]]


# # Alternative: return lists of specific length
# def pair_up(items):
#     result = []
#     for i in range(0, len(items), 2):
#         if i + 1 < len(items):
#             pair = [items[i], items[i + 1]]
#             result.append(pair)
#     return result

# print(pair_up([1, 2, 3, 4, 5]))

# # Another alternative, interesting approach: return lists of specific length
# def pair_up(items):
#     result = []
#     for i in range(len(items)):
#         if i + 1 != len(items) and (i ==0 or i % 2 ==0):
#             result.append([items[i], items[i + 1]])
#     return result

# print(pair_up([1, 2, 3, 4, 5]))

# # Cool alternative:
# def pair_up(items):
#     pairs = []
#     # Loop through the indexes of the items
#     for index, item in enumerate(items):
#         # If the index + 1 is less than the length
#         # if the index is even
#         if index % 2 == 0:
#             if index + 1 < len(items):
#                 # Make a pair
#                 pair = [items[index], items[index + 1]]
#                 # Append the pair
#                 pairs.append(pair)
#     return pairs
# print(pair_up([1, 2, 3, 4, 5]))


# # Join strings with separator in between
# def join_strings(strings, separator):
#     if strings == []:
#         return ''
#     return separator.join(strings)

# print(join_strings(["hello", " world"], ","))
# # output: "hello, world"

# # Do the same as above but with for loop:
# def join_strings(strings, separator=""):
#     # your code here
#     if len(strings) == 0:
#         return ""
#     output = strings[0]
#     for string in strings[1:]:
#         output += separator + string
#     return output

# print(join_strings(["aaa", "bbb", "ccc"], "--"))


# def unique_elements(items):
#     # your code here
#     res = []
#     for el in items:
#         if el not in res:
#             res.append(el)
#     return res

# print(unique_elements(["a", 1, "B", "a", 2, 1, "a"]))


# # Better alternative:
# def unique_elements(items):
#     # your code here
#     uniques = {}                  #-hide
#     for item in items:            #-hide
#         uniques[item] = 1         #-hide
#     return list(uniques.keys())
# print(unique_elements(["a", 1, "B", "a", 2, 1, "a"]))


# # Best performant alternative -- look into this. 'visited dictionary'
# def unique_elements(items):
#     output = []
#     visited = {}
#     for i in items:
#         if visited.get(i)== None:
#             output.append(i)
#         visited[i] = True

# print(unique_elements(["a", 1, "B", "a", 2, 1, "a"]))


# def mean(numbers):
#     try:
#         total = sum(numbers)
#         return  total / len(numbers)
#     except ZeroDivisionError as error:
#         return float("nan")

# print(mean(['EFF']))


# # This works, but I missed it on the test:
# def join(items):
#     result = ""
#     for item in items:
#         result += str(item)
#     return result

# print(join(["l", 3, 3, 7]))


# # Given a list of numbers numbers, complete the function mode that
# # returns a list of all of the modes of the list of numbers.
# # The list of numbers will always have at least one number in it.
# # input: list of nums
# # output: list of nums
# # First wave: create new dict with keys and value pairs.
# # Values are counts of occurrences of the keys in the numbers list
# # Second wave: go thru created dict and if values = max_count then push key to list
# # Return list of keys

# def mode(numbers):
#     # create empty list to return
#     res = []
#     # create empty dict to add key values to
#     counts = {}
#     # establish max_count as 0
#     max_count = 0
#     # iterate through numbers list
#     for num in numbers:
#         # if number not in empty dict:
#         if num not in counts:
#             # add num with a value of 0. (So we can increment it)
#             counts[num] = 0
#         # if num in list: add 1 to its value
#         counts[num] += 1
#         # if the value of the key in the list (aka count) > max_count:
#         if counts[num] > max_count:
#             # update max_count
#             max_count = counts[num]

#     for key, value in counts.items():
#         if value == max_count:
#             res.append(key)
#     return res

# print(mode([9, 2, 9, 6, 8, 2, 1, 2, 9, 6]))

# # Alternative:
# # Create a set from numbers
# # iterate through range(len(numbers))
# # set key[num] = count(num) in the set
# # return the keys that have the largest values


# def find_shortest(lists):
#     # your code here
#     min_len = len(lists[0])
#     for item in lists:
#         if len(item) <= min_len:
#             res = item
#     return res

# print(find_shortest([[1, 2, 3], [3, 2], [1, 2, 11, 200]]))


# from functools import reduce
# def find_shortest(lists):
#     # your code here
#     return reduce(lambda x, y: x if len(x) < len(y) else y, lists)

# print(find_shortest([[1, 2, 3], [3, 2], [1, 2, 11, 200]]))


# # Alternative, using index. Good practice, not best approach
# def find_shortest(lists):
#     if lists:
#         shortest = lists[0]
#         for index in range(len(lists)):
#             if len(lists[index]) < len(shortest):
#                 shortest = lists[index]
#         return shortest

# print(find_shortest([[1, 2, 3], [3, 2], [1, 2, 11, 200]]))

# Alternative, best: Look at the second arg of the MIN function!!!!
# def find_shortest(strings):
#     res = min(strings, key = len)
#     return res

# print(find_shortest([[1, 2, 3], [3, 2], [1, 2, 11, 200]]))


# # Write a function that returns a string in which firstname is swapped with last name.
# # Example(Input --> Output)
# # "john McClane" --> "McClane john"
# def name_shuffler(str):
#     res = ''
#     x = str.split()
#     return f'{x[1]} {x[0]}'

# print(name_shuffler('john McClane'))


# # Write a function that takes in a string of one or more words, and
# # returns the same string, but with all five or more letter words reversed
# #  Strings passed in will consist of only letters and spaces.
# # Spaces will be included only when more than one word is present.
# def spinWords(str):
#     temp = []
#     split_str = str.split()
#     for word in split_str:
#         if len(word) >= 5:
#             word = word[::-1]
#         temp.append(word)
#     result = ' '.join(temp)
#     return result

# print(spinWords("This is another test"))
# # output: This is rehtona test


# # implement a difference function, which subtracts one list from another and returns the result.
# # It should remove all values from list A, which are present in list B keeping their order.
# def array_diff(list1, list2):
#     result = []
#     for item in list1:
#         if item not in list2:
#             result.append(item)
#     return result

# print(array_diff([1,2,2,2,3],[2]))


# # # return all the multiples of integer upto and including limit
# def find_multiples(integer, limit):
#     res = []
#     for i in range(integer, limit + 1, integer):
#         res.append(i)
#     return res

# print(find_multiples(2, 11))

# # OR: while statement:
# def find_multiples(integer, limit):
#     res = []
#     i = integer
#     while i <= limit:
#         res.append(i)
#         i += integer
#     return res

# print(find_multiples(2, 11))


# Given a text, count the frequency of each word and store the results in a dictionary
# text = "this is a simple text text example"
# split_text = text.split(" ")
# word_count = {}
# for word in split_text:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print(word_count)

# #Alternative:
# text = "this is a simple text text example"
# split_text = text.split(' ')
# word_count = {}
# for word in split_text:
#    word_count.update({word: split_text.count(word)})
# print(word_count)


# # Given a list of numbers in a specific range, find the missing numbers within that range
# # expected output: [4, 6, 7]
# num_list = [3, 5, 8, 9, 10]
# missing_nums = []
# for num in range(min(num_list), max(num_list)):
#     if num not in num_list:
#         missing_nums.append(num)
# print(missing_nums)


# # Given a sorted list, remove the duplicates in-place such that each element appears only once and return the new length
# # expected output: [1, 2, 3, 4, 5]
# sorted_list = [1, 1, 2, 3, 3, 3, 4, 5, 5]
# for num in sorted_list:
#     if sorted_list.count(num) > 1:
#         sorted_list.remove(num)
# print(sorted_list, len(sorted_list))


# # Rotate list by k steps
# # output: [4, 5, 1, 2, 3]
# numbers = [1, 2, 3, 4, 5]
# k= 2
# print(numbers[-k:] + numbers[:-k])

# Alternative:
# numbers = [1, 2, 3, 4, 5]
# k= 2
# for count in range(k):
#     numbers.insert(0, numbers.pop())
# print(numbers)


# # Find the longest sublist with consecutive elements
# Output: [1, 2, 3, 4]
# def sublist(items):
#     items.sort()
#     longest = []
#     for i in range(len(items)):
#         j = 0
#         for j in range(i + 1, len(items)):
#             if items[j] - 1 != items[j - 1]: break
#         if j - i > len(longest):
#             longest = items[i: j]
#     return longest

# print(sublist([1, 9, 3, 10, 4, 20, 2]))


# def count_fries(items, match):
#     matches = []
#     for item in items:
#         if(item.get("fries") == match):
#             matches.append(item)
#     return len(matches)

# orders = [
#     {"burger": "veggie", "fries": "sweet potato", "drink": "cola" },
#     {"burger": "classic", "fries": "curly", "drink": "juice"},
#     {"burger": "chicken", "drink": "tea" },
#     {"burger": "impossible", "drink": "water"},
#     {"burger": "salmon", "drink": "juice"}
# ]

# result = count_fries(orders, None)
# print(result)


# add num to list based on condition
# def foo(list, num):
#     lows = []
#     sum = 0
#     for item in list:
#         if item < num:
#             sum += item
#         lows.append(sum)
#     return lows

# input = [10, 7, 3, 11, 4]

# result = foo(input, 10)
# print(result)


# # take a string, convert each letter to numeric value, add together then return value and convert to char
# def checksum(message):
#     sum = 0
#     for letter in message:
#         letter = ord(letter)
#         sum += letter
#     mod_sum = sum % 26 + 97
#     final = chr(mod_sum)
#     return final

# print(checksum("bat"))
# Output: 'z'


# # find longest run of identical letters in string
# def longest_run(string):
#     current_count = 1
#     top_count = 0
#     current_start = 0
#     top_start = 0
#     top_end = 0

#     for index in range(1, len(string)):
#         if (string[index] == string[index - 1]):
#             current_count += 1

#         else:
#             current_count = 1
#             current_start = index

#         if (current_count > top_count):
#             top_count = current_count
#             top_start = current_start
#             top_end = index

#     return string[top_start:top_end +1]

# print(longest_run('baabbbbcc'))


# def wave(people):
#     wave = []

#     for i in range(len(people)):
#         if people[i] == " ":
#             continue
#         else:
#             # first slice: grab everything before i
#             # second slice: grab i and uppercase it
#             # third slice: grab everything after i
#             waved_word = f'{people[:i]}{people[i].upper()}{people[i+1:]}'
#             wave.append(waved_word)
#     return wave

# print(wave("hello"))
#  # Ouput: ["Hello", "hEllo", "heLlo", "helLo", "hellO"]


# # Bubble Sort:
# # COMMENT OUT WHAT ALL IS HAPPENING HERE:!!!
# def sort(items):
#     # while swapping is happening:
#     while True:
#             # set swapped to False as default so it must be updated every time it's used
#         swapped = False
#         # loop thru range EXCEPT FOR LAST INDEX
#         for i in range(len(items) - 1):
#             # if the num at lower index is greater than num at index +1:
#             if items[i] > items[i+1]:
#                 # update swapped status to True
#                 swapped = True
#                 # swap the items
#                 (items[i], items[i+1]) = (items[i+1], items[i])
#         # break out of loop if there are no more items to swap
#         if not swapped:
#             break
#         # return items
#     return items

# print(sort([5, 4, 3, 2, 1, 19]))


# # Alt:
# def sort(items):
#     while True:
#         swapped = False
#         for i in range(len(items) -1):
#             if items[i] > items[i +1]:
#                 temp = items[i]
#                 items[i] = items[i +1]
#                 items[i +1] = temp
#                 swapped = True
#         if not swapped:
#             break
#     return items

# print(sort([5, 4, 3, 2, 1, 19]))


# def bubble_down(items):
#     for i in range(len(items) -1, 0, -1):
#         if items[i] < items[i - 1]:
#             (items[i], items[i - 1]) = (items[i - 1], items[i])
#     return items

# print(bubble_down([4,3,2,1]))


# # Cocktail sort:
# def cocktail_sort(items):
#     while True:
#         made_a_swap = False

#         for i in range(len(items) -1):
#             if items[i] > items[i + 1]:
#                 made_a_swap = True
#                 (items[i], items[i +1]) = (items[i + 1], items[i])

#         if not made_a_swap:
#             break

#         for i in range(len(items) -1, 0, -1):
#             if items[i] < items[i - 1]:
#                 made_a_swap = True
#                 (items[i], items[i -1]) = (items[i -1], items[i])

#         if not made_a_swap:
#             break

#     return items

# print(cocktail_sort([4, 1, 3, 2]))


# Merge 2 lists::::
# Opt. 1: EASY, apparently not most PERFORMANT:
# def merge_sorted_lists(list1, list2):
# return sorted(list1 + list2)
# print(merge_sorted_lists([13, 14, 54, 7], [98, 786, 17]))

# This DOESn't WORK::: FIX IT
# def merge_sorted_lists(list1, list2):
#     combined = []
#     while len(list1) > 0 or len(list2) > 0:
#         if len(list1) > 0 and len(list2) > 0:
#             if list1[0] < list2[0]:
#                 combined.append(list1[0])
#                 list1.pop(0)
#             else:
#                 combined.append(list2[0])
#                 list2.pop(0)
#         elif len(list1) > 0:
#             combined.extend(list1)
#             list1 = []
#         else:
#             len(list2) > 0
#             combined.extend(list2)
#             list2 = []
#     return combined
# print(merge_sorted_lists([13, 14, 54, 7], [98, 786, 17]))


# BINARY SEARCH:::
# def binary_search(items, target):
#     start = 0
#     end = len(items) -1
#     while start <= end:
#         half = (start + end) // 2
#         value = items[half]
#         if target == value:
#             return value
#         elif target < value:
#             end = half -1
#         else:
#             start = half +1
#     return None

# print(binary_search([2, 3, 5, 6, 9, 13, 167], 3))


# Recursion
# def my_factorial(n):

#     # base case
#     if n == 1:
#         return 1

#     else:
#         # recursive case
#         return n * my_factorial(n - 1)

# print(my_factorial(5))


# # More recursion:
# def triangular(n):
#     if n == 0:
#         return 0
#     else:
#         return n + triangular(n - 1)

# print(triangular(5))
# # Output: 15


# def count_letters(string):
#     word = 'HACK'
#     index = 0
#     count = 0
#     for char in string:
#         if char == word[index]:
#             index +=1
#             if index == len(word):
#                 count += 1
#                 index = 0
#     return count

# print(count_letters("HHHAAACCCKKK"))


# # Return only the words friom the given array that can ALL be typed on one
# #  row of the american keyboard
# def keyboard_words(words):
#     rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
#     result = []

#     for word in words:
#         lower = word.lower()
#         word_in_row = False

#         for row in rows:
#             if all(letter in row for letter in lower):
#                 word_in_row = True
#                 break
#         if word_in_row:
#             result.append(word)
#     return result


# print(
#     keyboard_words(["hello", "world", "AlAska", "test", "cat", "dog", "port", "people"])
# )


# # return index of minimum value in a list of lists:
# def find_lists_with_minimum_value(lists):
#     result = []
#     min_value = min([item for sublist in lists for item in sublist])

#     for i in range(len(lists)):
#         if min_value in lists[i]:
#             result.append(i)
#     return result


# print(
#     find_lists_with_minimum_value(
#         [[13, 111, 12, 64, 5], [19, 22, 333, 14], [434, 44, 45, 16]]
#     )
# )


# # return the (sorted) common numbers that occur in all sub-lists:
# def intersection(nums):
#     result = set(nums[0])
#     for l in nums[1:]:
#         result = result.intersection(set(l))
#     return list(sorted(result))


# print(intersection([[13, 111, 12, 5], [19, 22, 13, 14], [44, 45, 13, 16]]))


# # Alternative:
# def intersection(nums):
#     # use intersection and list comp to find a set of common nums
#     target = set.intersection(*[set(el) for el in nums[1:]])
#     # test set of common nums against first list and return dupes
#     return [n for n in nums[0] if n in target]
# print(intersection([[13, 111, 12, 5], [19, 22, 13, 14], [44, 45, 13, 16]]))


# SELECTION SORT:
# def selection_sort(items):
#     length = len(items)
#     for start in range(length-1):
#         min_idx = start
#         min_val = items[start]
#         for i in range(start+1, length):
#             if items[i] < min_val:
#                 min_idx = i
#                 min_val = items[i]
#         if min_idx > start:
#             items[start], items[min_idx] = items[min_idx], items[start]
#     return items


# # MERGE SORT:
# def mergeSort(array):
#     if len(array) > 1:

#         #  middle is the point where the array is divided into two subarrays
#         middle = len(array)//2
#         left = array[:middle]
#         right = array[middle:]

#         # Sort the two halves
#         mergeSort(left)
#         mergeSort(right)

#         i = j = k = 0

#         # Until we reach either end of either left or right, pick larger among
#         # elements left and right and place them in the correct position at A[p..r]
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         # When we run out of elements in either left or right,
#         # pick up the remaining elements and put in A[p..r]
#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1


# # reverse letters in a string:
# def revert(str):
#     result = ""
#     for i in range(len(str) - 1, -1, -1):
#         result += str[i]
#     return result

# print(revert("string"))


# # reverse items in array:
# def rev_list(list1):
#     result = []
#     for el in range(len(list1) - 1, -1, -1):
#         result.append(list1[el])
#     return result
# print(rev_list([1, 2, 3, 4, 5, 6]))

# # alternative:
# def rev_list(list1):
#     result = list1[::-1]
#     return result
# print(rev_list([1, 2, 3, 4, 5, 6]))


# write a fn that takes a str as input and returns a string reversed
# edge case: string can be empty
# def rev_str(string1):
#     if len(string1) == 0:
#         return "invalid input"
#     result = ""
#     for i in range(len(string1) - 1, -1, -1):
#         result += string1[i]
#     return result


# print(rev_str("party"))


# # alternative:
# def rev_str(string1):
#     # slice method
#     return string1[::-1]


# print(rev_str("party"))


# camel case the snake case words, keeping leading and trailing underscores intact
# import re
# def transform_word(word):
#     leading = re.match(r'^_+', word)
#     trailing = re.search(r'_+$', word)

#     leading = leading.group() if leading else ''
#     trailing = trailing.group() if trailing else ''

#     new_word = word.strip('_')

#     parts = new_word.split('_')
#     print(parts)

#     if len(parts) > 1:
#         parts[1] = parts[1].capitalize()
#     else:
#         parts.append('')

#     result = leading + parts[0] + parts[1] + trailing
#     return result


# def process_str(str):
#     split_str = str.split(' ')
#     result = []
#     for word in split_str:
#         if '_' in word:
#             result.append(transform_word(word))
#         else:
#             result.append(word)
#     return ' '.join(result)


# print(process_str('Hieee whoo __latvia chocolate dip_flip __butter_fly__'))
# # # Output: 'Hieee whoo __latvia chocolate dipFlip __butterFly__'


# The following string must meet the conditions below to be alphanumeric:
# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore

# import re

# def alphanumeric(password):
#     pattern = r'^[A-Za-z0-9]+$'
#     return bool(re.match(pattern, password))

# Alternative:
# def alphanumeric(password):
#     return password.isalnum() # look this up. god bless python.


# import re

# def transform_word(word):
#     # Preserve the leading and trailing underscores
#     leading_underscores = re.match(r'^_*', word)
#     trailing_underscores = re.search(r'_+$', word)

#     leading_underscores = leading_underscores.group() if leading_underscores else ''
#     trailing_underscores = trailing_underscores.group() if trailing_underscores else ''

#     # Remove the leading and trailing underscores for processing
#     core_word = word.strip('_')

#     # Split the word at the underscore
#     parts = core_word.split('_')

#     # Capitalize the second part if it exists
#     if len(parts) > 1:
#         parts[1] = parts[1].capitalize()

#     # Join the parts back together
#     new_core_word = parts[0] + ''.join(parts[1:])

#     # Add the leading and trailing underscores back
#     new_word = leading_underscores + new_core_word + trailing_underscores

#     return new_word

# def solution(src):
#     split_src = src.split(' ')
#     result = []
#     for word in split_src:
#         if '_' in word:
#             result.append(transform_word(word))
#         else:
#             result.append(word)
#     return ' '.join(result)

# # Test the function
# print(solution("This is the doc_string for __secret_fun"))  # Expected: This is the docString for __secretFun


# # Write a function that when given a URL as a string,
# # parses out just the domain name and returns it as a string.
# def domain_name(url):
#     if "://" in url:
#         url = url.split("://")[1]

#     if url.startswith('www.'):
#         url = url[4:]

#     last_index = url.find('.')

#     return url[:last_index]


# print(domain_name("http://github.com/carbonfive/raygun"))
# print(domain_name("http://www.zombie-bites.ru"))
# print(domain_name("https://www.cnet.com"))


# # Alternative:
# def domain_name(url):
#     return url.split("//")[-1].split("www.")[-1].split(".")[0]
# print(domain_name("http://github.com/carbonfive/raygun"))
# print(domain_name("http://www.zombie-bites.ru"))
# print(domain_name("https://www.cnet.com"))


# # convert num to binary:
# # Manual conversion with bitwise operations
# def convert_to_bitwise_string(num):
#     binary_string = ''
#     while num > 0:
#         binary_string = str(num % 2) + binary_string
#         num //= 2
#     # Handle the case when num is 0
#     binary_result = binary_string if binary_string else '0'
#     return binary_result

# print(convert_to_bitwise_string(2149583361))


# # convert binary string to ip address:
# def int32_to_ip(int32):
#     bin_str = format(int32, 'b')
#     temp_list = []
#     for i in range(0, len(bin_str), 8):
#         temp_list.append(bin_str[i: i + 8])
#     ip_address = ''
#     for el in temp_list:
#         el = int(el, 2)
#         ip_address += str(el) + '.'
#     return ip_address[:-1]

# print(int32_to_ip(2127875623))

# # Alternative:
# def int32_to_ip(int32):
#     if int32 == 0:
#         return '0.0.0.0'
#     bin_str = format(int32, '032b')
#     ip_address = '.'.join(str(int(bin_str[i:i+8], 2)) for i in range(0, len(bin_str), 8))
#     return ip_address

# print(int32_to_ip(2127875623))

# Find all integers between m and n (m and n integers with 1 <= m <= n)
# such that the sum of their squared divisors is itself a square.
# This works, but is not performant:
# import math
# def list_squared(m, n):
#     result = []
#     for i in range(m, n + 1):
#         divisors = [num for num in range(1, i + 1) if i % num == 0]
#         summed_squares = sum([num**2 for num in divisors])

#         if math.isqrt(summed_squares) ** 2 == summed_squares:
#             result.append([i, summed_squares])
#     return result

# print(list_squared(1, 250))

# # Alternative: This works, but produces a Max Buffer Size Reached (1.5 MiB). (Not optimized)
# import math
# def list_squared(m, n):
#     result = []
#     for i in range(m, n + 1):
#         divisors = set()
#         # Iterate up to the square root of i
#         for d in range(1, int(math.isqrt(i)) + 1):
#             if i % d == 0:
#                 divisors.add(d)
#                 divisors.add(i // d)
#                 print(list(divisors))
#         # Sum the squares of the divisors
#         summed_squares = sum(d ** 2 for d in divisors)
#         # Check if the sum of squares is a perfect square
#         if math.isqrt(summed_squares) ** 2 == summed_squares:
#             result.append([i, summed_squares])

#     return result

# print(list_squared(1, 250))

# # Better alternative:
# import math

# def list_squared(m, n):
#     result = []
#     for i in range(m, n + 1):
#         sum_of_squares = 0
#         for j in range(1, int(math.sqrt(i)) + 1):
#             if i % j == 0:
#                 sum_of_squares += j * j
#                 if j != i // j:
#                     sum_of_squares += (i // j) * (i // j)

#         if math.isqrt(sum_of_squares) ** 2 == sum_of_squares:
#             result.append([i, sum_of_squares])
#     return result

# print(list_squared(1, 250))

# Viable Alternative 2:
# def list_squared(m, n):
#     out = []
#     for i in range(m, n + 1):
#         # Finding all divisors below the square root of i
#         possibles = set([x for x in range(1, int(i**0.5) + 1) if i % x == 0])
#         # And adding their counterpart
#         possibles.update([i / x for x in possibles])
#         # Doubles in the possibles are solved due to the set
#         val = sum(x ** 2 for x in possibles)
#         # Checking for exact square
#         if (int(val ** 0.5)) ** 2 == val:
#             out.append([i, int(val)])
#     return out
# print(list_squared(1, 250))

# Produce all combinations of numbers for a pin based on observing someone enter them in a keypad ([123] on row 1, [456] on row 2, [789] on row 3, and 0 directly onder the 8 on row 4)
# Each of the digits could actually be another adjacent digit (horizontally or vertically, but not diagonally).
# E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.
# from itertools import product
# def get_pins(observed):
#     adjacent = {
#         '1': ['1', '2', '4'],
#         '2': ['2', '3', '1', '5'],
#         '3': ['3', '6', '2'],
#         '4': ['4', '5', '7', '1'],
#         '5': ['5', '8', '4', '6', '2'],
#         '6': ['6', '9', '3', '5'],
#         '7': ['7', '8', '4'],
#         '8': ['8', '7', '9', '5', '0'],
#         '9': ['9', '8', '6'],
#         '0': ['0', '8'],
#     }

#     possible_combos = product(*(adjacent[digit] for digit in observed))
#     return [''.join(p) for p in possible_combos]

# print(get_pins('11'))

# Sort of alternative:
# from itertools import product
# def get_pins(observed):
#     ADJACENTS = ['08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968']
#     return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
# print(get_pins('11'))
