import array as arr
import numpy
import FunctionDemo as func

myArray = arr.array('i', [1, 2, 3, 4, 5])
print(myArray)
print(type(myArray))
print(type(myArray[1]))

myNumpyArray = numpy.array([1, 2, 3, 4, 5])
print(myNumpyArray)
print(type(myNumpyArray))
print(type(myNumpyArray[1]))

myNumpyArray = numpy.array([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
print(myNumpyArray)
print(type(myNumpyArray))
print(type(myNumpyArray[1][1]))

func.greet()