import ModuleDemo.AnotherModule as am

print("In Main Module:", __name__)

# Calling method() of AnotherModule explicitly
am.method()

def fun1():
    print("from fun1")

def fun2():
    print("from fun2")

