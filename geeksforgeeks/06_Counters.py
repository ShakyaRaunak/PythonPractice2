# A Python program to show different ways to create Counter
from collections import Counter

# Example 1 :
# With sequence of items
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))

# with dictionary
print(Counter({'A': 3, 'B': 5, 'C': 2}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))

print()

# Example 2 :
coun = Counter()

coun.update([1, 2, 3, 1, 2, 1, 1, 2])
print(coun)

coun.update([1, 2, 4])
print(coun)

print()

# Example 3 :
# Python program to demonstrate that counts in Counter can be 0 and negative
c1 = Counter(A=4, B=3, C=10)
c2 = Counter(A=10, B=3, C=4)

c1.subtract(c2)
print(c1)

print()

# Example 4 :
# An example program where different list items are counted using counter
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']

# Count distinct elements and print Counter aboject
print(Counter(z))

print()

# Example 5 :
# Python program to demonstrate accessing of Counter elements
col_count = Counter(z)
print(col_count)

col = ['blue', 'red', 'yellow', 'green']

# Here green is not in col_count so count of green will be zero
for color in col:
    print(color, col_count[color])

print()

# Example 6 :
# Python example to demonstrate elements() on Counter (gives back list)
coun = Counter(a=1, b=2, c=3)
print(coun)
print(list(coun.elements()))

print()

# Example 7 :
# Python example to demonstrate most_elements() on Counter
coun = Counter(a=1, b=2, c=3, d=120, e=1, f=219)

# This prints 3 most frequent characters
for letter, count in coun.most_common(3):
    print('%s: %d' % (letter, count))
