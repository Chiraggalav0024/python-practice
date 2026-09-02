# ============================================================
#                PYTHON DICTIONARY - COMPLETE GUIDE
# ============================================================

print("=" * 70)
print("                  PYTHON DICTIONARY")
print("=" * 70)


# ============================================================
# 1. CREATING DICTIONARIES
# ============================================================

print("\n1. CREATING DICTIONARIES")

empty = {}

student = {
    "name": "Alice",
    "age": 21,
    "marks": 95
}

print("Empty:", empty)
print("Student:", student)


# ============================================================
# 2. dict() CONSTRUCTOR
# ============================================================

print("\n2. USING dict()")

student = dict(
    name="Alice",
    age=21,
    marks=95
)

print(student)


# ============================================================
# 3. DICTIONARY WITH DIFFERENT VALUE TYPES
# ============================================================

print("\n3. DIFFERENT VALUE TYPES")

data = {
    "name": "Alice",
    "age": 21,
    "percentage": 92.5,
    "passed": True,
    "skills": ["Python", "Java"],
    "address": {
        "city": "Jaipur",
        "country": "India"
    }
}

print(data)


# ============================================================
# 4. ACCESSING VALUES
# ============================================================

print("\n4. ACCESSING VALUES")

student = {
    "name": "Alice",
    "age": 21,
    "marks": 95
}

print(student["name"])
print(student["age"])
print(student["marks"])


# ============================================================
# 5. ACCESSING NON-EXISTING KEY
# ============================================================

print("\n5. NON-EXISTING KEY")

student = {
    "name": "Alice",
    "age": 21
}

# This causes KeyError:
#
# print(student["marks"])

print("Accessing a missing key with [] causes KeyError.")


# ============================================================
# 6. get()
# ============================================================

print("\n6. get()")

student = {
    "name": "Alice",
    "age": 21
}

print(student.get("name"))
print(student.get("marks"))


# ============================================================
# 7. get() WITH DEFAULT VALUE
# ============================================================

print("\n7. get() WITH DEFAULT")

student = {
    "name": "Alice",
    "age": 21
}

print(student.get("marks", 0))
print(student.get("city", "Unknown"))


# ============================================================
# 8. [] VS get()
# ============================================================

print("\n8. [] VS get()")

student = {
    "name": "Alice"
}

print(student["name"])
print(student.get("name"))

print(student.get("age"))
print(student.get("age", 0))

# student["age"]
# would cause KeyError.


# ============================================================
# 9. ADDING A NEW KEY
# ============================================================

print("\n9. ADDING NEW KEY")

student = {
    "name": "Alice",
    "age": 21
}

student["marks"] = 95

print(student)


# ============================================================
# 10. MODIFYING A VALUE
# ============================================================

print("\n10. MODIFYING VALUE")

student = {
    "name": "Alice",
    "age": 21,
    "marks": 90
}

student["marks"] = 95

print(student)


# ============================================================
# 11. ADD OR UPDATE
# ============================================================

print("\n11. ADD OR UPDATE")

student = {}

student["name"] = "Alice"

# If key doesn't exist -> adds it
# If key already exists -> updates it

student["name"] = "Bob"

print(student)


# ============================================================
# 12. CHECKING KEY
# ============================================================

print("\n12. KEY MEMBERSHIP")

student = {
    "name": "Alice",
    "age": 21
}

print("name" in student)
print("marks" in student)

print("marks" not in student)


# ============================================================
# 13. IMPORTANT: in CHECKS KEYS
# ============================================================

print("\n13. in CHECKS KEYS")

student = {
    "name": "Alice",
    "age": 21
}

print("name" in student)
print("Alice" in student)

# "name" -> True
# "Alice" -> False
#
# because "in" checks keys by default.


# ============================================================
# 14. len()
# ============================================================

print("\n14. len()")

student = {
    "name": "Alice",
    "age": 21,
    "marks": 95
}

print(len(student))


# ============================================================
# 15. keys()
# ============================================================

print("\n15. keys()")

student = {
    "name": "Alice",
    "age": 21,
    "marks": 95
}

print(student.keys())


