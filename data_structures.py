# # create a Node class:
# class Node:
#     def __init__(self, value, link=None):
#         self.value = value
#         #add link property
#         self.link = link

#     # Add code so print looks more like JavaScript output
#     def __str__(self):
#         return ("Node { value: '" + str(self.value)
#                 + "', link: " + str(self.link) + " }")

# # x = Node(5)
# # print(x)
# # print(x.value)

# # x.value = 10
# # print(x.value)

# p = Node('paper')
# r = Node('rock')
# s = Node('scissors')

# # print(p.value, r.value, s.value)
# # print(p.link)
# # print(p)

# p.link = r
# print(p)

# r.link = s
# print(p)


# # Let's make a QUEUE!
# class MyQ:
#     def __init__(self, head=None, tail=None):
#         self.head = head
#         self.tail = tail


# # Enqueue: add Node to back of the queue
#     def enqueue(self, val):
#         # Instantiate new node with value
#         n = Node(val)

#         #If queue is empty:
#         if self.head is None:
#             self.head = n
#             self.tail = n

#         # If queue has members:
#         else:
#             # link for old tail becomes new node
#             self.tail.link = n

#             #tail points to new tail
#             self.tail = n
#         # enqueue does not need to return a value

#         # Dequeue: remove from front of the queue and return value
#     def dequeue(self):
#         # Queue can not be empty
#         assert self.head, "Queue is empty"

#          # Temporarily store value for node at head
#         _value = self.head.value

#         # Reassign head property to node
#         # current head's link points to
#         self.head = self.head.link

#         # If final item removed
#         # set tail to None as well
#         if self.head is None:
#             self.tail = None

#         # return value
#         return _value

# # Single Linked List:
# class MyNode:

#     def __init__(self, value=None, link=None):
#         self.value = value
#         self.link = link

#     def __str__(self):
#         return f"Node with value:{self.value}"

# Length instance attribute

# Value can be returned
# from any location

# Values can be inserted
# into the list at any index

# Values can be removed
# from the list from any location

# The list can be searched

# class MySLL:
#     def __init__(self,
#                  head=None,
#                  tail=None):

#         self.head = head
#         self.tail = tail
#         self._length = 0

#     # "read-only" length property
#     @property
#     def length(self):
#         return self._length

#     def traverse(self, idx):
#     # If list empty
#     # If idx out of bounds
#         if (
#             self._length == 0 or
#             idx > (self._length - 1)
#     ):
#             raise IndexError("idx out of range")

#         # If idx not an integer
#         if not isinstance(idx, int):
#             raise TypeError("idx must be an integer")

#         i = 0
#         _current_node = self.head

#         while i < idx:
#             _current_node = _current_node.link
#             i += 1

#         return _current_node


#     def insert(self, val, idx=None):

#         _new_node = MyNode(val, link=None)

#         # idx None (default)
#         if idx is None:
#             idx = self._length

#         # list empty, inserting first node
#         if self.head is None:
#             self.head = _new_node
#             self.tail = _new_node
#             self._length += 1
#             return None

#         # insert at tail (default)
#         elif (idx == self._length):
#             self.tail.link = _new_node
#             self.tail = _new_node
#             self._length += 1
#             return None

#         # insert before head
#         elif idx == 0:
#             _new_node.link = self.head
#             self.head = _new_node
#             self._length += 1
#             return None

#         # insert between two nodes
#         else:
#             this_idx_node = self.traverse(idx - 1)
#             next_idx_node = this_idx_node.link

#             _new_node.link = next_idx_node
#             this_idx_node.link = _new_node

#             self._length += 1
#             return None


#     def remove(self, idx=0):
#         # If list empty
#         # If idx out of bounds
#         if (
#             self._length == 0 or
#             idx > (self._length - 1)
#         ):
#             raise IndexError("idx out of range")

#         # If idx not an integer
#         if not isinstance(idx, int):
#             raise TypeError("idx must be an integer")

#         # If idx 0
#         if idx == 0:
#             _val = self.head.value
#             self.head = self.head.link
#             self._length -= 1

#             # If no other members
#             if self._length == 0:
#                 self.tail = None

#             return _val

#         # Other indices
#         previous_idx_node = self.traverse(idx - 1)
#         this_idx_node = previous_idx_node.link

