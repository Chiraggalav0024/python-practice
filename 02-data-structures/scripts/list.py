# ============================================================
#                 PYTHON LIST - COMPLETE GUIDE
# ============================================================

print("=" * 70)
print("                 PYTHON LIST OPERATIONS")
print("=" * 70)


# ============================================================
# 1. CREATING LISTS
# ============================================================

print("\n1. CREATING LISTS")

# Empty list
empty_list = []

# List of integers
numbers = [10, 20, 30, 40, 50]

# List of strings
names = ["Alice", "Bob", "Charlie"]

# Mixed data types
mixed = [10, "Python", 3.14, True, None]

# Nested list
nested = [[1, 2], [3, 4], [5, 6]]

print("Empty:", empty_list)
print("Numbers:", numbers)
print("Names:", names)
print("Mixed:", mixed)
print("Nested:", nested)


# ============================================================
# 2. LIST USING list()
# ============================================================

print("\n2. USING list()")

a = list("Python")
b = list(range(1, 6))

print(a)
print(b)


# ============================================================
# 3. INDEXING
# ============================================================

print("\n3. INDEXING")

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Last element:", numbers[-1])
print("Second last:", numbers[-2])

# Index positions:
#
# Positive:
#   0    1    2    3    4
# [10, 20, 30, 40, 50]
#
# Negative:
#  -5   -4   -3   -2   -1
# [10, 20, 30, 40, 50]


# ============================================================
# 4. CHANGING LIST ELEMENTS
# ============================================================

print("\n4. CHANGING ELEMENTS")

numbers = [10, 20, 30, 40, 50]

numbers[0] = 100
numbers[-1] = 500

print(numbers)


# ============================================================
# 5. SLICING
# ============================================================

print("\n5. SLICING")

numbers = [10, 20, 30, 40, 50]

print("Original:", numbers)

print("numbers[1:4]:", numbers[1:4])
print("numbers[:3]:", numbers[:3])
print("numbers[2:]:", numbers[2:])
print("numbers[:]:", numbers[:])

print("Every second element:", numbers[::2])
print("Reverse:", numbers[::-1])
print("Reverse using [::-1]:", numbers[::-1])

# Syntax:
#
# list[start : stop : step]
#
# IMPORTANT:
# stop index is NOT included.


# ============================================================
# 6. LENGTH
# ============================================================

print("\n6. len()")

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))


# ============================================================
# 7. ADDING ELEMENTS - append()
# ============================================================

print("\n7. append()")

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

# append() adds ONE object at the end.


# ============================================================
# 8. append() WITH A LIST
# ============================================================

print("\n8. append() WITH LIST")

numbers = [10, 20, 30]

numbers.append([40, 50])

print(numbers)

# Result:
# [10, 20, 30, [40, 50]]
#
# The entire [40, 50] becomes ONE element.


# ============================================================
# 9. extend()
# ============================================================

print("\n9. extend()")

numbers = [10, 20, 30]

numbers.extend([40, 50])

print(numbers)

# Result:
# [10, 20, 30, 40, 50]


# ============================================================
# 10. append() vs extend()
# ============================================================

print("\n10. append() VS extend()")

a = [1, 2]
a.append([3, 4])

b = [1, 2]
b.extend([3, 4])

print("append:", a)
print("extend:", b)


# ============================================================
# 11. insert()
# ============================================================

print("\n11. insert()")

numbers = [10, 20, 40, 50]

numbers.insert(2, 30)

print(numbers)

# insert(index, value)


# ============================================================
# 12. insert() AT DIFFERENT POSITIONS
# ============================================================

print("\n12. insert() EXAMPLES")

numbers = [10, 20, 30]

numbers.insert(0, 5)
print("Beginning:", numbers)

numbers.insert(len(numbers), 100)
print("End:", numbers)

numbers.insert(2, 25)
print("Middle:", numbers)