# ============================================================
# 16. values()
# ============================================================

print("\n16. values()")

student = {
    "name": "Alice",
    "age": 21,
    "marks": 95
}

print(student.values())


# ============================================================
# 17. items()
# ============================================================

print("\n17. items()")

student = {
    "name": "Alice",
    "age": 21,
    "marks": 95
}

print(student.items())


# ============================================================
# 18. LOOP THROUGH KEYS
# ============================================================

print("\n18. LOOP THROUGH KEYS")

student = {
    "name": "Alice",
    "age": 21,
    "marks": 95
}

for key in student:
    print(key)


# ============================================================
# 19. LOOP THROUGH VALUES
# ============================================================

print("\n19. LOOP THROUGH VALUES")

for value in student.values():
    print(value)


# ============================================================
# 20. LOOP THROUGH KEY-VALUE PAIRS
# ============================================================

print("\n20. LOOP THROUGH ITEMS")

for key, value in student.items():
    print(key, "=", value)


# ============================================================
# 21. UPDATE()
# ============================================================

print("\n21. update()")

student = {
    "name": "Alice",
    "age": 21
}

student.update({
    "age": 22,
    "marks": 95
})

print(student)


# ============================================================
# 22. update() WITH KEYWORD ARGUMENTS
# ============================================================

print("\n22. update() KEYWORD")

student = {
    "name": "Alice"
}

student.update(age=21, marks=95)

print(student)


# ============================================================
# 23. SETDEFAULT()
# ============================================================

print("\n23. setdefault()")

student = {
    "name": "Alice",
    "age": 21
}

student.setdefault("city", "Jaipur")

print(student)


# ============================================================
# 24. SETDEFAULT() EXISTING KEY
# ============================================================

print("\n24. setdefault() EXISTING")

student = {
    "name": "Alice",
    "age": 21
}

result = student.setdefault("age", 100)

print("Returned:", result)
print("Dictionary:", student)


# ============================================================
# 25. pop()
# ============================================================

print("\n25. pop()")

student = {
    "name": "Alice",
    "age": 21,
    "marks": 95
}

removed = student.pop("age")

print("Removed:", removed)
print("Dictionary:", student)


# ============================================================
# 26. pop() DEFAULT VALUE
# ============================================================

print("\n26. pop() DEFAULT")

student = {
    "name": "Alice"
}

result = student.pop("age", 0)

print(result)
print(student)


# ============================================================
# 27. popitem()
# ============================================================

print("\n27. popitem()")

student = {
    "name": "Alice",
    "age": 21,
    "marks": 95
}

item = student.popitem()

print("Removed:", item)
print("Dictionary:", student)


# ============================================================
# 28. clear()
# ============================================================

print("\n28. clear()")

student = {
    "name": "Alice",
    "age": 21
}

student.clear()

print(student)


# ============================================================
# 29. del KEY
# ============================================================

print("\n29. del")

student = {
    "name": "Alice",
    "age": 21
}

del student["age"]

print(student)


# ============================================================
# 30. del ENTIRE DICTIONARY
# ============================================================

print("\n30. DELETE DICTIONARY")

student = {
    "name": "Alice"
}

del student

print("Dictionary variable deleted.")


# ============================================================
# 31. COPY
# ============================================================

print("\n31. copy()")

student = {
    "name": "Alice",
    "age": 21
}

copy_student = student.copy()

copy_student["age"] = 22

print("Original:", student)
print("Copy:", copy_student)


# ============================================================
# 32. ALIASING
# ============================================================

print("\n32. ALIASING")

student = {
    "name": "Alice",
    "age": 21
}

other = student

other["age"] = 25

print("student:", student)
print("other:", other)

# Both refer to the same dictionary.


# ============================================================
# 33. == VS is
# ============================================================

print("\n33. == VS is")

a = {
    "name": "Alice"
}

b = {
    "name": "Alice"
}

print("a == b:", a == b)
print("a is b:", a is b)


# ============================================================
# 34. NESTED DICTIONARY
# ============================================================

print("\n34. NESTED DICTIONARY")

