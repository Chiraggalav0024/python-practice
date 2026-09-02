# ============================================================
#                    PYTHON SET - COMPLETE GUIDE
# ============================================================

print("=" * 70)
print("                     PYTHON SET")
print("=" * 70)


# ============================================================
# 1. CREATING SETS
# ============================================================

print("\n1. CREATING SETS")

# Empty set
empty = set()

# Set of integers
numbers = {10, 20, 30, 40, 50}

# Set of strings
names = {"Alice", "Bob", "Charlie"}

# Mixed data types
mixed = {10, "Python", 3.14, True}

print("Empty:", empty)
print("Numbers:", numbers)
print("Names:", names)
print("Mixed:", mixed)


# ============================================================
# 2. DUPLICATES ARE AUTOMATICALLY REMOVED
# ============================================================

print("\n2. DUPLICATES")

numbers = {10, 20, 20, 30, 30, 30, 40}

print(numbers)

# Duplicate values are automatically removed.


# ============================================================
# 3. SET USING set()
# ============================================================

print("\n3. USING set()")

a = set([1, 2, 3, 4])
b = set((10, 20, 30))
c = set("hello")

print(a)
print(b)
print(c)

# Notice:
# set("hello")
# becomes something like:
#
# {'h', 'e', 'l', 'o'}
#
# Duplicate 'l' is removed.


# ============================================================
# 4. EMPTY SET CONFUSION
# ============================================================

print("\n4. EMPTY SET CONFUSION")

a = set()

print(a)
print(type(a))

# IMPORTANT:
#
# {} is NOT an empty set.
# {} is an empty dictionary.
#
# set() creates an empty set.


# ============================================================
# 5. TYPE
# ============================================================

print("\n5. TYPE")

numbers = {1, 2, 3}

print(type(numbers))


# ============================================================
# 6. SET IS UNORDERED
# ============================================================

print("\n6. UNORDERED")

numbers = {10, 20, 30, 40, 50}

print(numbers)

# Do NOT depend on the displayed order.


# ============================================================
# 7. NO INDEXING
# ============================================================

print("\n7. NO INDEXING")

numbers = {10, 20, 30}

# This is NOT allowed:
#
# print(numbers[0])
#
# Sets do not support indexing.


# ============================================================
# 8. NO SLICING
# ============================================================

print("\n8. NO SLICING")

numbers = {10, 20, 30, 40}

# This is NOT allowed:
#
# numbers[1:3]

print("Sets do not support slicing.")


# ============================================================
# 9. MEMBERSHIP
# ============================================================

print("\n9. MEMBERSHIP")

numbers = {10, 20, 30, 40}

print(20 in numbers)
print(100 in numbers)

print(20 not in numbers)
print(100 not in numbers)


# ============================================================
# 10. len()
# ============================================================

print("\n10. len()")

numbers = {10, 20, 30, 40}

print("Length:", len(numbers))


# ============================================================
# 11. add()
# ============================================================

print("\n11. add()")

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)


# ============================================================
# 12. add() DUPLICATE
# ============================================================

print("\n12. add() DUPLICATE")

numbers = {10, 20, 30}

numbers.add(20)

print(numbers)

# Nothing changes because 20 already exists.


# ============================================================
# 13. update()
# ============================================================

print("\n13. update()")

numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)


# ============================================================
# 14. add() VS update()
# ============================================================

print("\n14. add() VS update()")

a = {1, 2}

a.add((3, 4))

print("Using add:", a)


b = {1, 2}

b.update((3, 4))

print("Using update:", b)

# add((3,4))
# adds the tuple as ONE element.
#
# update((3,4))
# adds 3 and 4 separately.


# ============================================================
# 15. update() WITH STRING
# ============================================================

print("\n15. update() WITH STRING")

numbers = {1, 2}

numbers.update("abc")

print(numbers)

# Strings are iterable.
#
# Therefore:
# "abc" -> 'a', 'b', 'c'


# ============================================================
# 16. update() WITH MULTIPLE ITERABLES
# ============================================================

print("\n16. update() MULTIPLE VALUES")

numbers = {1, 2}

numbers.update([3, 4], (5, 6), {7, 8})

print(numbers)


# ============================================================
# 17. remove()
# ============================================================

print("\n17. remove()")

numbers = {10, 20, 30, 40}

numbers.remove(20)

print(numbers)


# ============================================================
# 18. remove() MISSING ELEMENT
# ============================================================

