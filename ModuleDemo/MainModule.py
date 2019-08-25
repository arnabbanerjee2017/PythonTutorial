import ModuleDemo.AnotherModule as am

print("In Main Module:", __name__)

# Calling method() of AnotherModule explicitly
am.method()

def fun1():
    print("from fun1")
    am.add()

def fun2():
    print("from fun2")
    am.sub()

def main():
    fun1()
    fun2()

main()

count = 0
def recursive_fun():
    global count
    count += 1
    print("Hello World! Count:", count)
#    recursive_fun() # Recursive call is currently commented out as it will result in Stack Overflow.

recursive_fun()