# ============================================================
#                  PYTHON TUPLE - COMPLETE GUIDE
# ============================================================

print("=" * 70)
print("                    PYTHON TUPLE")
print("=" * 70)


# ============================================================
# 1. CREATING TUPLES
# ============================================================

print("\n1. CREATING TUPLES")

# Empty tuple
empty = ()

# Tuple of integers
numbers = (10, 20, 30, 40, 50)

# Tuple of strings
names = ("Alice", "Bob", "Charlie")

# Mixed tuple
mixed = (10, "Python", 3.14, True, None)

# Nested tuple
nested = ((1, 2), (3, 4), (5, 6))

print("Empty:", empty)
print("Numbers:", numbers)
print("Names:", names)
print("Mixed:", mixed)
print("Nested:", nested)


# ============================================================
# 2. TUPLE USING tuple()
# ============================================================

print("\n2. USING tuple()")

a = tuple([1, 2, 3, 4])
b = tuple("Python")
c = tuple(range(1, 6))

print(a)
print(b)
print(c)


# ============================================================
# 3. INDEXING
# ============================================================

print("\n3. INDEXING")

numbers = (10, 20, 30, 40, 50)

print("Tuple:", numbers)

print("First:", numbers[0])
print("Second:", numbers[1])
print("Last:", numbers[-1])
print("Second last:", numbers[-2])


# Positive indexes:
#
#    0    1    2    3    4
# [ 10,  20,  30,  40,  50 ]
#
# Negative indexes:
#
#   -5   -4   -3   -2   -1
# [ 10,  20,  30,  40,  50 ]


# ============================================================
# 4. IMMUTABILITY
# ============================================================

print("\n4. IMMUTABILITY")

numbers = (10, 20, 30)

print("Original:", numbers)

# This would cause TypeError:
#
# numbers[0] = 100

print("Tuple elements cannot be changed directly.")


# ============================================================
# 5. SLICING
# ============================================================

print("\n5. SLICING")

numbers = (10, 20, 30, 40, 50)

print("Original:", numbers)

print("numbers[1:4]:", numbers[1:4])
print("numbers[:3]:", numbers[:3])
print("numbers[2:]:", numbers[2:])
print("numbers[:]:", numbers[:])

print("Every second:", numbers[::2])
print("Reverse:", numbers[::-1])

# Syntax:
#
# tuple[start : stop : step]
#
# stop is NOT included.


# ============================================================
# 6. LENGTH
# ============================================================

print("\n6. len()")

numbers = (10, 20, 30, 40)

print("Length:", len(numbers))


# ============================================================
# 7. MEMBERSHIP
# ============================================================

print("\n7. MEMBERSHIP")

numbers = (10, 20, 30, 40)

print("20 in tuple:", 20 in numbers)
print("100 in tuple:", 100 in numbers)

print("20 not in tuple:", 20 not in numbers)
print("100 not in tuple:", 100 not in numbers)


# ============================================================
# 8. index()
# ============================================================

print("\n8. index()")

numbers = (10, 20, 30, 20, 40)

print("First index of 20:", numbers.index(20))


# ============================================================
# 9. count()
# ============================================================

print("\n9. count()")

numbers = (10, 20, 20, 30, 20, 40)

print("Number of 20s:", numbers.count(20))


# ============================================================
# 10. min(), max(), sum()
# ============================================================

print("\n10. min(), max(), sum()")

numbers = (10, 20, 30, 40, 50)

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))


# ============================================================
# 11. CONCATENATION
# ============================================================

print("\n11. CONCATENATION")

a = (1, 2, 3)
b = (4, 5, 6)

c = a + b

print("a:", a)
print("b:", b)
print("a + b:", c)


# ============================================================
# 12. REPETITION
# ============================================================

print("\n12. REPETITION")

numbers = (1, 2, 3)

print(numbers * 3)


# ============================================================
# 13. SINGLE ELEMENT TUPLE
# ============================================================