print("\n18. remove() MISSING")

numbers = {10, 20, 30}

# This would cause KeyError:
#
# numbers.remove(100)

print("remove() raises KeyError if element does not exist.")


# ============================================================
# 19. discard()
# ============================================================

print("\n19. discard()")

numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)

numbers.discard(100)

print(numbers)

# discard() does NOT raise an error
# if the element is absent.


# ============================================================
# 20. remove() VS discard()
# ============================================================

print("\n20. remove() VS discard()")

numbers = {1, 2, 3}

numbers.remove(2)

print("After remove:", numbers)

numbers.discard(100)

print("After discard:", numbers)

# remove(missing) -> KeyError
# discard(missing) -> no error


# ============================================================
# 21. pop()
# ============================================================

print("\n21. pop()")

numbers = {10, 20, 30, 40}

removed = numbers.pop()

print("Removed:", removed)
print("Remaining:", numbers)

# IMPORTANT:
# Set pop() removes an arbitrary element.
# It does NOT accept an index.


# ============================================================
# 22. clear()
# ============================================================

print("\n22. clear()")

numbers = {10, 20, 30}

numbers.clear()

print(numbers)


# ============================================================
# 23. del
# ============================================================

print("\n23. del")

numbers = {10, 20, 30}

del numbers

print("Set variable deleted.")


# ============================================================
# 24. UNION
# ============================================================

print("\n24. UNION")

a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)

print(result)


# ============================================================
# 25. UNION OPERATOR |
# ============================================================

print("\n25. UNION USING |")

a = {1, 2, 3}
b = {3, 4, 5}

result = a | b

print(result)


# ============================================================
# 26. INTERSECTION
# ============================================================

print("\n26. INTERSECTION")

a = {1, 2, 3}
b = {3, 4, 5}

result = a.intersection(b)

print(result)


# ============================================================
# 27. INTERSECTION OPERATOR &
# ============================================================

print("\n27. INTERSECTION USING &")

a = {1, 2, 3}
b = {3, 4, 5}

result = a & b

print(result)


# ============================================================
# 28. DIFFERENCE
# ============================================================

print("\n28. DIFFERENCE")

a = {1, 2, 3}
b = {3, 4, 5}

print("a - b:", a.difference(b))
print("b - a:", b.difference(a))


# ============================================================
# 29. DIFFERENCE OPERATOR
# ============================================================

print("\n29. DIFFERENCE USING -")

a = {1, 2, 3}
b = {3, 4, 5}

print(a - b)
print(b - a)


# ============================================================
# 30. SYMMETRIC DIFFERENCE
# ============================================================

print("\n30. SYMMETRIC DIFFERENCE")

a = {1, 2, 3}
b = {3, 4, 5}

result = a.symmetric_difference(b)

print(result)


# ============================================================
# 31. SYMMETRIC DIFFERENCE OPERATOR ^
# ============================================================

print("\n31. SYMMETRIC DIFFERENCE USING ^")

a = {1, 2, 3}
b = {3, 4, 5}

print(a ^ b)


# ============================================================
# 32. SET OPERATIONS VISUALIZATION
# ============================================================

print("\n32. SET OPERATIONS")

a = {1, 2, 3}
b = {3, 4, 5}

print("A:", a)
print("B:", b)

print("Union:", a | b)
print("Intersection:", a & b)
print("A - B:", a - b)
print("B - A:", b - a)
print("Symmetric Difference:", a ^ b)


# ============================================================
# 33. UPDATE UNION
# ============================================================

print("\n33. update() UNION")

a = {1, 2, 3}
b = {3, 4, 5}

a.update(b)

print(a)


# ============================================================
# 34. INTERSECTION UPDATE
# ============================================================

print("\n34. intersection_update()")

a = {1, 2, 3}
b = {2, 3, 4}

a.intersection_update(b)

print(a)


# ============================================================
# 35. DIFFERENCE UPDATE
# ============================================================

print("\n35. difference_update()")

a = {1, 2, 3}
b = {2, 3, 4}

a.difference_update(b)

print(a)


# ============================================================
# 36. SYMMETRIC DIFFERENCE UPDATE
# ============================================================

print("\n36. symmetric_difference_update()")

a = {1, 2, 3}
b = {2, 3, 4}

a.symmetric_difference_update(b)

print(a)


# ============================================================
# 37. SUBSET
# ============================================================

print("\n37. SUBSET")

a = {1, 2}
b = {1, 2, 3, 4}

