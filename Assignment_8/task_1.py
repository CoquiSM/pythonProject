contactbook = {'Bob' : ['1234-5678', '174th Street', 'bob@pnw.edu'], 'Amy' : ['333-2222','173rd Street', 'amy@pnw.edu']}

##Initialize variable
choice = 'f'

while choice.lower() !=  'd':
    choice = input("\nChoose a following operation: ( A ): Add || ( B ): Remove || ( C ): View Contact | ( D ): Stop ")
    if choice.lower() == "a": ##addition
        print("\na chosen")
        contactName = input("Enter Name\n")
        contactNumber = input("Enter phone number\n")
        contactAddress = input("Enter Adress\n")
        contactEmail = input("Enter Email\n")
        contactbook.update({contactName: [contactNumber,contactAddress,contactEmail]})
        print("Updated List:\n " + str(contactbook))

    elif choice.lower() == "b": ##deletion
        print("\nb chosen")
        print("\nAvailable contacts: ")
        print(contactbook.keys())
        namePointer = input("\nEnter contact you wish to remove: \n")
        contactbook.pop(namePointer)
        print("\nNew contact list: ")
        print(contactbook)

    elif choice.lower() == "c": ##viewing
        print("\nc chosen")
        print("\nAvailable contacts: ")
        print(contactbook.keys())
        choice = input("\nEnter Name For view")
        contactbook.get(choice,'Not Found')
        print(contactbook[choice])

    elif choice.lower() == "d": ##End program
        print("\nEnding program")











