import math
choice = str(input("\nA: Cos(x)" + "\nB: Sin(x)" + "\nC: Tan(x)" + "\nD: Log10" + "\nE: sqrt(x)" + "\nF:hypot(x,y)"))

if choice.lower() == "a":
    print("\nCosine calculation chosen:")
    print(math.cos((int(input("Enter Number")))))
elif(choice.lower() == "b"):
    print("\nSine calculation chosen:")
    print(math.sin((int(input("Enter Number")))))
elif(choice.lower() == "c"):
    print("\nTangent calculation chosen:")
    print(math.tan((int(input("Enter Number")))))

elif(choice.lower() == "d"):
    print("\nLogarithm calculation chosen:")
    print(math.log((int(input("Enter Number")))))

elif(choice.lower() == "e"):
    print("\nSqrt calculation Chosen:")
    print(math.sqrt((int(input("Enter Number")))))

elif(choice.lower() == "f"):
    print("\nHypot calculation Chosen:")
    print(math.hypot((int(input("Enter Number")))))







# .LowerCase():