# ============================================================
# 13. REMOVING ELEMENT - remove()
# ============================================================

print("\n13. remove()")

numbers = [10, 20, 30, 20, 40]

numbers.remove(20)

print(numbers)

# remove() removes the FIRST matching value.


# ============================================================
# 14. pop()
# ============================================================

print("\n14. pop()")

numbers = [10, 20, 30, 40]

x = numbers.pop()

print("Removed:", x)
print("List:", numbers)


# ============================================================
# 15. pop(index)
# ============================================================

print("\n15. pop(index)")

numbers = [10, 20, 30, 40]

x = numbers.pop(1)

print("Removed:", x)
print("List:", numbers)


# ============================================================
# 16. del
# ============================================================

print("\n16. del")

numbers = [10, 20, 30, 40, 50]

del numbers[1]

print("After deleting index 1:", numbers)

del numbers[1:3]

print("After deleting slice:", numbers)


# ============================================================
# 17. clear()
# ============================================================

print("\n17. clear()")

numbers = [10, 20, 30]

numbers.clear()

print(numbers)


# ============================================================
# 18. remove vs pop vs del vs clear
# ============================================================

print("\n18. REMOVE vs POP vs DEL vs CLEAR")

numbers = [10, 20, 30, 40, 50]

# remove(value)
numbers.remove(20)

# pop(index)
removed = numbers.pop(1)

# del
del numbers[0]

print("Remaining:", numbers)
print("Popped:", removed)

# clear() would remove EVERYTHING.


# ============================================================
# 19. SEARCHING - in
# ============================================================

print("\n19. MEMBERSHIP")

numbers = [10, 20, 30, 40]

print(20 in numbers)
print(100 in numbers)

print(20 not in numbers)
print(100 not in numbers)


# ============================================================
# 20. index()
# ============================================================

print("\n20. index()")

numbers = [10, 20, 30, 20, 40]

print("Index of 20:", numbers.index(20))


# ============================================================
# 21. count()
# ============================================================

print("\n21. count()")

numbers = [10, 20, 20, 30, 20, 40]

print("20 occurs:", numbers.count(20), "times")


# ============================================================
# 22. MIN, MAX, SUM
# ============================================================

print("\n22. min(), max(), sum()")

numbers = [10, 20, 30, 40, 50]

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))


# ============================================================
# 23. SORTING - sort()
# ============================================================

print("\n23. sort()")

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print("Ascending:", numbers)

numbers.sort(reverse=True)

print("Descending:", numbers)


# ============================================================
# 24. sorted()
# ============================================================

print("\n24. sorted()")

numbers = [50, 10, 40, 20, 30]

new_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted copy:", new_numbers)


# ============================================================
# 25. sort() vs sorted()
# ============================================================

print("\n25. sort() VS sorted()")

numbers = [3, 1, 2]

result = numbers.sort()

print("List after sort():", numbers)
print("Return value of sort():", result)

numbers = [3, 1, 2]

result = sorted(numbers)

print("Original list:", numbers)
print("Result:", result)


# IMPORTANT:
# sort() changes the original list and returns None.
#
# sorted() creates/returns a sorted list
# without changing the original list.


# ============================================================
# 26. REVERSE
# ============================================================

print("\n26. reverse()")

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)


# ============================================================
# 27. COPY
# ============================================================

print("\n27. copy()")

a = [10, 20, 30]

b = a.copy()

b.append(40)

print("a:", a)
print("b:", b)


# ============================================================
# 28. ALIASING - IMPORTANT CONFUSING PART
# ============================================================

print("\n28. ALIASING")

a = [10, 20, 30]

b = a

b.append(40)

print("a:", a)
print("b:", b)

# a and b refer to the SAME list.


# ============================================================
# 29. IDENTITY - is
# ============================================================

print("\n29. is")

a = [1, 2, 3]
b = a
c = a.copy()