print("\n13. SINGLE ELEMENT TUPLE")

a = (10,)

print(a)
print(type(a))

# IMPORTANT:
#
# (10) is NOT a tuple.
# (10,) IS a tuple.


# ============================================================
# 14. WHY COMMA MATTERS
# ============================================================

print("\n14. COMMA CREATES TUPLE")

a = (10)

b = (10,)

print("a:", a)
print("type(a):", type(a))

print("b:", b)
print("type(b):", type(b))


# ============================================================
# 15. PARENTHESIS ARE OPTIONAL
# ============================================================

print("\n15. TUPLE WITHOUT PARENTHESES")

a = 10, 20, 30

print(a)
print(type(a))


# ============================================================
# 16. TUPLE PACKING
# ============================================================

print("\n16. TUPLE PACKING")

numbers = 10, 20, 30, 40

print(numbers)
print(type(numbers))


# ============================================================
# 17. TUPLE UNPACKING
# ============================================================

print("\n17. TUPLE UNPACKING")

numbers = (10, 20, 30)

a, b, c = numbers

print("a:", a)
print("b:", b)
print("c:", c)


# ============================================================
# 18. UNPACKING MUST MATCH
# ============================================================

print("\n18. UNPACKING COUNT")

numbers = (10, 20, 30)

a, b, c = numbers

print(a, b, c)

# This would cause ValueError:
#
# a, b = numbers
#
# because there are 3 values but only 2 variables.


# ============================================================
# 19. STAR UNPACKING
# ============================================================

print("\n19. STAR UNPACKING")

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# ============================================================
# 20. STAR UNPACKING AT BEGINNING
# ============================================================

print("\n20. STAR UNPACKING")

numbers = (10, 20, 30, 40, 50)

*beginning, last = numbers

print("Beginning:", beginning)
print("Last:", last)


# ============================================================
# 21. STAR UNPACKING AT END
# ============================================================

print("\n21. STAR UNPACKING AT END")

numbers = (10, 20, 30, 40, 50)

first, *remaining = numbers

print("First:", first)
print("Remaining:", remaining)


# ============================================================
# 22. LOOP THROUGH TUPLE
# ============================================================

print("\n22. FOR LOOP")

numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)


# ============================================================
# 23. LOOP WITH INDEX
# ============================================================

print("\n23. LOOP WITH INDEX")

numbers = (10, 20, 30, 40)

for i in range(len(numbers)):
    print("Index:", i, "Value:", numbers[i])


# ============================================================
# 24. enumerate()
# ============================================================

print("\n24. enumerate()")

numbers = (10, 20, 30, 40)

for index, value in enumerate(numbers):
    print(index, value)


# ============================================================
# 25. NESTED TUPLE
# ============================================================

print("\n25. NESTED TUPLE")

data = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(data)

print("First row:", data[0])
print("First element:", data[0][0])
print("Second row, third element:", data[1][2])


# ============================================================
# 26. MODIFYING NESTED TUPLE
# ============================================================

print("\n26. NESTED TUPLE")

data = (
    [1, 2],
    [3, 4]
)

# The tuple itself is immutable.
#
# But the LIST INSIDE the tuple is mutable.

data[0][0] = 100

print(data)


# ============================================================
# 27. IMPORTANT IMMUTABILITY CONFUSION
# ============================================================

print("\n27. IMMUTABLE TUPLE CONTAINING MUTABLE OBJECT")

data = ([1, 2], [3, 4])

print("Before:", data)

data[0].append(100)

print("After:", data)

# The tuple structure did not change.
# The list inside the tuple changed.


# ============================================================
# 28. TUPLE COMPARISON
# ============================================================

print("\n28. COMPARISON")

a = (1, 2, 3)
b = (1, 2, 3)
c = (1, 2, 4)

print("a == b:", a == b)
print("a == c:", a == c)

print("a < c:", a < c)


# ============================================================
# 29. == VS is
# ============================================================