print("a subset of b:", a.issubset(b))

print("Using <=:", a <= b)


# ============================================================
# 38. PROPER SUBSET
# ============================================================

print("\n38. PROPER SUBSET")

a = {1, 2}
b = {1, 2, 3}

print(a < b)


# ============================================================
# 39. SUPERSET
# ============================================================

print("\n39. SUPERSET")

a = {1, 2, 3, 4}
b = {1, 2}

print("a superset of b:", a.issuperset(b))

print("Using >=:", a >= b)


# ============================================================
# 40. PROPER SUPERSET
# ============================================================

print("\n40. PROPER SUPERSET")

a = {1, 2, 3}
b = {1, 2}

print(a > b)


# ============================================================
# 41. DISJOINT
# ============================================================

print("\n41. DISJOINT")

a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))


# ============================================================
# 42. NON-DISJOINT
# ============================================================

print("\n42. NON-DISJOINT")

a = {1, 2, 3}
b = {3, 4, 5}

print(a.isdisjoint(b))


# ============================================================
# 43. COPYING SET
# ============================================================

print("\n43. COPY")

a = {1, 2, 3}

b = a.copy()

b.add(4)

print("a:", a)
print("b:", b)


# ============================================================
# 44. ALIASING
# ============================================================

print("\n44. ALIASING")

a = {1, 2, 3}

b = a

b.add(4)

print("a:", a)
print("b:", b)

# a and b refer to the same set.


# ============================================================
# 45. == VS is
# ============================================================

print("\n45. == VS is")

a = {1, 2, 3}
b = {1, 2, 3}

print("a == b:", a == b)
print("a is b:", a is b)


# ============================================================
# 46. SET COMPREHENSION
# ============================================================

print("\n46. SET COMPREHENSION")

numbers = [1, 2, 3, 4, 5]

squares = {x * x for x in numbers}

print(squares)


# ============================================================
# 47. SET COMPREHENSION WITH CONDITION
# ============================================================

print("\n47. SET COMPREHENSION WITH CONDITION")

numbers = range(1, 11)

even = {x for x in numbers if x % 2 == 0}

print(even)


# ============================================================
# 48. SET COMPREHENSION WITH EXPRESSION
# ============================================================

print("\n48. SET COMPREHENSION")

numbers = range(1, 6)

result = {
    x * 10
    for x in numbers
}

print(result)


# ============================================================
# 49. REMOVE DUPLICATES FROM LIST
# ============================================================

print("\n49. REMOVE DUPLICATES FROM LIST")

numbers = [1, 2, 2, 3, 3, 4, 5, 5]

unique = set(numbers)

print("Original:", numbers)
print("Unique:", unique)


# ============================================================
# 50. SET BACK TO LIST
# ============================================================

print("\n50. SET -> LIST")

numbers = {1, 2, 3, 4}

result = list(numbers)

print(result)


# ============================================================
# 51. LIST -> SET -> LIST
# ============================================================

print("\n51. REMOVE DUPLICATES")

numbers = [1, 2, 2, 3, 3, 4]

unique = list(set(numbers))

print(unique)

# WARNING:
# Original ordering is not guaranteed.


# ============================================================
# 52. PRESERVE ORDER WHILE REMOVING DUPLICATES
# ============================================================

print("\n52. REMOVE DUPLICATES AND PRESERVE ORDER")

numbers = [1, 2, 2, 3, 3, 4, 1]

unique = list(dict.fromkeys(numbers))

print(unique)


# ============================================================
# 53. LOOP THROUGH SET
# ============================================================

print("\n53. LOOP")

numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)


# ============================================================
# 54. SET WITH STRINGS
# ============================================================

print("\n54. STRINGS")

languages = {"Python", "Java", "C++", "Java"}

print(languages)


# ============================================================
# 55. SET OF TUPLES
# ============================================================

print("\n55. SET OF TUPLES")

coordinates = {
    (1, 2),
    (3, 4),
    (5, 6)
}

print(coordinates)


# ============================================================
# 56. SET CANNOT CONTAIN LIST
# ============================================================

print("\n56. UNHASHABLE ELEMENT")

# This is NOT allowed:
#
# data = {[1, 2], [3, 4]}
#
# because lists are unhashable.

print("Lists cannot be set elements.")


# ============================================================
# 57. SET CAN CONTAIN TUPLE
# ============================================================

print("\n57. TUPLE AS SET ELEMENT")