print("a is b:", a is b)
print("a is c:", a is c)

print("a == b:", a == b)
print("a == c:", a == c)


# ============================================================
# 30. == VS is
# ============================================================

print("\n30. == VS is")

a = [1, 2, 3]
b = [1, 2, 3]

print("a == b:", a == b)
print("a is b:", a is b)

# == checks VALUE/equality.
# is checks whether both references point to SAME OBJECT.


# ============================================================
# 31. LIST CONCATENATION
# ============================================================

print("\n31. CONCATENATION")

a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

print(c)


# ============================================================
# 32. LIST REPETITION
# ============================================================

print("\n32. REPETITION")

numbers = [1, 2, 3]

print(numbers * 3)


# ============================================================
# 33. UNPACKING
# ============================================================

print("\n33. UNPACKING")

numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)


# ============================================================
# 34. STAR UNPACKING
# ============================================================

print("\n34. STAR UNPACKING")

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# ============================================================
# 35. LOOP THROUGH LIST
# ============================================================

print("\n35. FOR LOOP")

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)


# ============================================================
# 36. LOOP WITH INDEX - range(len())
# ============================================================

print("\n36. LOOP WITH INDEX")

numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])


# ============================================================
# 37. enumerate()
# ============================================================

print("\n37. enumerate()")

numbers = [10, 20, 30, 40]

for index, value in enumerate(numbers):
    print(index, value)


# ============================================================
# 38. LIST COMPREHENSION
# ============================================================

print("\n38. LIST COMPREHENSION")

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print("Squares:", squares)


# ============================================================
# 39. LIST COMPREHENSION WITH CONDITION
# ============================================================

print("\n39. LIST COMPREHENSION WITH CONDITION")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = [x for x in numbers if x % 2 == 0]

print("Even:", even)


# ============================================================
# 40. IF-ELSE IN LIST COMPREHENSION
# ============================================================

print("\n40. IF-ELSE COMPREHENSION")

numbers = [1, 2, 3, 4, 5]

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)


# ============================================================
# 41. NESTED LIST
# ============================================================

print("\n41. NESTED LIST")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

print("First row:", matrix[0])
print("First row, first element:", matrix[0][0])
print("Second row, third element:", matrix[1][2])


# ============================================================
# 42. MODIFY NESTED LIST
# ============================================================

print("\n42. MODIFY NESTED LIST")

matrix = [
    [1, 2],
    [3, 4]
]

matrix[0][1] = 100

print(matrix)


# ============================================================
# 43. NESTED LOOP
# ============================================================

print("\n43. NESTED LOOP")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")

    print()


# ============================================================
# 44. COPYING NESTED LIST - SHALLOW COPY
# ============================================================

print("\n44. SHALLOW COPY")

a = [[1, 2], [3, 4]]

b = a.copy()

b[0][0] = 100

print("a:", a)
print("b:", b)

# The inner list is still shared.


# ============================================================
# 45. DEEP COPY
# ============================================================

print("\n45. DEEP COPY")

import copy

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

b[0][0] = 100

print("a:", a)
print("b:", b)


# ============================================================
# 46. COPYING USING SLICING
# ============================================================

print("\n46. COPY USING SLICING")

a = [1, 2, 3]

b = a[:]

b.append(4)

print("a:", a)
print("b:", b)


# ============================================================
# 47. COPYING USING list()
# ============================================================

print("\n47. COPY USING list()")

a = [1, 2, 3]

b = list(a)

b.append(4)

print("a:", a)
print("b:", b)


# ============================================================
# 48. ANY AND ALL
# ============================================================

print("\n48. any() AND all()")

numbers = [2, 4, 6, 8]

print("any:", any(x > 5 for x in numbers))
print("all:", all(x % 2 == 0 for x in numbers))


# ============================================================
# 49. ZIP
# ============================================================

print("\n49. zip()")

