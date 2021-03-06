# https://www.geeksforgeeks.org/chainmap-in-python/

# Python code to demonstrate ChainMap and keys(), values() and maps

# importing collections for ChainMap operations
import collections

# Example 1 :
# initializing dictionaries
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}

# initializing ChainMap
chain = collections.ChainMap(dic1, dic2)

# printing chainMap using maps
print("All the ChainMap contents are : ")
print(chain.maps)

# printing keys using keys()
print("All keys of ChainMap are : ")
print(list(chain.keys()))

# printing keys using keys()
print("All values of ChainMap are : ")
print(list(chain.values()))

print()

# Example 2 :
dic3 = {'f': 5}

# using new_child() to add new dictionary
chain1 = chain.new_child(dic3)

# printing chainMap using map
print("Displaying new ChainMap : ")
print(chain1.maps)

# displaying value associated with b before reversing
print("Value associated with b before reversing is : ", end="")
print(chain1['b'])

# reversing the ChainMap
chain1.maps = reversed(chain1.maps)

# displaying value associated with b after reversing
print("Value associated with b after reversing is : ", end="")
print(chain1['b'])
