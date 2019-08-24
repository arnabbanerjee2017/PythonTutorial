# Basics of function
def greet():
    print("Hello World!")
    print("Good Morning!")

def ops(a, b):
    return a + b, a - b, a * b, a / b

greet()
greet()

result = ops(4, 5)
print(result)
print(type(result))

add, sub, mul, div = ops(8, 2)
print(add, type(add))
print(sub, type(sub))
print(mul, type(mul))
print(div, type(div))

print("============================================================================================================")

# Functions arguments
def update(x):
    print("Old x:", x)
    print("ID of old x:", id(x))
    x = 255
    print("New x:", x)
    print("ID of new x:", id(x))

a = 10
print("Old a:", a)
print("ID of old a:", id(a))
update(a)
print("New a:", a)
print("ID of new a:", id(a))

# Types of arguments - fixed position, default, non-fixed position.
def person(name, age=18):
    print(name)
    print(age - 5)

person('arnab', 30)             # fixed position
person('arnab')                 # default
person(age=40, name='arnab')    # non-fixed position, parameter names are specified explicitly

# Varargs
def sum(*b):
    a = 0
    for i in b:
        a += i
    return a

sum1 = sum(1, 2, 3, 4, 5)
sum2 = sum(10, 20)
sum3 = sum(0, 10, 20, 30, 40)
print(sum1, sum2, sum3)

# Keyworded Variable Length Arguments
def personVarArgs(name, **data):
    print(name, type(name))
    print(data, type(data))

# Passing dictionary
def personDict(name, data):
    print(name, type(name))
    print(data, type(data))

personVarArgs('arnab', age=29, city='kolkata', phone=9874563210)
data = {'age': 29, 'city': 'kolkata', 'phone': 9874563210}
personDict('arnab', data)

# Iterating dictionary
for i, j in data.items():
    print("Key:", i, "Value:", j, type(i))

# Global Variable
print("===================================================================================================")
aNum = 10
def funcToChangeANum():
    global aNum
    aNum = 15
    print("aNum:", aNum)
funcToChangeANum()
print("Global aNum:", aNum)

# Getting Global variables.
print("===================================================================================================")
aNum = 10
print(id(aNum))
def funcToChangeANum():
    aNum = 8
    globalVars = globals()['aNum']
    print("id of globalVars:", id(globalVars))
    globalVars = 15 # It will not change the value of global aNum, instead it will simply point to new location where 15 resides.
    print("globalVars:", globalVars)
    print("id of globalVars:", id(globalVars))
    globals()['aNum'] = 20
    globalVars = globals()['aNum']
    print("id of globalVars:", id(globalVars))
    print("globalVars:", globalVars)
    print("Local aNum:", aNum)
funcToChangeANum()
print("Global aNum:", aNum)
print(id(aNum))

# Passing List to a function
print("===================================================================================================")
def getEvenAndOdd(list):
    countOfEven = 0
    countOfOdd = 0
    for i in list:
        if(i % 2 == 0):
            countOfEven += 1
        else:
            countOfOdd += 1
    return countOfEven, countOfOdd
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = getEvenAndOdd(list)
print("No. of even no.:", even)
print("No. of odd no.:", odd)

# Anonymous / Lambda Function
print("===================================================================================================")
f_sqr = lambda a: a * a
print(f_sqr(5))
f_add = lambda a, b: a + b
print(f_add(5,6))

# Filter, Map, and Reduce
print("===================================================================================================")
from functools import reduce
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = []
for i in filter(lambda n: n % 2 == 0, nums):
    evens.append(i)
print(evens)
plusTwoEvens = []
for i in map(lambda n: n + 2, evens):
    plusTwoEvens.append(i)
print(plusTwoEvens)
sum = reduce(lambda x, y: x + y, plusTwoEvens)
print(sum)

print("===================================================================================================")

# Next start from Decorators
def div(a, b):
    print(a/b)

def smart_div(a, b):
    if a > b:
        div(a, b)
    else:
        div(b, a)

smart_div(2, 4)


