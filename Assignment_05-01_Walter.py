import inquirer

print("Sum Game is a command line application that takes user entered values and adds them up based on even and odd values.")


def sumGame():

    userAnswers = []
    evenNums = []
    oddNums = []

    def userPrompt():
        answers = input("Please enter an integer: ")
        try:
            answers = int(answers)
        except:
            answers = int(6)
            print(f"This is not a valid number. We'll use {answers} instead.")
        if answers % 2 == 0:
            evenNums.append(answers)
            userAnswers.append(answers)
        elif answers % 2 != 0:
            oddNums.append(answers)
            userAnswers.append(answers)

    for x in range(10):
        userPrompt()

    userAnswers.sort()
    evenNums.sort()
    oddNums.sort()

    print(
        f"Here are your selected integers: {userAnswers}. Your selected even numbers are: {evenNums}. Your selected odd numbers are: {oddNums}.")

    print(f"The sum of the even numbers is: {sum(evenNums)}")
    print(f"The sum of the odd numbers is: {sum(oddNums)}")


def welcome():
    questions = [
        inquirer.List('user',
                      message="What would you like to do?",
                      choices=['Play Sum Game', 'Exit'],
                      ),
    ]

    answers = inquirer.prompt(questions)

    if answers == {'user': 'Play Sum Game'}:
        sumGame()
        welcome()
    elif answers == {'user': 'Exit'}:
        print("See you next time!")
        exit()


welcome()