names = ["Alice", "Bob", "Charlie"]
marks = [90, 85, 95]

for name, mark in zip(names, marks):
    print(name, mark)


# ============================================================
# 50. CONVERTING LIST TO STRING
# ============================================================

print("\n50. JOIN")

words = ["Python", "is", "powerful"]

sentence = " ".join(words)

print(sentence)


# ============================================================
# 51. CONVERTING STRING TO LIST
# ============================================================

print("\n51. split()")

sentence = "Python is powerful"

words = sentence.split()

print(words)


# ============================================================
# 52. FILTERING
# ============================================================

print("\n52. filter()")

numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)


# ============================================================
# 53. map()
# ============================================================

print("\n53. map()")

numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))

print(squares)


# ============================================================
# 54. SORTING STRINGS
# ============================================================

print("\n54. SORTING STRINGS")

names = ["Charlie", "Alice", "Bob"]

names.sort()

print(names)


# ============================================================
# 55. SORTING BY LENGTH
# ============================================================

print("\n55. SORTING BY LENGTH")

names = ["John", "Alexander", "Bob", "Christopher"]

names.sort(key=len)

print(names)


# ============================================================
# 56. SORTING WITH lambda
# ============================================================

print("\n56. SORTING WITH lambda")

students = [
    ["Alice", 85],
    ["Bob", 95],
    ["Charlie", 75]
]

students.sort(key=lambda x: x[1])

print(students)


# ============================================================
# 57. REVERSE SORTING
# ============================================================

print("\n57. REVERSE SORTING")

students = [
    ["Alice", 85],
    ["Bob", 95],
    ["Charlie", 75]
]

students.sort(key=lambda x: x[1], reverse=True)

print(students)


# ============================================================
# 58. DELETE LAST ELEMENT
# ============================================================

print("\n58. DELETE LAST ELEMENT")

numbers = [1, 2, 3, 4, 5]

del numbers[-1]

print(numbers)


# ============================================================
# 59. DELETE MULTIPLE ELEMENTS
# ============================================================

print("\n59. DELETE MULTIPLE ELEMENTS")

numbers = [1, 2, 3, 4, 5, 6]

del numbers[1:4]

print(numbers)


# ============================================================
# 60. REPLACE MULTIPLE ELEMENTS USING SLICING
# ============================================================

print("\n60. REPLACE USING SLICING")

numbers = [1, 2, 3, 4, 5]

numbers[1:4] = [20, 30, 40]

print(numbers)


# ============================================================
# 61. INSERT MULTIPLE ELEMENTS USING SLICING
# ============================================================

print("\n61. INSERT MULTIPLE ELEMENTS USING SLICING")

numbers = [1, 2, 5]

numbers[2:2] = [3, 4]

print(numbers)


# ============================================================
# 62. REMOVE ALL OCCURRENCES
# ============================================================

print("\n62. REMOVE ALL OCCURRENCES")

numbers = [1, 2, 2, 3, 2, 4, 2]

numbers = [x for x in numbers if x != 2]

print(numbers)


# ============================================================
# 63. REMOVE DUPLICATES
# ============================================================

print("\n63. REMOVE DUPLICATES")

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))

print(unique)

# WARNING:
# set does not guarantee the original order.


# ============================================================
# 64. REMOVE DUPLICATES WHILE PRESERVING ORDER
# ============================================================

print("\n64. REMOVE DUPLICATES - PRESERVE ORDER")

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(dict.fromkeys(numbers))

print(unique)


# ============================================================
# 65. LIST OF LISTS -> FLATTEN
# ============================================================

print("\n65. FLATTEN NESTED LIST")

nested = [[1, 2], [3, 4], [5, 6]]

flat = [x for row in nested for x in row]

print(flat)


# ============================================================
# 66. CHECK EMPTY LIST
# ============================================================

print("\n66. CHECK EMPTY LIST")

numbers = []

if not numbers:
    print("List is empty")
