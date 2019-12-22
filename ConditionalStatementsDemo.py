
if False:
    print("Inside if")
print("Outside of if.")

a = 10
b = 10;
if a > b:
    print("a > b")
elif a == b:
    print("a == b")
else:
    print("b > a")

arnab = ['arnab', 'banerjee', 'kolkata', 'wb', 700074, 5.1]
for i in arnab:
    print(i, type(i))

for i in range(10):
    if i % 2 == 0:
        continue
    print(i ** i)

nums = [16, 18, 21, 26, 30]
for num in nums:
    if num % 5 == 0:
        print("found!")
        break
else:
    print("not found!")

while True:
    x = int(input("Enter a number: "))
    if x == 555:
        print("Hey, thanks for using our system! Wish to serve you again! Good Bye!")
        break
    if x % 2 == 0 and x != 0:
        print(x, "is an even number.")
        if x > 999:
            print("Now that is huge!")
    elif x == 0:
        print("Wow! You entered a zero.")
    else:
        print(x, "is an odd number.")
        if x > 999:
            print("Now that is huge!")


