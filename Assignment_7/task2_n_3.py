dataList = []
counter = 0
sentinel = "I AM BORED"
dataInput =""

while dataInput != sentinel:
    dataInput = input("Enter data")
    dataList.insert(counter, dataInput)
    counter += 1

dataList = sorted(dataList)

print("\nSentinel detected, sorting list...")

for x in range(0, counter):
    print(dataList[x])

print("\n" + str(dataList))
print("\nAmount of iterations: " + str(counter))
