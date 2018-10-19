# Example 1 :
# A Python program to to return multiple values from a method using class
class Test:
    def __init__(self):
        self.str = "geeksforgeeks"
        self.x = 20


# This function returns an object of Test
def fun():
    return Test()


# Driver code to test above method
t = fun()
print(t.str)
print(t.x)

print()


# Example 2 :
# A Python program to to return multiple values from a method using tuple
# This function returns a tuple
def fun():
    str = "geeksforgeeks"
    x = 20
    return str, x  # Return tuple, we could also write (str, x)


str, x = fun()  # Assign returned tuple
print(str)
print(x)

print()


# Example 3 :
# A Python program to to return multiple values from a method using list
# This function returns a list
def fun():
    str = "geeksforgeeks"
    x = 20
    return [str, x]


list = fun()
print(list)

print()


# Example 4 :
# A Python program to to return multiple values from a method using dictionary
# This function returns a dictionary
def fun():
    d = dict()
    d['str'] = "GeeksforGeeks"
    d['x'] = 20
    return d


d = fun()
print(d)
