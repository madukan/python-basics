print("Variables")

#String/Int
myString = "'Foo'"
mySecondString = '"Bar"'

myInteger = 0

#Lists
myList = [1, 2, 3, 4, 5]
print(myList)
myList.extend([6, 7, 8])
print(myList)
newList = myList[0:3]
print(newList)

#Dictionary
myDict = {"Something": "SomethingElse", "OneThing": "AnotherThing"}
print(myDict)

#Sets
mySet = set(["One", "Two", "Three", "Four", "One", "Three"])
print(mySet)

#Tuples
myTuple = ("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight")
print(myTuple)

#Multiple assignment
foo, bar, baz = "Yes", "No", False