import inquirer

numOne = input("First number value: ")
try:
    numOne = float(numOne)
except:
    numOne = float(39)
    print(f"This is not a valid number. We'll use {numOne} instead.")

numTwo = input("Second number value: ")
try:
    numTwo = float(numTwo)
except:
    numTwo = float(54)
    print(f"This is not a valid number. We'll use {numTwo} instead.")

userValues = f'Your selected numbers are: {numOne}, {numTwo}'

print(userValues)


def userQuestions():
    questions = [
        inquirer.List('option',
                      message="What would you like to do next?",
                      choices=['Add', 'Subtract', 'Multiply', 'Exit'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    if answers == {'option': 'Add'}:
        add = numOne + numTwo
        print(f"Your selected numbers sum is: {add}")
        userQuestions()
    elif answers == {'option': 'Subtract'}:
        sub = numOne - numTwo
        print(f"Your selected numbers subtracted is: {sub}")
        userQuestions()
    elif answers == {'option': 'Multiply'}:
        mult = numOne * numTwo
        print(f"Your selected numbers multiplied is: {mult}")
        userQuestions()
    elif answers == {'option': 'Exit'}:
        print("See you next time!")
        exit()


userQuestions()