student = {
    "name": "Alice",
    "marks": {
        "math": 90,
        "python": 95,
        "java": 88
    }
}

print(student)

print(student["marks"])
print(student["marks"]["python"])


# ============================================================
# 35. MODIFY NESTED DICTIONARY
# ============================================================

print("\n35. MODIFY NESTED DICTIONARY")

student = {
    "name": "Alice",
    "marks": {
        "math": 90,
        "python": 95
    }
}

student["marks"]["math"] = 98

print(student)


# ============================================================
# 36. DICTIONARY WITH LIST
# ============================================================

print("\n36. DICTIONARY WITH LIST")

student = {
    "name": "Alice",
    "skills": ["Python", "Java"]
}

student["skills"].append("SQL")

print(student)


# ============================================================
# 37. DICTIONARY WITH TUPLE
# ============================================================

print("\n37. DICTIONARY WITH TUPLE")

student = {
    "name": "Alice",
    "coordinates": (26.9, 75.8)
}

print(student)


# ============================================================
# 38. DICTIONARY OF LISTS
# ============================================================

print("\n38. DICTIONARY OF LISTS")

students = {
    "Alice": [90, 95, 88],
    "Bob": [80, 85, 90]
}

print(students)

print(students["Alice"])


# ============================================================
# 39. DICTIONARY OF DICTIONARIES
# ============================================================

print("\n39. DICTIONARY OF DICTIONARIES")

students = {
    "student1": {
        "name": "Alice",
        "marks": 95
    },
    "student2": {
        "name": "Bob",
        "marks": 85
    }
}

print(students["student1"]["name"])
print(students["student2"]["marks"])


# ============================================================
# 40. LIST OF DICTIONARIES
# ============================================================

print("\n40. LIST OF DICTIONARIES")

students = [
    {"name": "Alice", "marks": 95},
    {"name": "Bob", "marks": 85},
    {"name": "Charlie", "marks": 90}
]

print(students)

print(students[0])
print(students[0]["name"])
print(students[0]["marks"])


# ============================================================
# 41. DICTIONARY COMPREHENSION
# ============================================================

print("\n41. DICTIONARY COMPREHENSION")

numbers = range(1, 6)

squares = {
    x: x * x
    for x in numbers
}

print(squares)


# ============================================================
# 42. DICTIONARY COMPREHENSION WITH CONDITION
# ============================================================

print("\n42. DICTIONARY COMPREHENSION CONDITION")

numbers = range(1, 11)

even_squares = {
    x: x * x
    for x in numbers
    if x % 2 == 0
}

print(even_squares)


# ============================================================
# 43. DICTIONARY FROM TWO LISTS
# ============================================================

print("\n43. zip()")

names = ["Alice", "Bob", "Charlie"]
marks = [90, 85, 95]

student_marks = dict(zip(names, marks))

print(student_marks)


# ============================================================
# 44. DICTIONARY FROM TUPLE PAIRS
# ============================================================

print("\n44. DICTIONARY FROM PAIRS")

data = [
    ("name", "Alice"),
    ("age", 21),
    ("marks", 95)
]

student = dict(data)

print(student)


# ============================================================
# 45. FROMKEYS()
# ============================================================

print("\n45. fromkeys()")

keys = ["name", "age", "marks"]

student = dict.fromkeys(keys)

print(student)


# ============================================================
# 46. FROMKEYS() WITH DEFAULT
# ============================================================

print("\n46. fromkeys() DEFAULT")

keys = ["math", "python", "java"]

marks = dict.fromkeys(keys, 0)

print(marks)


# ============================================================
# 47. COPYING WITH dict()
# ============================================================

print("\n47. dict() COPY")

a = {
    "name": "Alice",
    "age": 21
}

b = dict(a)

b["age"] = 25

print("a:", a)
print("b:", b)


# ============================================================
# 48. SORTING KEYS
# ============================================================

print("\n48. SORTING KEYS")

student = {
    "z": 1,
    "a": 2,
    "m": 3
}

for key in sorted(student):
    print(key, student[key])


# ============================================================
# 49. SORTING ITEMS BY VALUE
# ============================================================

print("\n49. SORTING BY VALUE")

students = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 95
}

sorted_students = sorted(
    students.items(),
    key=lambda item: item[1]
)

print(sorted_students)


# ============================================================
# 50. SORTING ITEMS BY VALUE DESCENDING
# ============================================================

print("\n50. DESCENDING SORT")

students = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 95
}

sorted_students = sorted(
    students.items(),
    key=lambda item: item[1],
    reverse=True
)

print(sorted_students)


# ============================================================
# 51. MAX VALUE
# ============================================================

print("\n51. MAX")

students = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 95
}

topper = max(
    students,
    key=students.get
)

print(topper)
print(students[topper])


# ============================================================
# 52. MIN VALUE
# ============================================================

print("\n52. MIN")

lowest = min(
    students,
    key=students.get
)

print(lowest)
print(students[lowest])


# ============================================================
# 53. DICTIONARY WITH INTEGER KEYS
# ============================================================

print("\n53. INTEGER KEYS")

data = {
    1: "One",
    2: "Two",
    3: "Three"
}

print(data[1])


# ============================================================
# 54. TUPLE KEYS
# ============================================================

print("\n54. TUPLE KEYS")

locations = {
    (26.9, 75.8): "Jaipur",
    (28.6, 77.2): "Delhi"
}

print(locations[(26.9, 75.8)])


# ============================================================
# 55. LIST AS KEY - INVALID
# ============================================================

print("\n55. LIST AS KEY")

# This is invalid:
#
# data = {
#     [1, 2]: "value"
# }

print("Lists cannot be dictionary keys.")


# ============================================================
# 56. KEY MUST BE HASHABLE
# ============================================================

print("\n56. HASHABLE KEYS")

data = {
    "name": "Alice",
    1: "Number",
    (1, 2): "Tuple"
}

print(data)


# ============================================================
# 57. DUPLICATE KEYS
# ============================================================

print("\n57. DUPLICATE KEYS")

data = {
    "name": "Alice",
    "name": "Bob"
}

print(data)

# Last value wins.


# ============================================================
# 58. DUPLICATE KEY CONFUSION
# ============================================================

print("\n58. DUPLICATE KEY")

data = {}

data["name"] = "Alice"
data["name"] = "Bob"

print(data)


# ============================================================
# 59. SETDEFAULT VS GET
# ============================================================

print("\n59. setdefault() VS get()")

data = {}

print(data.get("name", "Alice"))

print("After get:", data)

data.setdefault("name", "Alice")

print("After setdefault:", data)


# ============================================================
# 60. MERGING DICTIONARIES USING |
# ============================================================

print("\n60. MERGING USING |")

a = {
    "name": "Alice",
    "age": 21
}

b = {
    "age": 22,
    "marks": 95
}

result = a | b

print(result)


# ============================================================
# 61. UPDATE USING |=
# ============================================================

print("\n61. MERGING USING |=")

a = {
    "name": "Alice",
    "age": 21
}

b = {
    "marks": 95
}

a |= b

print(a)


# ============================================================
# 62. DICTIONARY UNPACKING
# ============================================================

print("\n62. DICTIONARY UNPACKING")

a = {
    "name": "Alice"
}

b = {
    "age": 21
}

result = {
    **a,
    **b
}

print(result)


# ============================================================
# 63. DICTIONARY UNPACKING CONFLICT
# ============================================================

print("\n63. UNPACKING CONFLICT")

a = {
    "name": "Alice",
    "age": 21
}

b = {
    "name": "Bob",
    "marks": 95
}

result = {
    **a,
    **b
}

print(result)

# Later values override earlier values.


# ============================================================
# 64. NESTED LOOP
# ============================================================

print("\n64. NESTED DICTIONARY LOOP")

students = {
    "Alice": {
        "math": 90,
        "python": 95
    },
    "Bob": {
        "math": 80,
        "python": 85
    }
}

for student, subjects in students.items():

    print(student)

    for subject, marks in subjects.items():
        print(" ", subject, "=", marks)


# ============================================================
# 65. CHECK VALUE
# ============================================================

print("\n65. CHECK VALUE")

