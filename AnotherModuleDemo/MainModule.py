import AnotherModuleDemo.Calculator as cal

x = 987
y = 313

print("Additon:", cal.add(x, y))
print("Subtraction:", cal.sub(x, y))
print("Multiplication:", cal.mul(x, y))
print("Division:", cal.div(x, y))
print("Remainder:", cal.rem(x, y))

print(__name__)
print(cal.__name__)

