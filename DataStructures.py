from array import *


class DataStructures:
    """Working on Data Structures"""

    def printArray(self, arrayToPrint):
        print("Array Contents:")
        for y in arrayToPrint:
            print(y)

    def printElement(self, elementName, intToPrint):
        print("Element %s: %i" % (elementName, intToPrint))


myPrinter = DataStructures()

array1 = array("i", [50, 40, 300, 29, 360])

print(array1.index(300))

myPrinter.printArray(array1)
myPrinter.printElement("Zero", array1[0])
