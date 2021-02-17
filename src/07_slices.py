"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
result = a[1]
print(result)

# Output the second-to-last element: 9
result = a [4]
print(result)

# Output the last three elements in the array: [7, 9, 6]
result = slice(3, 6, 1)
print(a[result])
print(a[3:])

# Output the two middle elements in the array: [1, 7]
result = slice(2, 4, 1)
print(a[result])
print(a[2:4])

# Output every element except the first one: [4, 1, 7, 9, 6]
result = slice(1, 6)
print(a[result])
print(a[1:6])

# Output every element except the last one: [2, 4, 1, 7, 9]
result = slice(5)
print(a[result])
print(a[0:5])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
result = slice(7, 12)
print(s[result])
