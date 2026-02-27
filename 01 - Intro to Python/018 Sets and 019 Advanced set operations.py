# 018 Sets
# A set is an unordered collection of unique elements. It is defined using curly braces {} or the set() function.
# Sets are mutable, meaning you can add or remove elements from a set after it has been
# created. However, the elements themselves must be immutable (e.g., numbers, strings, tuples).

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
# Adding elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
# Removing elements from a set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}
# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# Union
union_set = set_a | set_b
print(union_set)  # Output: {1, 2, 3, 4, 5}
# Intersection
intersection_set = set_a & set_b
print(intersection_set)  # Output: {3}
# Difference
difference_set = set_a - set_b
print(difference_set)  # Output: {1, 2}
# Symmetric Difference
symmetric_difference_set = set_a ^ set_b
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
# Checking for membership
print(2 in set_a)  # Output: True
print(4 in set_a)  # Output: False
# Set comprehension
squared_set = {x**2 for x in range(1, 6)}
print(squared_set)  # Output: {1, 4, 9, 16, 25}
# Frozen sets
# A frozen set is an immutable version of a set. It is defined using the frozenset() function.
frozen_set = frozenset([1, 2, 3, 4, 5])
print(frozen_set)  # Output: frozenset({1, 2, 3, 4, 5})
# frozen_set.add(6)  # This line will raise an AttributeError because frozen sets are immutable

# give me advanced methods for the set in python like issubset, issuperset, isdisjoint, etc.
# Advanced set methods
set_c = {1, 2}
set_d = {1, 2, 3, 4, 5}
# issubset
print(set_c.issubset(set_d))  # Output: True
# issuperset
print(set_d.issuperset(set_c))  # Output: True
# isdisjoint
set_e = {6, 7, 8}
print(set_c.isdisjoint(set_e))  # Output: True
print(set_c.isdisjoint(set_d))  # Output: False

# difference
set_f = {1, 2, 3, 4, 5}
difference_set = set_f.difference({3, 4})
print(difference_set)  # Output: {1, 2, 5}

# difference_update
set_f = {1, 2, 3, 4, 5}
set_f.difference_update({3, 4})
print(set_f)  # Output: {1, 2, 5}

# symmentric_difference
set_g = {1, 2, 3}
set_h = {3, 4, 5}
sym_diff_set = set_g.symmetric_difference(set_h)
print(sym_diff_set)  # Output: {1, 2, 4, 5}

# symmetric_difference_update
set_g = {1, 2, 3}
set_h = {3, 4, 5}
set_g.symmetric_difference_update(set_h)
print(set_g)  # Output: {1, 2, 4, 5}

# union, intersection and update
set_i = {1, 2, 3}
set_j = {3, 4, 5}
# union
union_set = set_i.union(set_j)
print(union_set)  # Output: {1, 2, 3, 4, 5}
# intersection
intersection_set = set_i.intersection(set_j)
print(intersection_set)  # Output: {3}
# update
set_i.update(set_j)
print(set_i)  # Output: {1, 2, 3, 4, 5}
