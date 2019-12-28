
# Define a class - Person
class Person:
    # Define a method inside the class. This method belongs to this class and not the global module.
    # So to use this method, you need to create an object of this class.
    def getPerson(self):
        print("Arnab Banerjee" + "\nAge:29")

# Create an object of class Person
person = Person()

# Check the type of the object created above
print("Object type created above:", type(person))

# Here is the calling of getPerson() method by the class name.
# Remember when you call the method by class name, just pass the actual object created by that class to that method.
# Because there might be several objects of that class created and to access a particular object's method, you need
# to pass the object to it's method as a parameter. That is why the the 'self' declaration in that getPerson() method
# in the class Person - def getPerson(self).
Person.getPerson(person)

# This is another way of calling a method belonging to an object.
# And generally we will use this way only.
person.getPerson()

#---------------------------------------------------------------------------------------------------------------------
print("=================================================================================")

# Let's try a real world object creation and handler.
# Here we are creating a List of three Person objects.
# We will iterate through this list and would call the methods within it.
persons = [Person(), Person(), Person()]

# First let's check the type of the persons object
print("Type of persons object:", type(persons))

# Print the exact object to check what actually gets printed.
print("persons:", persons)

# Let's iterate through the list and print individual objects.
for p in persons:
    print("<<==>>")
    p.getPerson()
    print("<<==>>")

# ---------------------------------------------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------------------------------------")
# Demonstrating __init__
# __init__ is like a constructor.
class PersonalDetails:
    # Here in __init__ we are passing name and city as parameters.
    # Also to note that the variables declared in this class - name and city are declared in this __init__ method.
    # And we are assigning the values from the parameters - name anc city to the name and city variable of the current
    # object - self -> self.name and self.city
    def __init__(self, name, city):
        self.name = name
        self.city = city

    # This is getter method returning the name of the current object.
    # To return the value of variable of an object, just use the self as mentioned below -
    # self.name or self.city
    def getName(self):
        return self.name

    # Same as above - self.name
    def getCity(self):
        return self.city

    # Here we are just printing name and city of the current object - self.name and self.city
    def print_details(self):
        print("Name:", self.name, "City:", self.city)

# Here we are creating 2 objects of the class PersonalDetails.
# 1. person1 with the details mentioned in the class arguments below.
# 2. person2 with the details mentioned in the class arguments below.
person1 = PersonalDetails('Arnab Banerjee', 'Kolkata')
person2 = PersonalDetails(city='Calcutta', name='Balaram Ghosh')

# Now we are calling the print methods of the objects create above.
person1.print_details()
person2.print_details()

# Here we are calling the actual getters or methods under the objects created above.
print("Testing the getters!")
print("Person1 Name:", person1.getName(), "\tPerson1 City:", person1.getCity())
print("Person2 Name:", person2.getName(), "\tPerson2 City:", person2.getCity())

# ---------------------------------------------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------------------------------------")
# Constructor, self, and Comparing Objects
class Computer:
    def __init__(self):
        self.cpu = "Ryzen 5"
        self.ram = 16

    # This is just another method to compare the objects.
    # Here you can define your custom compare logic.
    # Here we are comparing the objects by ram.
    def compare(self, computer):
        if self.ram == computer.ram:
            return True
        else:
            return False

# Again we are creating 2 objects.
# Both will be separate objects and be created on the heap, but having same values.
comp1 = Computer()
comp2 = Computer()

# Just to confirm that the objects are different, we are printing the id/address or the objects.
print("Address of comp1:", id(comp1))
print("Address of comp2:", id(comp2))

# Here we are comparing the 2 objects. But this will only compare the id or the address of the objects, rather
# comparing the actual objects by their values.
print(comp1 == comp2)

# Same thing as above.
if comp1 == comp2:
    print("They are same!")
else:
    print("They are not same!")

# Here we are calling the compare method of one object and passing the second object as parameter.
print(comp1.compare(comp2))
