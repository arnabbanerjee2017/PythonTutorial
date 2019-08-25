def method():
    print("Hello from just another module:", __name__)
    name = input("Enter your name:")
    print(name)

if __name__ == '__main__':
    method()

def add():
    print("Inside add() method.")

def sub():
    print("Inside sub() method.")

def main():
    add()
    sub()

main()