print("\n29. == VS is")

a = (1, 2, 3)
b = (1, 2, 3)

print("a == b:", a == b)
print("a is b:", a is b)


# ============================================================
# 30. SORTING A TUPLE
# ============================================================

print("\n30. SORTING")

numbers = (50, 10, 40, 20, 30)

sorted_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)


# IMPORTANT:
#
# Tuple does NOT have sort().
#
# sorted(tuple) returns a LIST.


# ============================================================
# 31. REVERSE A TUPLE
# ============================================================

print("\n31. REVERSE")

numbers = (10, 20, 30, 40)

reversed_numbers = numbers[::-1]

print("Original:", numbers)
print("Reversed:", reversed_numbers)


# ============================================================
# 32. sorted() WITH reverse=True
# ============================================================

print("\n32. DESCENDING SORT")

numbers = (10, 50, 20, 40, 30)

result = sorted(numbers, reverse=True)

print(result)


# ============================================================
# 33. CONVERT TUPLE TO LIST
# ============================================================

print("\n33. TUPLE -> LIST")

numbers = (10, 20, 30)

numbers_list = list(numbers)

print(numbers_list)


# ============================================================
# 34. CONVERT LIST TO TUPLE
# ============================================================

print("\n34. LIST -> TUPLE")

numbers = [10, 20, 30]

numbers_tuple = tuple(numbers)

print(numbers_tuple)


# ============================================================
# 35. MODIFY TUPLE THROUGH LIST CONVERSION
# ============================================================

print("\n35. MODIFY THROUGH CONVERSION")

numbers = (10, 20, 30)

temp = list(numbers)

temp.append(40)
temp[0] = 100

numbers = tuple(temp)

print(numbers)


# ============================================================
# 36. TUPLE AS DICTIONARY KEY
# ============================================================

print("\n36. TUPLE AS DICTIONARY KEY")

locations = {
    (26.9, 75.8): "Jaipur",
    (28.6, 77.2): "Delhi"
}

print(locations[(26.9, 75.8)])


# ============================================================
# 37. TUPLE AS SET ELEMENT
# ============================================================

print("\n37. TUPLE INSIDE SET")

data = {
    (1, 2),
    (3, 4),
    (5, 6)
}

print(data)


# ============================================================
# 38. HASHING
# ============================================================

print("\n38. HASHING")

numbers = (1, 2, 3)

print("Hash:", hash(numbers))

# Immutable tuples containing hashable elements
# can be hashed.


# ============================================================
# 39. TUPLE WITH DICTIONARY
# ============================================================

print("\n39. TUPLE WITH DICTIONARY")

student = ("Alice", 21, {"Math": 90, "Python": 95})

print(student)

print("Name:", student[0])
print("Age:", student[1])
print("Marks:", student[2])


# ============================================================
# 40. MODIFY MUTABLE OBJECT INSIDE TUPLE
# ============================================================

print("\n40. MODIFY DICTIONARY INSIDE TUPLE")

student = ("Alice", 21, {"Math": 90})

student[2]["Math"] = 98

print(student)


# ============================================================
# 41. any() and all()
# ============================================================

print("\n41. any() AND all()")

numbers = (2, 4, 6, 8)

print("Any > 5:", any(x > 5 for x in numbers))
print("All even:", all(x % 2 == 0 for x in numbers))


# ============================================================
# 42. zip()
# ============================================================

print("\n42. zip()")

names = ("Alice", "Bob", "Charlie")
marks = (90, 85, 95)

for name, mark in zip(names, marks):
    print(name, mark)


# ============================================================
# 43. LIST OF TUPLES
# ============================================================

print("\n43. LIST OF TUPLES")

students = [
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
]

print(students)

print("First student:", students[0])
print("First student's name:", students[0][0])
print("First student's marks:", students[0][1])


# ============================================================
# 44. SORT LIST OF TUPLES
# ============================================================

print("\n44. SORT LIST OF TUPLES")

