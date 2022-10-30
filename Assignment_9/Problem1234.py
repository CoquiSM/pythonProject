import re
sentenceBook = {'default': ['sample', 6]}
bookIteration = 0
flag = False
sentenceList = []
lowerCaseList = []
while flag is False:
    # Counter is for the number qty of letters
    counter = 0

    # Sentence number for better to for dictionary lookup
    bookIteration += 1

    userInput = str(input("\nEnter a sentence"))
    if userInput == "DONE":
        flag = True
        print("\nProgram done:")
        print(sentenceList)
        print("\nAll LowerCase: ")
        print(lowerCaseList)
    else:
        # Cool functionality
        userInput = re.sub("[^A-Za-z]+", '', userInput)
        userInput = userInput.replace(" ", "")

        sentenceList.append(userInput)
        userInput = userInput.lower()
        lowerCaseList.append(userInput)

        # updates sentence book  with sentence and qty of letters
        counter = len(userInput)
        sentenceBook.update({str(bookIteration): [userInput, counter]})
        print("\nSentence book updated: " + str(sentenceBook))

