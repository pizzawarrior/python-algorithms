# Learning objectives

    # python classes - syntax
    # dunder methods for classes
        # init
        # methods to do various things inside classes
    # instantiate instances
    # inheritance
    # classmethods


# Everything in python is an object

# print(type([]))
# # <class 'list'>

# # classes also allow you to create custom classes
# # classes are blueprints from which you can create objects

# class PlayerCharacter:
#     # the init is a dunder mthod or a magic method
#     # at the top when you build your class
#     # it is a constructor method
#     # it is automatically called when we instantiate
#     # self refers to the PlayCharacter - self.name to equal whatever the parameter name is when i instantiate the class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         return 'done'


# print(PlayerCharacter)

# player1 = PlayerCharacter('Cindy', 44)
# print(player1.name)
# print(f'{player1.name} is {player1.age} years old')
# print(player1.run())


# # help(list)
# # help method shows you everything the object has access to




# classmethods and static methods - decorators


# class Dog():
#     dog_id = 1 # class attribute - this variable is shared across all instance
#     # each dog that we instantiate from this class has dog_id to it

#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#         self.id = Dog.dog_id
#         Dog.dog_id += 1 #adds 1 every time a new dog is created

#     def bark(self):
#         print(f"{self.name} says wooof!!")

#     def __str__(self): #string method - prints the class in the following way
#         return f"Dog {self.id} named {self.name} is {self.age} years old"

#     @classmethod
#     def get_total_dogs(cls):
#         # get us the total number of dogs that were instantiated from this class
#         return cls.dog_id -1


# first_dog = Dog('Spock', 8)
# print(first_dog)

# second_dog = Dog('Sniffles', 2)

# third_dog = Dog('Julius', 4)

# print(Dog.get_total_dogs())



#Random:
#Use this for help on objects, etc:
#help(list)
#type Q in terminal below to exit


#EXERCISE:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# #Add cats:
# cat1 = Cat('alfafa', 42)
# cat2 = Cat('Mini', 13)
# cat3 = Cat('pinwheel', 37)

# def oldest_cat(*args):
#     if cat1.age > cat2.age and cat1.age > cat3.age:
#         old_cat = cat1
#     elif cat2.age > cat1.age and cat2.age > cat3.age:
#         old_cat = cat2
#     else:
#         old_cat = cat3
#     return old_cat.age

# print((f"The oldest cat is {oldest_cat(cat1, cat2, cat3)} years old"))


#BETTER SOLUTION:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# #Add cats:
# cat1 = Cat('alfafa', 42)
# cat2 = Cat('Mini', 13)
# cat3 = Cat('pinwheel', 37)

# # # find the oldest cat
# def get_oldest_cat(*args):
#     return max(args)

# # # output
# # "The oldest cat is ____ years old"

# print(f"the oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old")






# inheritance

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def compound_interest(self):
        new_balance = self.interest_rate * self.balance + self.balance
        self.balance = int(new_balance)
        return self.balance


#put it to work:
sav_account1 = SavingsAccount(300, .13)

print(f'your current savings balance is {sav_account1.compound_interest()}')
