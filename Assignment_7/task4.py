import random

print("\nEnter a list of data entries separated by a comma ',' .... ")
dataEntries = str(input("\nEnter data here: "))

print("\nSplitting data entries....")
tupleEntries = dataEntries.split(',')
print(tupleEntries)

#Making assorted tupleEntries
mutableTuple1 = tupleEntries
mutableTuple1 = sorted(mutableTuple1)
print("\nSorted Tuple Copy: " + str(mutableTuple1))

#Making randomly assorted tupleEntries
mutableTuple2 = tupleEntries
mutableTuple2 = random.shuffle(mutableTuple2)
print("\nRandomly Sorted Tuple Copy: " + str(mutableTuple2))

#Conversion to tuple
print("\nTuple Conversion: ")
tupleEntries = tuple(tupleEntries)
print(tupleEntries)


#String concat
tupleConcat = str(mutableTuple1) + str(mutableTuple2)
print("\nConcatanated String: " + str(tupleConcat))