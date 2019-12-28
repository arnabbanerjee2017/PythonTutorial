
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

# ---------------------------------------------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------------------------------------")
# Types of variables
# 2 types of variables - Instance Variables and Class or Static Variables
class Car:
    # Below variable - wheels is a class or static variable and belongs to the Class Namespace.
    # As this is a class variable, this is shared across the objects.
    wheels = 4      # A Class or Static Variable

    def __init__(self):
        # Below variables are instance variables. Means they are bound to a particular instance.
        # Every time you create an object, that object will be created in a separate space in the heap memory, though
        # they have same values. So below, car1 and car2 will be having same value and at the time of creation,
        # they will be identical objects, still they will be created separately having different id or address.
        # But in the object, as they are identical, they are having same values. So both of the objects will contain
        # the below variables having same values. In this case, as Python is memory optimized, the variables will point
        # to same memory locations. Like in car1, the brand is 'TATA', and in car2, the brand is also 'TATA'. So,
        # actually in memory, a single 'TATA' object will be created and both brand of car1 ad car2 will point to
        # that same object.
        self.brand = "TATA"     # An Instance variable
        self.model = "TIAGO"    # An Instance variable
        self.engine = "Twin Valve 1.2L Turbo Petrol"    # An Instance variable
        self.mil = "12"         # An Instance variable

    # This is a print method just to demonstrate the the instance and class variables.
    def print(self):
        print("Brand:", self.brand, "\tModel:", self.model, "\tEngine:", self.engine, "\tMileage:", self.mil)
        print("Wheels:", Car.wheels, "ID of Wheels:", id(Car.wheels))

# Here we are creating 2 Car objects - car1 and car2
car1 = Car()
car2 = Car()

# Here we are calling the print() method just to show the values after the object is created.
car1.print()
car2.print()

# Here we are making some changes to the car1 objects.
car1.model = "TIGOR"
car1.mil = 8

print("<<<<<<After Change>>>>>>")

# Here we are again calling the print() method of the objects to check whether the above changes made are
# reflected or not
car1.print()
car2.print()

print("<<<<<<After Change>>>>>>")

# Here we are trying to change the class variable through an object.
# This will not change the static or class variable, rather this creates a new wheels instance
# variable belonging to car1 object.
car1.wheels = 6

# Here you can see the print statements below. Make a note of it.
# First when the print() method of car1 is called, you can see the values as it was earlier.
# Also note that address of the wheels variable - the class variable. This is shared by all the objects of that class.
# Now, we have just tried to modify the class variable through the car1 object. See above.
# But in this case, this attempt just created another instance variable - wheels in the car1 objects and this didn't
# make any changes to the actual class variable. See the id or the address of the class variable and the car1.wheels
# variable. In case of car1, the id of wheels and car1.wheels are different. But in case of car2, both are same.
car1.print()
print("Car1 Wheels:", car1.wheels, "ID of Car1.Wheels:", id(car1.wheels))
car2.print()
print("Car2 Wheels:", car2.wheels, "ID of Car2.Wheels:", id(car2.wheels))

print("<<<<<<After Change>>>>>>")

# Now we are trying to change the class variable through class name.
Car.wheels = 6

# Here below, check that the the wheels is now a static/class variable and the change is reflected to all te objects.
# Compare the id or address of the wheels objects across the objects - car1 and car2, and Car class.
car1.print()
print("Car1 Wheels:", car1.wheels, "ID of Car1.Wheels:", id(car1.wheels))
car2.print()
print("Car2 Wheels:", car2.wheels, "ID of Car2.Wheels:", id(car2.wheels))

# ---------------------------------------------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------------------------------------")
# Types of Methods
# 3 types of methods - Instance methods, Class methods, and Static methods.




