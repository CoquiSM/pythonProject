import random
numList = []
average = 0
counter = 0
##First 5 numbers randomized between -50 & 50
for x in range(6):
    numList.insert(x,random.randint(-50, 50))

##last 5 numbers randomized between 10 & 100
for y in range(7, 11):
    numList.insert(y,random.randint(10, 100))

print("\nNumber list:")
print("\n" + str(numList))

while counter != 9:
    average = average + counter
    counter += 1

average = average / 1

print("\nThe Average is: " + str(average))