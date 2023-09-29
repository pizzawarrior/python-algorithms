import math


class EquilateralShape:
    # first we start with an init method:
    def __init__(self, num_sides, side_length):
        # self holds the instance of class, default
        self.num_sides = num_sides
        self.side_length = side_length

    # we never return anything from the init method

# now we can create instances that have different values, aka put this thing to work!
# triangle1 = EquilateralShape(3, 1)
# triangle2 = EquilateralShape(3, 100)
# square = EquilateralShape(3, 1)

# print(triangle1.num_sides)    # Prints 3
# print(triangle1.side_length)  # Prints 1

# print(triangle2.num_sides)    # Prints 3
# print(triangle2.side_length)  # Prints 100

# print(square.num_sides)       # Prints 4
# print(square.side_length)     # Prints 1


# We'll often write methods for the class for each behavior that we want to add.
# Here's the description of the behavior for calculating the perimeter:
def calc_perimeter(self):
    return self.num_sides * self.side_length

# Calculate area of different shapes:
# Can comment out now because child classes created for each shape below::
# def calculate_area(self):
#     side_squared = pow(self.side_length, 2)
#     #for triangle:
#     if self.num_sides == 3:
#         return math.sqrt(3) / 4 * side_squared
#     #for square:
#     if self.num_sides == 4:
#         return side_squared
#     #for pentagon
#     elif self.num_sides == 5:
#         weird_value = math.sqrt(25 + 10 * math.sqrt(5))
#         return weird_value / 4 * side_squared
#     #for hexagon:
#     elif self.num_sides == 6:
#         return (3 * math.sqrt(3)) / 2 * side_squared
#     else:
#         raise ValueError


#class INHERITANCE: use this to replace the if statement above for the triangle
class EquilateralTriangle(EquilateralShape):
    def __init__(self, side_length):
        super().__init__(3, side_length)

    def calculate_area(self):
        side_squared = pow(self.side_length, 2)
        return math.sqrt(3) / 4 * side_squared

# triangle = EquilateralTriangle(2)
# print(triangle.num_sides)    # Prints 3
# print(triangle.side_length)  # Prints 2

# print(triangle.calculate_perimeter())
# # Prints 6

# print(triangle.calculate_area())
# # Prints 1.7320508075688772

#  Now let's init the SQUARE child class:
class Square(EquilateralShape):
    def __init__(self, side_length):
        super().__init__(4, side_length)

    def calculate_area(self):
        return pow(self.side_length, 2)

# Pentagon child class:
class Pentagon(EquilateralShape):
    def __init__(self, side_length):
        super().__init__(5, side_length)

    def calculate_area(self):
        side_squared = pow(self.side_length, 2)
        weird_value = math.sqrt(25 + 10 * math.sqrt(5))
        return weird_value / 4 * side_squared

# Now it's Hexagon's turn:
class EquilateralHexagon(EquilateralShape):
    def __init__(self, side_length):
        super().__init__(6, side_length)

    def calculate_area(self):
        side_squared = pow(self.side_length, 2)
        return (3 * math.sqrt(3)) / 2 * side_squared
