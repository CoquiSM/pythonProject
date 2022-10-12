##Problem 1
dayNum = int(input("Enter A number between 1-7\n"))
if (dayNum <= 7):
        if(dayNum == 1):
            print("The day is Monday")
            breakpoint()
        elif(dayNum == 2):
            print("The day is Tuesday")
            breakpoint()
        elif(dayNum == 3):
            print("The day is Wednesday")
            breakpoint()
        elif(dayNum == 4):
            print("The day is Thursday")
            breakpoint()
        elif(dayNum == 5):
            print("The day is Friday")
            breakpoint()
        elif(dayNum == 6):
            print("The day is Saturday")
            breakpoint()
        elif(dayNum == 7):
            print("The day is Sunday")
            breakpoint()
elif(dayNum > 7):
    print("ERROR Number must be smaller than 7 and an integer")
    breakpoint()
    exit()