students = [
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
]

students.sort(key=lambda x: x[1])

print(students)


# ============================================================
# 45. MAXIMUM FROM TUPLES
# ============================================================

print("\n45. MAXIMUM")

students = (
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
)

topper = max(students, key=lambda x: x[1])

print(topper)


# ============================================================
# 46. MINIMUM FROM TUPLES
# ============================================================

print("\n46. MINIMUM")

lowest = min(students, key=lambda x: x[1])

print(lowest)


# ============================================================
# 47. TUPLE COMPREHENSION CONFUSION
# ============================================================

print("\n47. TUPLE COMPREHENSION CONFUSION")

numbers = (1, 2, 3, 4, 5)

# This is NOT a tuple comprehension.
result = (x * x for x in numbers)

print(result)

# It creates a GENERATOR.
#
# To create a tuple:
#
# result = tuple(x * x for x in numbers)

result = tuple(x * x for x in numbers)

print(result)


# ============================================================
# 48. GENERATOR VS TUPLE
# ============================================================

print("\n48. GENERATOR VS TUPLE")

numbers = (1, 2, 3)

generator = (x * 2 for x in numbers)
tuple_result = tuple(x * 2 for x in numbers)

print("Generator:", generator)
print("Tuple:", tuple_result)


# ============================================================
# 49. FUNCTION RETURNING MULTIPLE VALUES
# ============================================================

print("\n49. FUNCTION RETURNING MULTIPLE VALUES")


def get_student():
    name = "Alice"
    age = 21
    marks = 95

    return name, age, marks


student = get_student()

print(student)
print(type(student))


# ============================================================
# 50. UNPACK FUNCTION RETURN VALUE
# ============================================================

print("\n50. UNPACK FUNCTION RESULT")

name, age, marks = get_student()

print("Name:", name)
print("Age:", age)
print("Marks:", marks)


# ============================================================
# 51. SWAPPING VARIABLES
# ============================================================

print("\n51. VARIABLE SWAPPING")

a = 10
b = 20

print("Before:", a, b)

a, b = b, a

print("After:", a, b)


# ============================================================
# 52. TUPLE OF MIXED DATA
# ============================================================

print("\n52. MIXED DATA")

data = (
    10,
    "Python",
    3.14,
    True,
    None,
    [1, 2, 3],
    {"name": "Alice"}
)

print(data)


# ============================================================
# 53. CHECK EMPTY TUPLE
# ============================================================

print("\n53. CHECK EMPTY")

data = ()

if not data:
    print("Tuple is empty")
else:
    print("Tuple is not empty")


# ============================================================
# 54. TUPLE LENGTH
# ============================================================

print("\n54. LENGTH")

data = (10, 20, 30)

print(len(data))


# ============================================================
# 55. NESTED UNPACKING
# ============================================================

print("\n55. NESTED UNPACKING")

student = ("Alice", (90, 95, 88))

name, (math, python, science) = student

print("Name:", name)
print("Math:", math)
print("Python:", python)
print("Science:", science)


# ============================================================
# 56. ENUMERATE
# ============================================================

print("\n56. ENUMERATE")

colors = ("red", "green", "blue")

for index, color in enumerate(colors, start=1):
    print(index, color)


# ============================================================
# 57. REVERSED()
# ============================================================

print("\n57. reversed()")

numbers = (1, 2, 3, 4)

result = tuple(reversed(numbers))

print(result)


# ============================================================
# 58. FILTER
# ============================================================

print("\n58. filter()")

numbers = (1, 2, 3, 4, 5, 6)

even = tuple(filter(lambda x: x % 2 == 0, numbers))

print(even)


# ============================================================
# 59. MAP
# ============================================================

print("\n59. map()")

numbers = (1, 2, 3, 4)

squares = tuple(map(lambda x: x * x, numbers))

print(squares)


# ============================================================
# 60. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("                 END OF TUPLE GUIDE")
print("=" * 70)