squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[2])
print(squares[2:])
squares[2] = 90
print(squares)

a = ['a', 'b', 'c']
b = [1, 2, 3]
x = [a, b]
print(x)

i = 256 * 256
print("The value of i is", i)

a = 0
b = 1
while a < 1000:
    print(a, end=',')
    z = a + b
    a = b
    b = z

print("\n")

words = ['Apple', 'Banana', 'Cat', "Dog"]
for w in words:
    print(w, len(w))

for i in range(len(words)):
    print(i, words[i])


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=',')
        z = a + b
        a = b
        b = z
    print()


#fib(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

x = int(input())
y = int(input())
z = x + y
print(z)