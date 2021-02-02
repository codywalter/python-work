import inquirer
import emoji

print("Palindrome Game is an interactive command line application that takes a user's input and checks to see if it is a palindrome.")


def palGame():

    userInput = input("Please enter a word: ")

    def isPalindrome(word):
        return word == word[::-1]

    palindromeCheck = isPalindrome(userInput)

    if palindromeCheck == True:
        print(f'{userInput} is a palindrome! {emoji.emojize(":money-mouth_face:")}')
    else:
        print(
            f'{userInput} is not a palindrome... {emoji.emojize(":face_with_medical_mask:")}')


def welcome():
    questions = [
        inquirer.List('user',
                      message="What would you like to do?",
                      choices=['Play Palindrome Game', 'Exit'],
                      ),
    ]

    answers = inquirer.prompt(questions)

    if answers == {'user': 'Play Palindrome Game'}:
        palGame()
        welcome()
    elif answers == {'user': 'Exit'}:
        print("See you next time!")
        exit()


welcome()