else:
    print("List is not empty")


# ============================================================
# 67. MUTABILITY
# ============================================================

print("\n67. MUTABILITY")

numbers = [1, 2, 3]

numbers[0] = 100

print(numbers)

# Lists are MUTABLE.
# Their elements can be changed after creation.


# ============================================================
# 68. LIST CAN CONTAIN DIFFERENT TYPES
# ============================================================

print("\n68. MIXED TYPES")

data = [
    10,
    "Python",
    3.14,
    True,
    [1, 2, 3],
    {"name": "Alice"}
]

print(data)


# ============================================================
# 69. LIST OF OBJECTS / DICTIONARIES
# ============================================================

print("\n69. LIST OF DICTIONARIES")

students = [
    {"name": "Alice", "marks": 90},
    {"name": "Bob", "marks": 80},
    {"name": "Charlie", "marks": 95}
]

print(students[0]["name"])
print(students[1]["marks"])


# ============================================================
# 70. MODIFY DICTIONARY INSIDE LIST
# ============================================================

print("\n70. MODIFY DICTIONARY INSIDE LIST")

students[0]["marks"] = 98

print(students)


# ============================================================
# 71. FIND MAXIMUM USING key
# ============================================================

print("\n71. MAXIMUM USING key")

students = [
    {"name": "Alice", "marks": 90},
    {"name": "Bob", "marks": 80},
    {"name": "Charlie", "marks": 95}
]

topper = max(students, key=lambda x: x["marks"])

print(topper)


# ============================================================
# 72. FIND MINIMUM USING key
# ============================================================

print("\n72. MINIMUM USING key")

lowest = min(students, key=lambda x: x["marks"])

print(lowest)


# ============================================================
# 73. COPY LIST WITH + []
# ============================================================

print("\n73. COPY USING + []")

a = [1, 2, 3]

b = a + []

b.append(4)

print("a:", a)
print("b:", b)


# ============================================================
# 74. MEMBERSHIP IN NESTED LIST
# ============================================================

print("\n74. MEMBERSHIP IN NESTED LIST")

matrix = [
    [1, 2],
    [3, 4]
]

print([1, 2] in matrix)
print(1 in matrix)

# 1 is NOT directly an element of matrix.
# [1, 2] IS an element.


# ============================================================
# 75. LIST COMPARISON
# ============================================================

print("\n75. LIST COMPARISON")

a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 4]

print(a == b)
print(a == c)

print(a < c)

# Lists are compared lexicographically,
# similar to dictionary ordering.


# ============================================================
# 76. LIST AS STACK
# ============================================================

print("\n76. LIST AS STACK")

stack = []

stack.append("A")
stack.append("B")
stack.append("C")

print("Stack:", stack)

print("Pop:", stack.pop())
print("Stack:", stack)


# ============================================================
# 77. LIST AS QUEUE (BASIC)
# ============================================================

print("\n77. LIST AS QUEUE")

queue = []

queue.append("A")
queue.append("B")
queue.append("C")

print("Queue:", queue)

first = queue.pop(0)

print("Removed:", first)
print("Queue:", queue)

# For efficient queues, collections.deque is preferred.


# ============================================================
# 78. MEMORY / REFERENCE DEMONSTRATION
# ============================================================

print("\n78. REFERENCE DEMONSTRATION")

a = [1, 2, 3]
b = a

print("Before:", a, b)

a.append(4)

print("After:", a, b)

# Both change because both refer to the same object.


# ============================================================
# 79. PRACTICAL EXAMPLE
# ============================================================

print("\n79. PRACTICAL EXAMPLE")

marks = [78, 92, 65, 88, 95]

print("Marks:", marks)
print("Total:", sum(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks) / len(marks))

marks.sort(reverse=True)

print("Sorted marks:", marks)


# ============================================================
# 80. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("                    END OF LIST GUIDE")
print("=" * 70)