#         _val = this_idx_node.value

#         next_idx_node = this_idx_node.link

#         # connect previous to next
#         previous_idx_node.link = next_idx_node

#         if next_idx_node is None:
#             self.tail = previous_idx_node

#         self._length -= 1
#         return _val


# MERGE SORT:
def mergeSort(array):
    if len(array) > 1:
        #  middle is the point where the array is divided into two subarrays
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        # Sort the two halves
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

        # Until we reach either end of either left or right, pick larger among
        # elements left and right and place them in the correct position at A[p..r]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # When we run out of elements in either left or right,
        # pick up the remaining elements and put in A[p..r]
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def find_median(array):
    n = len(array)
    # print(n)
    if n % 2 != 0:  # For odd number of elements
        median = array[n // 2]
    else:  # For even number of elements
        median = (array[n // 2 - 1] + array[n // 2]) / 2
    return median


def find_mode(array):
    mode_count = {}  # Dictionary to store element counts
    max_count = 0  # Variable to track the maximum count

    # Count occurrences of each element in the array
    for num in array:
        if num in mode_count:
            mode_count[num] += 1
        else:
            mode_count[num] = 1

        # Update max_count if needed
        if mode_count[num] > max_count:
            max_count = mode_count[num]

    # Find element(s) with maximum count (mode)
    modes = [key for key, value in mode_count.items() if value == max_count]

    return modes, max_count


array = [
    -71,
    28,
    57,
    39,
    -45,
    17,
    -46,
    57,
    57,
    57,
    4,
    86,
    -15,
    97,
    97,
    70,
    57,
    -15,
    -46,
    74,
    29,
    74,
    57,
    60,
    39,
    -33,
    70,
    60,
    4,
    70,
    39,
    37,
    70,
    86,
    -40,
    4,
    101,
    20,
    57,
    4,
    -30,
    70,
    2,
    4,
    85,
    29,
    86,
    -15,
    -66,
    4,
    101,
    86,
    -40,
    4,
    97,
    -79,
    -45,
    4,
    75,
    -66,
    -40,
    5,
    4,
    85,
    51,
    2,
    97,
    7,
    -46,
    97,
    70,
    -46,
    -45,
    20,
    7,
    -33,
    -46,
    -84,
    70,
    -40,
    75,
    74,
    28,
    75,
    39,
    10,
    86,
    37,
    29,
    39,
    7,
    4,
    75,
    10,
    5,
    13,
    0,
    17,
    93,
    39,
    85,
    -71,
    57,
    4,
    29,
    85,
    2,
    -33,
    -46,
    75,
    -15,
    -15,
    75,
    93,
    -84,
    28,
    4,
    -46,
    -15,
    0,
    -68,
    70,
    29,
    29,
    75,
    4,
    2,
    4,
    74,
    -79,
    57,
    -45,
    75,
    57,
    -15,
    85,
    -46,
    75,
    85,
    -84,
    74,
    86,
    -46,
    -84,
    4,
    86,
    92,
    -40,
    2,
    -30,
    28,
    57,
    39,
    57,
    86,
    75,
    70,
    29,
    39,
    70,
    74,
    -79,
    70,
    2,
    75,
    39,
    29,
    29,
    70,
    60,
    29,
    17,
    -40,
    97,
    97,
    97,
    29,
    57,
    73,
    60,
    -30,
    4,
    51,
    10,
    -15,
    39,
    51,
    -68,
    70,
    39,
    39,
    -45,
    4,
    -40,
    4,
    -71,
    2,
    39,
    86,
    -30,
    57,
    4,
    20,
    51,
    86,
    4,
    86,
    5,
    70,
    70,
    -33,
    4,
    57,
    86,
    -46,
    10,
    4,
    7,
    -40,
    -17,
    -46,
    20,
    39,
    -33,
    85,
    -84,
    -40,
    39,
    75,
    2,
    -15,
    -17,
    4,
    -45,
    93,
    57,
    57,
    7,
    51,
    5,
    -33,
    37,
    70,
    -84,
    -40,
    85,
    70,
    74,
    4,
    10,
    -33,
    20,
    92,
    75,
    85,
    20,
    70,
    97,
    -33,
    -71,
    85,
    -71,
    29,
    51,
    75,
    -68,
    75,
    7,
    51,
    -15,
    29,
    74,
    75,
    -46,
    0,
    4,
    7,
    73,
    17,
    97,
    57,
    7,
    5,
    -33,
    51,
    29,
    2,
    86,
    17,
    92,
    -84,
    -40,
    -66,
    -40,
    -68,
    75,
    92,
    86,
    4,
    86,
    5,
    51,
    7,
    39,
    -33,
    75,
    -84,
    51,
    86,
    70,
    -40,
    -15,
    -17,
    -46,
    85,
    -15,
    97,
    4,
    57,
    -46,
    -84,
    -30,
    0,
    20,
    86,
    51,
    0,
    -33,
    -40,
    37,
    -40,
    75,
    -46,
    92,
    -46,
    7,
    86,
    86,
    29,
    39,
    57,
    -33,
    85,
    39,
    57,
    -71,
    4,
    -40,
    7,
    2,
    4,
    -40,
    20,
    2,
    -46,
    101,
    4,
    28,
    39,
    -66,
    29,
    93,
    57,
    20,
    29,
    -40,
    4,
    29,
    57,
    39,
    -71,
    97,
    74,
    7,
    -40,
    5,
    86,
    5,
    7,
    29,
    -46,
    5,
    86,
    4,
    -71,
    -30,
    -71,
    29,
    -45,
    -68,
    39,
    5,
    -71,
    4,
    -30,
    75,
    70,
    101,
    2,
    86,
    85,
    86,
    4,
    57,
    29,
    -46,
    -15,
    97,
    -46,
    2,
    74,
    -45,
    -46,
    -66,
    -71,
    37,
    60,
    4,
    -33,
    57,
    -15,
    -33,
    86,
    2,
    74,
    -68,
    -40,
    29,
    93,
    60,
    20,
    92,
    75,
    20,
    -68,
    -33,
    51,
    86,
    57,
    -68,
    74,
    -84,
    -40,
    74,
    86,
    -33,
    -46,
    86,
    -46,
    75,
    -15,
    -68,
    -84,
    85,
    5,
    75,
    -15,
    -33,
    7,
    20,
    5,
    -71,
    75,
    85,
    28,
    86,
    -84,
    75,
    29,
    -79,
    7,
    -46,
    -33,
    2,
    -15,
    -84,
    37,
    60,
    70,
    -46,
    51,
    -71,
    75,
    -40,
    5,
    58,
    93,
    -33,
    -15,
    86,
    86,
    -46,
    -45,
    39,
    86,
    4,
    -33,
    -84,
    60,
    60,
    75,
    2,
    37,
    2,
    -46,
    97,
    -46,
    -15,
    -15,
    17,
    -17,
    39,
    4,
    51,
    29,
    -46,
    85,
    7,
    2,
    7,
    -45,
    10,
    4,
    70,
    7,
    29,
    -71,
    97,
    74,
    4,
    12,
    2,
    -71,
    -33,
    70,
    -33,
    -84,
    86,
    74,
    2,
    -33,
    29,
    17,
    60,
    2,
    -17,
    -33,
    5,
    17,
    -46,
    2,
    -33,
    17,
    -15,
    4,
    17,
    -33,
    70,
    57,
    -17,
    75,
    97,
    2,
    -17,
    29,
    7,
    -15,
    -40,
    -33,
    -15,
    -71,
    74,
    101,
    4,
    -33,
    -84,
    2,
    -45,
    28,
    97,
    97,
    86,
    -15,
    7,
    57,
    29,
    29,
    -15,
    -45,
    5,
    58,
    2,
    75,
    86,
    -17,
    10,
    39,
    57,
    75,
    39,
    86,
    2,
    4,
    -15,
    4,
    97,
    101,
    10,
    -33,
    92,
    97,
    60,
    4,
    7,
    -15,
    5,
    -66,
    51,
    -17,
    0,
    -40,
    85,
    -15,
    92,
    29,
    -84,
    70,
    17,
    51,
    -40,
    101,
    -68,
    2,
    85,
    -33,
    74,
    75,
    2,
    -15,
    97,
    -84,
    -84,
    57,
    -46,
    70,
    86,
    39,
    17,
    86,
    -40,
    39,
    2,
    86,
    57,
    75,
    86,
    2,
    -84,
    51,
    -68,
    7,
    -33,
    39,
    20,
    20,
    29,
    -71,
    -84,
    75,
    -71,
    4,
    -15,
    2,
    -17,
    51,
    70,
    39,
    93,
    -15,
    97,
    39,
    74,
    4,
    93,
    57,
    4,
    39,
    70,
    28,
    97,
    2,
    -66,
    5,
    5,
    4,
    37,
    -46,
    74,
    2,
    5,
    -15,
    -45,
    97,
    -15,
    97,
    57,
    2,
    7,
    75,
    85,
    -33,
    -33,
    93,
    92,
    86,
    97,
    4,
    2,
    101,
    -68,
    -17,
    -17,
    29,
    5,
    20,
    -68,
    -71,
    4,
    2,
    93,
    -45,
    0,
    -33,
    73,
    2,
    -30,
    70,
    75,
    51,
    85,
    0,
    4,
    51,
    57,
    4,
    97,
    57,
    -40,
    -68,
    20,
    39,
    70,
    29,
    -33,
    4,
    2,
    57,
    -46,
    70,
    7,
    -68,
    75,
    39,
    2,
    97,
    86,
    -46,
    86,
    29,
    -84,
    51,
    -84,
    20,
    5,
    4,
    -15,
    -40,
    75,
    37,
    2,
    60,
    86,
    -84,
    57,
    57,
    85,
    2,
    39,
    70,
    -79,
    39,
    39,
    85,
    92,
    57,
    101,
    -68,
    20,
    2,
    92,
    5,
    29,
    29,
    -15,
    -46,
    -30,
    29,
    -30,
    39,
    75,
    -15,
    97,
    7,
    57,
    -66,
    2,
    -46,
    39,
    -84,
    70,
    39,
    5,
    -17,
    29,
    57,
    2,
    -33,
    86,
    2,
    0,
    39,
    60,
    -15,
    -15,
    57,
    -68,
    -15,
    -68,
    29,
    7,
    10,
    -15,
    -15,
    -46,
    86,
    70,
    75,
    -33,
    2,
    2,
    -46,
    74,
    39,
    5,
    17,
    29,
    -66,
    97,
    85,
    -40,
    2,
    2,
    4,
    97,
    97,
    -46,
    92,
    -15,
    2,
    37,
    86,
    2,
    58,
    58,
    -33,
    97,
    2,
    10,
    39,
    74,
    20,
    4,
    74,
    58,
    -40,
    -71,
    -40,
    -33,
    97,
    39,
    29,
    -45,
    85,
    2,
    74,
    51,
    29,
    -45,
    57,
    -33,
    57,
    -68,
    51,
    29,
    -84,
    20,
    57,
    -68,
    20,
    86,
    58,
    -84,
    85,
    29,
    -46,
    39,
    2,
    5,
    -15,
    92,
    70,
    97,
    10,
    58,
    2,
    2,
    4,
    70,
    93,
    20,
    -45,
    -17,
    -84,
    75,
    60,
    37,
    7,
    -17,
    86,
    57,
    4,
    7,
    74,
    4,
    -71,
    4,
    57,
    20,
    85,
    74,
    29,
    -46,
    -30,
    -46,
    74,
    -40,
    -33,
    -17,
    57,
    -33,
    -46,
    4,
    57,
    10,
    2,
    20,
    70,
    39,
    -46,
    -33,
    -46,
    4,
    -40,
    93,
    -40,
    29,
    39,
    -79,
    -17,
    -33,
    29,
    57,
    4,
    51,
    -33,
    -68,
    70,
    97,
    4,
    37,
    7,
    5,
    -71,
    2,
    -13,
    86,
    85,
    39,
    -33,
    -71,
    29,
]

mergeSort(array)
print("Sorted array, first num:", array[0])

# # Find the median value from the sorted array
# median_value = find_median(array)
# print("Median value:", median_value)

# Assuming 'array' is the sorted array obtained from merge_sort
modes, mode_count = find_mode(array)
print("Mode(s) value(s):", modes)
print("count:", mode_count)
