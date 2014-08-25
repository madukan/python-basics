from variables import myTuple, myList, myDict, mySet

print("\nControl Flow")

#If
if len(myTuple) == 8:
    print("Eight elements in the tuple")
else:
    print("More or less than eight elements")

#While
i = 0
while i < len(myList):
    print("While loop iteration " + str(i))
    i += 1

#While with Else
i = 0
while i < len(myList):
    print("While loop iteration " + str(i))
    if myList[i] == 100:
        break
    i += 1
else:
    print("While Else reached")

#For loop
for element in myTuple:
    print(element)

#For loop with multiple variables
for index, element in enumerate(myTuple):
    print(str(index) + ": " + element)

#For loop over dict
for key, value in myDict.iteritems():
    print(key + ": " + value)

#List comprehensions
cubes = [number**3 for number in myList]
print(cubes)

cubes_above_three = [number**3 for number in myList if number > 3]
print(cubes_above_three)


#Generator expressions
#natural_numbers_list = (number**3 for number in range(1000000000))