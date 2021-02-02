import inquirer


def userPrompt():
    userChar = input("Please enter a character between a and z (or A and Z): ")
    try:
        userChar = userChar.lower()
    except:
        userChar = "a"
        print(f"This is not a valid number. We'll use {userChar} instead.")

    print(f"Your selected chatacter is: {userChar}")

    def isVowel(userChar):
        allVowels = 'aeiou'
        return userChar in allVowels

    print(f"{userChar} is a vowel: {isVowel(userChar)}")


userPrompt()


def userQuestions():
    questions = [
        inquirer.List('option',
                      message="What would you like to do next?",
                      choices=['Select another character', 'Exit'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    if answers == {'option': 'Select another character'}:
        userPrompt()
        userQuestions()
    elif answers == {'option': 'Exit'}:
        print("See you next time!")
        exit()


userQuestions()
