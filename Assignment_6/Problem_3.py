import circleCalc
import rectangleCalc
import triangleCalc

holder1 = 0
holder2 = 0
holder3 = 0
holder4 = 0

choice = str(input("Choose a Shape: " + "\nA:Rectangle" + "\nB:Triangle" + "\nC:Circle"))

if (choice.lower() == "a"):
    holder1 = float(input("\nEnter length"))
    holder2 = float(input("\nEnter width"))
    rectangleCalc.rectangleAreaPerim(holder1, holder2)

elif(choice.lower() == "b"):
    holder1 = float(input("\nEnter height"))
    holder2 = float(input("\nEnter base"))
    holder3 = float(input("\nEnter side B"))
    holder4 = float(input("\nEnter side C"))
    triangleCalc.triangleAreaPerim(holder1,holder2,holder3,holder4)

elif(choice.lower() == "c"):
    holder1 = float(input("\nEnter radius"))
    circleCalc.circleAreaPerim(holder1)









