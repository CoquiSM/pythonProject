print("System Reboot Complete")
answer = str(input("Is Problem Fixed? Y/N"))
if answer == "Y":
    print("Wifi connection found, resuming initialization")
    exit()
else:
    print("Wifi connection not found, reboot router and try again")
    answer = str(input("Is Problem Fixed? Y/N"))
    if answer == "Y":
        print("Reboot complete")
        exit()
    elif(answer == "N"):
        print("Make sure cables between the modem and the "
            "router are connected properly")
        answer = str(input("Is Problem Fixed? Y/N"))
        if answer == "Y":
            print("Reboot complete")
            exit()
        elif(answer == "N"):
            print("Move router to a new location and try again")
            answer = str(input("Is Problem Fixed? Y/N"))
            if (answer == "Y"):
                print("Reboot complete")
                exit()
            elif(answer == "N"):
                print("Get a new router")
                exit()






