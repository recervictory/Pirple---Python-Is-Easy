"""
Homework Assignment #4: Lists


Details:
 
Create a global variable called myUniqueList. It should be an empty list to start.

Next, create a function that allows you to add things to that list. Anything that's passed to this function should get added to myUniqueList, unless its value already exists in myUniqueList. If the value doesn't exist already, it should be added and the function should return True. If the value does exist, it should not be added, and the function should return False;

Finally, add some code below your function that tests it out. It should add a few different elements, showcasing the different scenarios, and then finally it should print the value of myUniqueList to show that it worked.


Extra Credit:

Add another function that pushes all the rejected inputs into a separate global array called myLeftovers. If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness), it should get added to myLeftovers instead.

"""
myUniqueList = []
myLeftovers = []


def addmyUniqueList(data):
  if data not in myUniqueList:
    myUniqueList.append(data)
    return True
  else:
    myLeftovers.append(data)
    return False

#Test 1
print(myUniqueList,myLeftovers)

#Test 2
addmyUniqueList(1)
print(myUniqueList,myLeftovers)

#Test 3
addmyUniqueList(2)
print(myUniqueList,myLeftovers)

#Test 4
addmyUniqueList(2)
print(myUniqueList,myLeftovers)

#Test 
addmyUniqueList(3)
print(myUniqueList,myLeftovers)