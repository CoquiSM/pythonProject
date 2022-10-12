
def getUserInput():
    holdvalue = float(input("Enter score: "))
    return holdvalue


def calc_average(score1,score2,score3,score4,score5):
    averageOutput = float(score1 + score2 + score3 + score4 + score5/5)
    return averageOutput

#converts integer grade to letter value
def get_letter_grade(numGrade):
    outputLetter = " "
    if ((numGrade < 60) and (numGrade < 70)):
        outputLetter = "F"
    elif((numGrade >= 60) and (numGrade < 70)):
        outputLetter = "D"
    elif((numGrade >= 70) and (numGrade < 80)):
        outputLetter = "C"
    elif((numGrade >= 80) and (numGrade < 90)):
        outputLetter = "B"
    elif(numGrade >= 90):
        outputLetter = "A"
    return outputLetter

s1 = getUserInput()
s2 = getUserInput()
s3 = getUserInput()
s4 = getUserInput()
s5 = getUserInput()

print("\nLetter Grade for score " + "equals: " + " " + get_letter_grade(s1))
print("\nLetter Grade for score " + "equals: " + " " + get_letter_grade(s2))
print("\nLetter Grade for score " + "equals: " + " " + get_letter_grade(s3))
print("\nLetter Grade for score " + "equals: " + " " + get_letter_grade(s4))
print("\nLetter Grade for score " + "equals: " + " " + get_letter_grade(s5))

print("\nThe score average is: " + str(calc_average(s1,s2,s3,s4,s5)))

























