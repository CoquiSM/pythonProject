tuition = 15000.00
#Interest will initialize at 1.04 as a default
interest = 1.04
years = 10
counter = 0
rateOfIncrease = 0.00
input("\nInterest is at 1.04 (Default)")
print("\nStarting tuition cost is: $" + str(15000))
rateOfIncrease = float(input("\nPlease enter rate of interest increase"))

while (counter != 10):
    counter += 1
    interest = float(interest + rateOfIncrease)
    tuition = tuition * interest
    tuition_Format = "{:.2f}".format(tuition)
    print("\nYear " + str(counter) + ":")
    print("\nTuition cost: $" + str.format(tuition_Format))
    print("Interest at: " + str(interest))