data = {(1, 2), (3, 4)}

print(data)


# ============================================================
# 58. SET OF FROZENSET
# ============================================================

print("\n58. FROZENSET")

a = frozenset([1, 2, 3])

print(a)
print(type(a))


# ============================================================
# 59. FROZENSET IMMUTABILITY
# ============================================================

print("\n59. FROZENSET")

numbers = frozenset([1, 2, 3])

print(numbers)

# These would NOT work:
#
# numbers.add(4)
# numbers.remove(2)


# ============================================================
# 60. FROZENSET OPERATIONS
# ============================================================

print("\n60. FROZENSET OPERATIONS")

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric:", a ^ b)


# ============================================================
# 61. FROZENSET AS SET ELEMENT
# ============================================================

print("\n61. FROZENSET AS SET ELEMENT")

a = frozenset([1, 2])
b = frozenset([3, 4])

data = {a, b}

print(data)


# ============================================================
# 62. FROZENSET AS DICTIONARY KEY
# ============================================================

print("\n62. FROZENSET AS DICTIONARY KEY")

data = {
    frozenset([1, 2]): "Group A",
    frozenset([3, 4]): "Group B"
}

print(data[frozenset([1, 2])])


# ============================================================
# 63. SET LENGTH
# ============================================================

print("\n63. LENGTH")

numbers = {10, 20, 30}

print(len(numbers))


# ============================================================
# 64. ANY AND ALL
# ============================================================

print("\n64. any() AND all()")

numbers = {2, 4, 6, 8}

print("Any > 5:", any(x > 5 for x in numbers))
print("All even:", all(x % 2 == 0 for x in numbers))


# ============================================================
# 65. MIN, MAX, SUM
# ============================================================

print("\n65. min(), max(), sum()")

numbers = {10, 20, 30, 40}

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))


# ============================================================
# 66. sorted() WITH SET
# ============================================================

print("\n66. sorted()")

numbers = {50, 10, 40, 20, 30}

result = sorted(numbers)

print("Set:", numbers)
print("Sorted list:", result)


# ============================================================
# 67. SET WITH MULTIPLE TYPES
# ============================================================

print("\n67. MIXED TYPES")

data = {
    10,
    "Python",
    3.14,
    True
}

print(data)


# ============================================================
# 68. SET OF BOOLEAN AND INTEGER CONFUSION
# ============================================================

print("\n68. True AND 1")

data = {True, 1, False, 0}

print(data)

# True == 1
# False == 0
#
# Therefore they are considered equal
# for set uniqueness.


# ============================================================
# 69. SET RELATIONSHIPS
# ============================================================

print("\n69. SET RELATIONSHIPS")

students_python = {"Alice", "Bob", "Charlie"}
students_java = {"Bob", "Charlie", "David"}

print("Both courses:", students_python & students_java)

print("Only Python:", students_python - students_java)

print("Only Java:", students_java - students_python)

print("Everyone:", students_python | students_java)

print("Exactly one course:",
      students_python ^ students_java)


# ============================================================
# 70. PRACTICAL EXAMPLE
# ============================================================

print("\n70. PRACTICAL EXAMPLE")

registered_students = {
    "Alice",
    "Bob",
    "Charlie",
    "David"
}

present_students = {
    "Bob",
    "Charlie",
    "David"
}

print("Present:", present_students)
print("Absent:", registered_students - present_students)
print("Present and registered:",
      registered_students & present_students)


# ============================================================
# 71. SUBSET PRACTICAL EXAMPLE
# ============================================================

print("\n71. SUBSET EXAMPLE")

required = {"Python", "SQL"}

skills = {"Python", "SQL", "Java", "Git"}

print("Has all required skills:",
      required.issubset(skills))


# ============================================================
# 72. DISJOINT PRACTICAL EXAMPLE
# ============================================================

print("\n72. DISJOINT EXAMPLE")

morning = {"Alice", "Bob"}
evening = {"Charlie", "David"}

print("No common student:",
      morning.isdisjoint(evening))


# ============================================================
# 73. COPY USING set()
# ============================================================

print("\n73. COPY USING set()")

a = {1, 2, 3}

b = set(a)

b.add(4)

print("a:", a)
print("b:", b)


# ============================================================
# 74. CLEAR SET
# ============================================================

print("\n74. CLEAR")

a = {1, 2, 3}

a.clear()

print(a)


# ============================================================
# 75. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("                  END OF SET GUIDE")
print("=" * 70)