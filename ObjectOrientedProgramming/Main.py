
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
person.getPerson()

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