student = {
    "name": "Alice",
    "age": 21
}

print("Alice" in student.values())
print(21 in student.values())


# ============================================================
# 66. CHECK KEY-VALUE PAIR
# ============================================================

print("\n66. CHECK ITEM")

student = {
    "name": "Alice",
    "age": 21
}

print(("name", "Alice") in student.items())
print(("age", 25) in student.items())


# ============================================================
# 67. COPY NESTED DICTIONARY
# ============================================================

print("\n67. SHALLOW COPY")

student = {
    "name": "Alice",
    "marks": {
        "math": 90
    }
}

copy_student = student.copy()

copy_student["marks"]["math"] = 100

print("Original:", student)
print("Copy:", copy_student)


# ============================================================
# 68. DEEPCOPY
# ============================================================

print("\n68. DEEP COPY")

import copy

student = {
    "name": "Alice",
    "marks": {
        "math": 90
    }
}

copy_student = copy.deepcopy(student)

copy_student["marks"]["math"] = 100

print("Original:", student)
print("Copy:", copy_student)


# ============================================================
# 69. PRACTICAL API-LIKE DATA
# ============================================================

print("\n69. API-LIKE DATA")

user = {
    "id": 101,
    "username": "alice",
    "email": "alice@example.com",
    "active": True,
    "roles": ["user", "admin"]
}

print(user["username"])
print(user["roles"])


# ============================================================
# 70. PRACTICAL FARM DATA
# ============================================================

print("\n70. PRACTICAL FARM DATA")

farm = {
    "farmer": "Ravi",
    "location": {
        "latitude": 26.9,
        "longitude": 75.8
    },
    "crops": ["Tomato", "Wheat"],
    "soil": {
        "ph": 6.8,
        "moisture": 42
    }
}

print("Farmer:", farm["farmer"])
print("Crops:", farm["crops"])
print("Soil pH:", farm["soil"]["ph"])
print("Moisture:", farm["soil"]["moisture"])


# ============================================================
# 71. MODIFY PRACTICAL DATA
# ============================================================

print("\n71. MODIFY PRACTICAL DATA")

farm["soil"]["moisture"] = 55
farm["crops"].append("Mustard")

print(farm)


# ============================================================
# 72. DELETE NESTED DATA
# ============================================================

print("\n72. DELETE NESTED DATA")

farm = {
    "name": "Farm A",
    "soil": {
        "ph": 6.5,
        "moisture": 40
    }
}

del farm["soil"]["ph"]

print(farm)


# ============================================================
# 73. BUILD DICTIONARY USING LOOP
# ============================================================

print("\n73. BUILD USING LOOP")

squares = {}

for x in range(1, 6):
    squares[x] = x * x

print(squares)


# ============================================================
# 74. INVERT DICTIONARY
# ============================================================

print("\n74. INVERT DICTIONARY")

data = {
    "a": 1,
    "b": 2,
    "c": 3
}

inverted = {
    value: key
    for key, value in data.items()
}

print(inverted)


# ============================================================
# 75. FILTER DICTIONARY
# ============================================================

print("\n75. FILTER DICTIONARY")

marks = {
    "Alice": 90,
    "Bob": 70,
    "Charlie": 95,
    "David": 60
}

passed = {
    name: mark
    for name, mark in marks.items()
    if mark >= 75
}

print(passed)


# ============================================================
# 76. DICTIONARY LENGTH
# ============================================================

print("\n76. LENGTH")

data = {
    "a": 1,
    "b": 2,
    "c": 3
}

print(len(data))


# ============================================================
# 77. EMPTY DICTIONARY CHECK
# ============================================================

print("\n77. EMPTY CHECK")

data = {}

if not data:
    print("Dictionary is empty")


# ============================================================
# 78. CLEAR
# ============================================================

print("\n78. CLEAR")

data = {
    "a": 1,
    "b": 2
}

data.clear()

print(data)


# ============================================================
# 79. PRACTICAL COUNTING
# ============================================================

print("\n79. COUNT FREQUENCY")

numbers = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)


# ============================================================
# 80. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("              END OF DICTIONARY GUIDE")
print("=" * 70)