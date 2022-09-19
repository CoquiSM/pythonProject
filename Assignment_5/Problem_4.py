import random
computerNum = random.randint(1, 6) + random.randint(1, 6)
tries = 3
flag = False
userOption = ""


while(flag != True):
 answerInput = int(input("\nSelect a number between 2-12"))
 if(answerInput == computerNum):
     print("Correct! The number is " + str(computerNum) + " you win")
     tries -=1
     print("remaining tries: " + tries)

 elif(answerInput != computerNum):
     tries -= 1
     print("\nWrong Answer!")
     print("\ntries remaining: 2")
     print("Re-rolling dice...")
     computerNum = random.randint(1, 6) + random.randint(1, 6)

 if(tries == 0):
     print("Computer Wins!")
     userOption = str(input("\nWant to play again? Y/N"))
     if(answerInput == ("N") or ("n") or ("No") or ("no")):
         print("Game ends")
         flag = True





