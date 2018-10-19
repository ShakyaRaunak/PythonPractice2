class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('being deleted')

    def study(self):
        print('Student Studying')


s1 = Student('Raunak', 10)


class scc_student(Student):
    def study(self):
        super(scc_student, self).study()
        print('scc_student studying')


s2 = scc_student('Rahul', 14)
s2.study()
print(s2.name)
print(s2.age)


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def print(self):
        print('Vector {0}, {1}'.format(self.a, self.b))

    def __str__(self):
        print('Vector (%d, %d)' % (self.a, self.b))


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
v3.print()
# print(v3)

fs = open('iris.csv', 'r')
lines = fs.read()
print(lines)
fs = open('iris.csv', 'w')
fs.write('Hello World')
fs.close()
