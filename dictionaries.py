Python containers
lists [] - mutable
tuples () - immutable
dictionaries {} - mutable, they keep the order of INSERTION, but are not ordered



codes_and_cities = {
    "LAX": "Los Angeles",
    "LGA": "New York City",
    "IAH": "Houston",
    "BOI": "Boise",
    "SEA": "Seattle",
    "GSP": "Greenville"
}

code = input("What's the airport code? ")

# This will return None if the key does not exist
city = codes_and_cities.get(code)
print(city)

OR:

# This will cause an error if the value in code
# is not a key in the dictionary, like "BOO"
city = codes_and_cities[code]
print(city)


That's how you get values out of a dictionary.
You use either the get method of the dictionary,
in case the key may not exist (if you don't want an error),
or square bracket notation (if you don't care about the error or the key is guaranteed to exist).

## Adding to a Dictionary:
codes_and_cities = {
    "LAX": "Los Angeles",
    "LGA": "New York City",
    "IAH": "Houston",
    "BOI": "Boise",
    "SEA": "Seattle",
    "GSP": "Greenville",
}

print(len(codes_and_cities))

# Add Flagstaff with the airport code FLG
codes_and_cities["FLG"] = "Flagstaff"
# print(codes_and_cities.get("FLG"))
print(codes_and_cities)

# Remove Houston
del codes_and_cities["IAH"]
print(codes_and_cities.get("IAH", "NOTHING!"))

# Ask the human to provide a code and city
# and store those.
code = input("Please gimme an airport code. ")
city = input("Please tell me what city that's in. ")
codes_and_cities[code] = city


# Add multiple new entries:
wants_six_entries = {
    "crew": "t-shirt",
    "mock": "turtle neck",
    "khakis": "pants",
    "ankle": "socks",
}

new_data = {"Turtle" : 'animal', 'python' :'language'}
wants_six_entries.update(new_data)
print(wants_six_entries)



numbers_to_words = {
  1: "one",
  2: "two",
  3: "three",
}

for initial_key in numbers_to_words:
    print("The key is key:", initial_key)

    # # Use the key to get the value from
    # # the dictionary
    value = numbers_to_words[initial_key]
    print("The associated value is:", value)



adventurer = {
    'name': 'Timothy',
    'hitPoints' : 10,
    'belongings': ['Sword', 'magic potion', 'tums', 'water bottle'],
    'companion': {
        'name': 'Velma',
        'type': 'bat',
        'companion': {
          'name': 'Tim',
          'type': 'parasite',
          'belongings': ['scuba tank', 'ipod', 'health insurance']
        }
    }
}

print(adventurer)
print(adventurer['name'])
print(adventurer.keys())
print(adventurer.values())

# .get - access a value AND allows you to give a default msg when the value does not exist
print(adventurer.get('vehicle', 'This key does not exist!'))

#find items in dictionaries:
companion_belongings = adventurer['companion']['companion']['belongings']

for item in companion_belongings:
    print(item)

#add to dictionaries
adventurer['love'] = 'level 1'
print(adventurer)

#remove items:
# pop(key) - takes argument - remove specific key value pair
# popitem() - remove item last item you added to dictionary

adventurer.pop('love')
print(adventurer)

adventurer.popitem()
print(adventurer)

setdefault() - can be used when you want to have a placeholder key and the value will be updated later-- look this up
https://www.programiz.com/python-programming/methods/dictionary/setdefault


keys() - return keys
values() - return values
items() - return key value pairs


# update() - is useful to merge dictionaries, or add kv pairs using an iterable
party = {
    'people': 'are hurr',
    'drinkies': 'no drinks'
}
animals = {
  'burrito': 'burr',
  'shoes': 'dunks'
}
party.update(animals)
print(party)


# looping through dictionaries:
for kv in party.items():
    print(kv)

#alternative:
for key, value in party.items():
  print(key)
  print(value)


#exercise:
# Convert 2 lists to dictionaries:
list1 = ['ten', 'twenty', 'thirty']
list2 = [10,20,30]

output = dict()
for i in range(len(list1)):
   output.update({list1[i]: list2[i]})
print(output)

#or:
output = dict(zip(list1,list2))
print(output)


Practice Problems:

Problem 1
Assign the following dictionary to a variable.
continents = {
  "Asia":["China", "Mongolia", "India"],
  "South America": ["Brazil", "Argentina", "Chile"],
  "North America": ["United States", "Canada", "Mexico"], "Antarctica": [],
  "Africa": ["South Africa", "Algeria", "Kenya", "Ethiopia", "Egypt"],
  "Europe": ["France", "Germany", "England", "Spain", "Greece", "Italy"],
  "Australia": ["New Zealand", "Australia", "Fiji"]
  }

# Task: Use the dictionary to print the value of "Asia"
print(continents["Asia"])

# Task: use the dictionary to print the third item in the value of "Australia"
print(continents["Australia"][2])

# Task: print a list of all the keys, in alphabetical order
print(sorted(continents.keys()))



Problem 2
Assign the following dictionary to a variable:

identity = { "first_name": "Wally",
  "last_name": "McCrea",
  "years_experience": 4,
  "role": "graphic designer"
}

# Use the dictionary keys and string interpolation to print out this string:
# "The candidate, Wally McCrea has 4 years of experience as a graphic designer."
print(f"The candidate, {identity['first_name']} {identity['last_name']} has {identity['years_experience']} years of experience as a {identity['role']}.")




# Problem 3
# Consider the following dictionary:
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Task: Loop through the dictionary and create a new one where the values are
the squares of the current values. Print the new dictionary.
new_dict = my_dict.copy()
for key in new_dict:
    new_dict[key] *= new_dict[key]
print(new_dict)


# print a dictionary where the keys are the squares of the values and the values are the keys.
new_dict = my_dict.copy()
for key in new_dict:
    new_dict[key] *= new_dict[key]

## convert old values to list of keys
new_keys_list = list(new_dict.values())

## convert old keys to list of values
new_values_list = list(new_dict.keys())

## zip 2 lists together as a dict
print(dict(zip(new_keys_list, new_values_list)))


def find_item(dict1, dict2):
    result = {}
    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            result[key] = dict1[key]
    return result

print(find_item({'a': 1, 'b':2, 'c':3}, {'b': 2, 'c':4, 'd': 5}))

# # output: {'b': 2}



# return sum of dict values
from functools import reduce
def find_item(dict1):
    # create list of values
    vals = dict1.values()
    return reduce(lambda a, b: a + b, vals)

print(find_item({'a': 1, 'b': 2, 'c': 3}))
# output: 6

# return a joined string containing only the keys of a dictionary:
def key_str(dict1):
    return ''.join(dict1.keys())

print(key_str({'h': 2, 'e': 54, 'l': 9, 'p': -7}))
output: help



Given a list of numbers numbers, complete the function mode that
returns a list of all of the modes of the list of numbers.
The list of numbers will always have at least one number in it.
USE A DICTIONARY
input: list of nums
output: list of nums
First wave: create new dict with keys and value pairs.
Values are counts of occurrences of the keys in the numbers list
Second wave: go thru created dict and if values = max_count then push key to list
Return list of keys

def mode(numbers):
    res = []
    dict = {}
    max_length = 0
    for num in numbers:
        if num not in dict:
            dict[num] = 0
        dict[num] += 1
        if dict[num] > max_length:
            max_length = dict[num]

    for k, v in dict.items():
        if v == max_length:
            res.append(k)
    return res

print(mode([9, 2, 9, 6, 8, 2, 1, 2, 9, 6]))


Another one: return key that has highest value in dictionary
add all values to a list
return max val from list
def high_val(list1):
    result = []
    for k, v in list1.items():
        result.append(v)
    return max(result)

print(high_val({'h': 2, 'e': 54, 'l': 9, 'p': -7}))

# Alternative: use the .values() method
def high_val(list1):
    result = []
    for i in list1.values():
        result.append(i)
    return max(result)

print(high_val({'h': 2, 'e': 54, 'l': 9, 'p': -7}))


# Alternative: use reduce on dictionary using .values() method
from functools import reduce
def high_val(list1):
    if list1:
        return reduce(lambda x, y: x if x > y else y, list1.values())

print(high_val({'h': 2, 'e': 54, 'l': 9, 'p': -7}))


def relation_to_luke(name):

    rel_dict = {
    'Darth Vader': 'father',
    'Leia':	'sister',
    'Han':	'brother in law',
    'R2D2':	'droid'
    }

    for names, position in rel_dict.items():
        if name == names:
            return f'Luke, I am your {position}.'

print(relation_to_luke('Leia'))


#7.Find common keys and values in a dictionary
# DICTIONARY KEYS MUST BE UNIQUE, THEY CAN NOT BE DUPLICATE
def find_item(dict1, dict2):
    # make a new dictionary
    result = {}
    # loop thru dict 1
    for el in dict1:
        # if the key in dict1 is found in dict2 and they equal ea./other
        if el in dict2 and dict1[el] == dict2[el]:
            # add the key to the result dictionary
            result[el] = dict1[el]
    return result

print(find_item({'a': 1, 'b':2, 'c':3}, {'b': 2, 'c':4, 'd': 5}))
# output: {'b': 2}


The main idea is to count all the occurring characters in a string.
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
What if the string is empty? Then the result should be empty object literal, {}.
def count_alpha(string):
    res = {}
    for el in string:
        if el in res:
            res[el] += 1
        else:
            res[el] = 1
    return res

print(count_alpha('alhambra'))


8. Invert a dictionary:
given a dictionary, create a new dictionary where
the keys are the values from the original dictionary,
and the values are lists of keys from the original dictionary that had the corresponding value

original_dict = {'a':1, 'b':2, 'c':1, 'd':3}
output: {1: ['a', 'c'], 2: ['b'], 3: ['d']}

def find_out(dict1):
    result = {}
    for key, value in dict1.items():
        if value in result:
            result[value].append(key)
        else:
            result[value] = [key]
    return result

print(find_out({'a':1, 'b':2, 'c':1, 'd':3}))

Alternative, not the best, but the line where the key is added is interesting
def find_out(dict1):
    result = {}
    for key, value in dict1.items():
        if value not in result.keys():
            result[value] = [key]
        else:
            result[value] = result[value] + [key]
    return result

print(find_out({'a':1, 'b':2, 'c':1, 'd':3}))


# Alternative, absolutely BRILLIANT
def find_out(dict1):
    result = {}
    # loop thru dict1 keys
    for key in dict1.keys():
        # initialise temp as the value of dict1 key, OR default value of []
        tmp = result.get(dict1[key], [])
        # append key to []
        tmp.append(key)
        result[dict1[key]] = tmp
    return result

print(find_out({'a':1, 'b':2, 'c':1, 'd':3}))



10. Group by category
output has the key as the category and the names in a list as values
{'fruit': ['apple', 'banana', etc...], 'category": ['carrot', etc...]}
def cat_group():
    # set the value of items.get('category) as the KEY in result with the VALUE of items.get('name)
    things = [
        {'name': 'apple', 'category': 'fruit'},
        {'name': 'banana', 'category': 'fruit'},
        {'name': 'carrot', 'category': 'vegetable'},
        {'name': 'grape', 'category': 'fruit'},
        {'name': 'broccoli', 'category': 'vegetable'}
        ]
    res = {}
    for row in things:
        if row['category'] in res.keys():
            res[row['category']].append(row['name'])
        else:
            res[row['category']] = [row['name']]
    return res

print(cat_group())

# ALTERNATIVE, BRILLIANT:
def cat_group():
    things = [
        {'name': 'apple', 'category': 'fruit'},
        {'name': 'banana', 'category': 'fruit'},
        {'name': 'carrot', 'category': 'vegetable'},
        {'name': 'grape', 'category': 'fruit'},
        {'name': 'broccoli', 'category': 'vegetable'}
        ]
    output = {}
    for row in things:
        tmp = output.get(row["category"], [])
        tmp.append(row['name'])
        output[row["category"]] = tmp
    return output
print(cat_group())


11. Dictionary key sorting
sort the keys of a dictionary based on their values in descending order
output sorted keys ['David', 'Bob', 'Alice', 'Charlie']

def sort_keys(dict1):
    # specify a sort key- based off of score. This works because .items converts dict items to a list of tuples.
    # Then you can access each item in a tuple by the index--eg. score[1]-- try changing to score[0] to illustrate
    res = dict(sorted(dict1.items(), key=lambda score: score[1], reverse=True))
    return list(res.keys())

print(sort_keys({'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David':95}))




Anagram grouping
given a list of words, group the anagrams together in a dictionary
output: {'eilnst': ['listen', 'silent'], 'aehrt': ['earth', 'heart'], 'hnopty': ['python', 'typhon']}
def ana_gram(list1):
    res = {}
    #  iterate through list1
    for word in list1:
        # unpack the word, sort each letter
        letters = sorted([*word])
        # Join letters back into final word
        letters = ''.join(letters)
        # establish that sorted word as a key in a new dict
        # assign default value of [] to the key
        temp = res.get(letters, [])
        # append value to []
        temp.append(word)
        # add key to res with value of temp
        res[letters] = temp
    return res

print(ana_gram(['listen', 'silent', 'earth', 'heart', 'python', 'typhon']))



DICTIONARY COMPREHENSION::::
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

def get_names(people):

    return [
        {'first_name': person.first_name, "last_name": person.last_name}
            for person in people
    ]


Alternative:
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.children = []

    def add_child(self, person):
        self.children.append(person)

# dict comprehension:
def get_person_and_child_names(person):
    child_names = [
        {'first_name': child.first_name, 'last_name': child.last_name}
        for child in person.children
        ]

    return {
        "first_name": person.first_name,
        "last_name": person.last_name,
        "children": child_names,
    }


convert list to dictionary:
# The function list_to_dict takes a list as its input and transforms it into a dictionary,
# such that each successive pair of values in the list becomes a key and value for the dictionary.
def list_to_dict(lst):
    result = {}
    for i in range(0, len(lst), 2):
        result[lst[i]] = lst[i +1]
    return result
print(list_to_dict(["a", 1, "b", 2]))
# --> {"a": 1, "b": 2}



# convert the dictionary to a list:
# The function dict_to_list takes a dictionary as its input and transforms the dictionary into a list by adding its keys and values to the list.

def dict_to_list(the_dict):
    result = []
    for k, v in the_dict.items():
        result.append(k)
        result.append(v)
    return result

print(dict_to_list({"a": 1, "b": 2}))
# --> ["a", 1, "b", 2]




import json
def decode_and_pluck(input_json, fields):
    json_dict =  json.loads(input_json)
    result = {}
    for field in fields:
        result[field] = json_dict.get(field)
    return result

print(decode_and_pluck('{"a": 1, "b": 2, "c": 3}', ["a", "c"]))
# --> {"a": 1, c": 3}



The input is a list of dictionaries where each dictionary represents an object in space that has a probability of smashing into earth. You're going help sort out the more dangerous objects for further analysis. Follow this pseudo-code:

big_objects = new list
for each of the input space objects
    if the object's estimated diameter is less than 1, skip it
    create a new dictionary with these fields (and values) from the space-object:
        * `estimated_diameter`
        * `impact_probability`
    encoded_object = json encode the dictionary
    add encoded_object to the big_objects list
return the big_objects list

import json
def find_big_space_objects(space_objects):
    big_objects = []
    for obj in space_objects:
        if obj['estimated_diameter'] < 1:
            continue
        big_objects.append(json.dumps({
            'estimated_diameter': obj['estimated_diameter'],
            'impact_probability': obj['impact_probability']
        }))
    return big_objects
print(find_big_space_objects([{'estimated_diameter': 1.5, 'impact_probability': 0.0001, 'mass': 300}]))




Implement the function below that will return a single dictionary that contains all of the key/value pairs of the two input dictionaries.
If both inputs have the same key, then the key in d2 should override the key in d1.

def merge_dictionaries(d1, d2):
    d3 = d1.copy()
    for key, value in d2.items():
        d3[key] = value
    return d3

print(merge_dictionaries({"a":1, "b":2}, {"b":"bbb", "c": "ccc"}))
# --> {"a":1, "b":"bbb", "c": "ccc"})

Alternative:
def merge_dictionaries(d1, d2):
    d3 = d1.copy()
    d3.update(d2)
    return d3

print(merge_dictionaries({"a":1, "b":2}, {"b":"bbb", "c": "ccc"}))
# --> {"a":1, "b":"bbb", "c": "ccc"})




This function takes a list of dictionaries (items) and a list of fields (fields).
It should return a copy of items where each dictionary only contains the fields listed in fields.

def just_these_fields(items, fields):
    result = []
    for row in items:
        temp = {}
        for k, v in row.items():
            if k in fields:
                temp[k] = v
        result.append(temp)
    return result

print(just_these_fields([
    {"a": 1, "b":2, "c": 3},
    {"a":3, "size": 4},
    {"b": 5, "d": 7}
],
["a", "b"]
))
Output:
[
    {"a": 1, "b": 2},
    {"a":3},
    {"b": 5}
]


Alt:
def just_these_fields(items, fields):
    result = []
    for item in items:
        d = {}
        for field in fields:
            value = item.get(field)
            if value:
                d[field] = value
        result.append(d)
    return result

print(just_these_fields([
    {"a": 1, "b":2, "c": 3},
    {"a":3, "size": 4},
    {"b": 5, "d": 7}
],
["a", "b"]
))
Output:
[
    {"a": 1, "b": 2},
    {"a":3},
    {"b": 5}
]

Alternative
def just_these_fields(items, fields):
    result = []
    for item in items:
        sub_dict = {key:value for key,value in item.items() if key in fields}
        result.append(sub_dict)
    return result

print(just_these_fields([
    {"a": 1, "b":2, "c": 3},
    {"a":3, "size": 4},
    {"b": 5, "d": 7}
],
["a", "b"]
))
Output:
[
    {"a": 1, "b": 2},
    {"a":3},
    {"b": 5}
]




This function takes a dictionary and returns the sum of all of the summable values in it. Here "summable" means any value that is:

an int or a float
is a string and isnumeric(). These should be cast to float()

def sum_summables(dictionary):
    total = 0

    # loop over the things, get the ones you want
    for value in dictionary.values():
        if isinstance(value, (int, float)):
            total += value
        elif isinstance(value, str):
            if value.isnumeric():
                total += float(value)

    return total

dictionary = {
    "dog": 1,
    "number": "three",
    "size": "2",
    "heavy": True,
    "weight": 3.4,
}

print(sum_summables(dictionary))
# --> 7.4




# This function takes a list of dictionaries (items) and dictionary of filters (filters). It should return a filtered copy of items with only the items that match any of the filters.

def only_items_with(items, filters):
    result = []
    for item in items:
        keep = False
        for key, value in filters.items():
            if item.get(key) == value:
                keep = True
                break
        if keep:
            result.append(item)
    return result

print(only_items_with(items = [
    {"color":"blue", "size":"small"},
    {"color":"red", "size":"small"},
    {"color":"purple", "size":"medium"},
    {"color":"green", "size":"large"},
],
filters = {
    "color": "blue",
    "size": "medium"
}))

# Alternative:
def only_items_with(items, filters):
    result = []
    for item in items:
        for value in item.values():
            if value in filters.values():
                result.append(item)
                break

    return result

print(only_items_with(items = [
    {"color":"blue", "size":"small"},
    {"color":"red", "size":"small"},
    {"color":"purple", "size":"medium"},
    {"color":"green", "size":"large"},
],
filters = {
    "color": "blue",
    "size": "medium"
}))
