# https://www.geeksforgeeks.org/array-in-python-set-2-important-functions/

# Python code to demonstrate the working of typecode, itemsize, buffer_info()
import array

# initializing array with signed integers
arr1 = array.array('i', [1, 2, 3, 1, 2, 5])

"""
typecode :- This function returns the data type by which array is initialised.
itemsize :- This function returns size in bytes of a single array element.
buffer_info() :- Returns a tuple representing the address in which array is stored and number of elements in it.
"""

# using typecode to print datatype of array
print("The datatype of array is : ", end="")
print(arr1.typecode)

# using itemsize to print itemsize of array
print("The itemsize of array is : ", end="")
print(arr1.itemsize)

# using buffer_info() to print buffer info. of array
print("The buffer info. of array is : ", end="")
print(arr1.buffer_info())
print()

"""
count() :- This function counts the number of occurrences of argument mentioned in array.
extend(arr) :- This function appends a whole array mentioned in its arguments to the specified 
"""

# initializing array 2 with signed integers
arr2 = array.array('i', [1, 2, 3])

# using count() to count occurrences of 1 in array
print("The occurrences of 1 in array is : ", end="")
print(arr1.count(1))

# using extend() to add array 2 elements to array 1
arr1.extend(arr2)

print("The modified array is : ", end="")
for i in range(0, 9):
    print(arr1[i], end=" ")

print('\n')

"""
fromlist(list) :- This function is used to append a list mentioned in its argument to end of array.
tolist() :- This function is used to transform an array into a list.
"""

arr = array.array('i', [1, 2, 3, 1, 2, 5])

# initializing list
li = [1, 2, 3]

# using fromlist() to append list at end of array
arr.fromlist(li)

# printing the modified array
print("The modified array is : ", end="")
for i in range(0, 9):
    print(arr[i], end=" ")

# using tolist() to convert array into list
li2 = arr.tolist()

print("\r")

# printing the new list
print("The new list created is : ", end="")
for i in range(0, len(li2)):
    print(li2[i], end=" ")
