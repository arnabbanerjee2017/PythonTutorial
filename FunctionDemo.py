# Basics of Functions

def func1():
    print("Hello, World!")
    print("Hi, how are you? I am doing fine!")

func1()

def func2(x, y):
    return x + y, x - y, x * y, x / y

print(func2(5, 4), type(func2(5, 4)))

print(func2(5, 4)[0], type(func2(5, 4)[0]))
print(func2(5, 4)[1], type(func2(5, 4)[1]))
print(func2(5, 4)[2], type(func2(5, 4)[2]))
print(func2(5, 4)[3], type(func2(5, 4)[3]))

print("\n\n====================================================================================================\n\n")

def func_update_test(x):
    print("Old x:", x)
    print("ID of old x:", id(x))
    x = 255
    print("New x:", x)
    print("ID of new x:", id(x))

a = 10
print("Old a:", a)
print("ID of old a:", id(a))
func_update_test(a)
print("New a:", a)
print("ID of new a:", id(a))

# Types of Parameters -  fixed position, default, non-fixed position.
print("\n\nTypes of Parameters -  fixed position, default, non-fixed position.")
def person(name, age = 18):
    print("Name:", name)
    print("Age after deducting 5 years:", age - 5)

person("Arnab Banerjee", 30)            # fixed position
person("Arnab Banerjee")                # default
person(age=35, name="Arnab Banerjee")   # non-fixed position

# Varargs
print("\n\nVariable Arguments - Varargs")
def var_sum(*data):
    sum = 0
    for i in data:
        sum += i
    return sum

print("Sum:", var_sum(1, 2, 3, 4, 5))
print("Sum:", var_sum(10, 20, 90, 80, 70))
print("Sum:", var_sum()) # var_sum() will return 0 in case no argument is passed as sum is initialized to 0

# Keyworded variable length argument - Key-Value pair as Variable name and value pair.
print("\n\nKeyworded variable length argument - Key-Value pair as Variable name and value pair.")
def personKeywordVarargs(name, **data):
    print("Name:", name, "Type of name:", type(name))
    print("Data:", data, "Type of data:", type(data)) # dictionary
    return name, data

name, data = personKeywordVarargs("Arnab Banerjee", age = 30, city = 'Kolkata', prof = "Software Developer/Java Developer")

# Passing dictionary.
print("\n\nPassing dictionary.")
def personWithDictionary(name, data):
    print("Name:", name, "Type of name:", type(name))
    print("Data:", data, "Type of data:", type(data))  # dictionary
    print("===== Iterating Dictionary =====")
    for key, value in data.items():
        print("Key:", key, "\tType of Key:", type(key), "\tValue:", value, "\tType of Value:", type(value))
    print("===== Iterating Dictionary =====")

personWithDictionary(name, data)

# Global Variable
print("\n\nGlobal Variable")
num = 10
def functionToChangeGlobalNum():
    global num
    num = 15
    print("num:", num)

functionToChangeGlobalNum()
print("Global num:", num)

# Getting Global Variables
print("\n\nGetting Global Variables")
num = 10
print("num:", num, "ID of num:", id(num))
def functionToGetGlobalVariables():
    num = 8
    globalVars = globals()
    print("GlobalVars:", globalVars, "Type of GlobalVars:", type(globalVars))
    #for key, value in globalVars:
    #    print("Key:", key, "Value:", value)
    globalNum = globalVars.get("num")
    print("globalNum:", globalNum, "ID of globalNum:", id(globalNum))
    globalNum = 15
    print("globalNum:", globalNum, "ID of globalNum:", id(globalNum))
    globals()['num'] = 20
    print("globalNum:", globalNum, "ID of globalNum:", id(globalNum))
    globalNum = globalVars.get("num")
    print("globalNum:", globalNum, "ID of globalNum:", id(globalNum))

functionToGetGlobalVariables()
print("num:", num, "ID of num:", id(num))

# Passing a list to a function
print("\n\nPassing a list to a function")
def getTotalCountOfEvenAndOddNumbers(list):
    evenNumbers = 0
    oddNumbers = 0
    for value in list:
        if value % 2 == 0:
            evenNumbers += 1
        else:
            oddNumbers += 1
    return evenNumbers, oddNumbers

evens, odds = getTotalCountOfEvenAndOddNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print("Even Numbers:", evens, "Odd Numbers:", odds)

# Anonymous or Lambda Function
print("\n\nAnonymous or Lambda Function")
sqrt_of_a = lambda a: a * a
add_of_2_nos = lambda a, b: a + b
print("Square Root of a Number: 5 ->", sqrt_of_a(5))
print("Addition of 2 Numbers: 5, 6 ->", add_of_2_nos(5, 6))

# __name__ variable
print("\n\n__name__:", __name__)



