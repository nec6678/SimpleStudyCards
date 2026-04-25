## Simple Study Cards version 1.0.1
## Copyright 2026 Leo Feldman

### IMPORTS ###
import linecache
import sys
import os

### STARTING PROCESS ###
def relaunch():
    # Clears terminal
    print("\033[H\033[J", end="")

    # Prints starting text
    print("Simple Study Cards version 1.0.1")
    print("Copyright 2026 Leo Feldman")
    print("--")

### FUNCTION SELECT ###
def startSelect():
    print("Please make a selection:")
    print("1.) Create new set")
    print("2.) Load saved set")
    print("3.) Delete saved set")
    print("4.) Quit")
    global option
    option = int(input("> "))
    if option == 1:
        newSet()
    elif option == 2:
        loadSet()
    elif option == 3:
        deleteSet()
    elif option == 4:
        sys.exit(0)
    else:
        print("Please enter the number corresponding to one of the options above.")
        startSelect()

### CREATE NEW SET ###
def newSet():
    # Creates new file for storing question data
    newSetName = str(input("What is the name of the new set? "))
    newSetQuestions = int(input("How many terms? "))
    with open(f"{newSetName.casefold()}.ssc", "w") as file:
        file.write("SIMPLE STUDY CARDS DATA FILE\n")
        file.write("YOU REALLY SHOULDN'T TOUCH ANYTHING HERE\n")
        file.write("--\n")
        file.write(f"{newSetQuestions}\n")
    # Gets question data
    print("--")
    newSetQuestionIndex = int(0)
    while newSetQuestionIndex < newSetQuestions:
        newSetQuestionIndex = newSetQuestionIndex + 1
        print("Question", newSetQuestionIndex, "name?")
        questionName = input("> ")
        print("Question", newSetQuestionIndex, "answer?")
        questionAnswer = input("> ")
        # Appends question data to previously created data file
        # Data file uses .ssc extension, same data as .txt file
        # Do not rename .ssc file without updating file 'open' commands
        with open(f"{newSetName.casefold()}.ssc", "a") as file:
            file.write(f"{newSetQuestionIndex}\n")
            file.write(f"{questionName}\n")
            file.write(f"{questionAnswer.casefold()}\n")
    print("\nSet created successfully.\n")
    startSelect()

###LOAD SET ###
def loadSet():
    global fileName
    fileName = str(input("What is the name of the set you want to load? "))
    reloadSet()
### LOAD/RELOAD SET ###
def reloadSet():
    loadSetQuestionIndex = int(0)
    lineIndex = int(6)
    questionsCorrect = int(0)
    loadFileName = fileName.casefold()
    loadSetQuestions = int(linecache.getline(f"{loadFileName}.ssc", 4))
    print(f"\n{loadSetQuestions} Questions")
    while loadSetQuestionIndex < loadSetQuestions:
        loadSetQuestionIndex = loadSetQuestionIndex + 1
        print(f"\nQuestion {loadSetQuestionIndex}:")
        questionData = linecache.getline(f"{loadFileName}.ssc", lineIndex)
        lineIndex = lineIndex + 1
        print(questionData)
        userAnswer = input("Your answer? ")
        correctAnswer = linecache.getline(f"{loadFileName}.ssc", lineIndex)
        lineIndex = lineIndex + 2
        if f"{userAnswer.casefold()}\n" == correctAnswer:
            print("Correct!")
            questionsCorrect = questionsCorrect + 1
        else:
            print(f"Incorrect! The correct answer was {correctAnswer}")
    print("\nSet complete!")
    print(f"Score: {questionsCorrect}/{loadSetQuestions}")
    inquirePlayAgain()

### RELOAD SET INQUIRY ###
def inquirePlayAgain():
        playAgain = str(input("Play again? (Y/N) "))
        if playAgain.casefold() == "y":
            reloadSet()
        elif playAgain.casefold() == "n":
            print()
            startSelect()
        else:
            print("Please answer either 'Y' or 'N'.")
            inquirePlayAgain()

### READ MANUAL ###
## This feature has been discontinued.
# def readManual():
#     with open("SimpleStudyCards_manual.txt", "r") as f:
#         content = f.read()
#         print()
#         print(content)
#     print()
#     startSelect()

### DELETE SET ###
def deleteSet():
    nameToDelete = str(input("What is the name of the set you want to delete? "))
    fileToDelete = (f"{nameToDelete.casefold()}.ssc")
    if os.path.exists(fileToDelete):
        def inquireCommitDelete():
            commitDelete = str(input(f"Are you sure you want to delete the set '{nameToDelete}'? (Y/N)"))
            if commitDelete.casefold() == "y":
                os.remove(fileToDelete)
                print(f"\nSet '{nameToDelete}' deleted successfully.\n")
                startSelect()
            elif commitDelete.casefold() == "n":
                print(f"\nSet '{nameToDelete}' not deleted.\n")
                startSelect()
            else:
                print("Please answer either 'Y' or 'N'.")
                inquireCommitDelete()
        inquireCommitDelete()
    else:
        print(f"\nSet '{nameToDelete}' does not exist.\n")
        startSelect()

### RUN FUNCTIONS ###
relaunch()
startSelect()