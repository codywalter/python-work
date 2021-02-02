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

numThree = input("Third number value: ")
try:
    numThree = float(numThree)
except:
    numThree = float(99)
    print(f"This is not a valid number. We'll use {numThree} instead.")

userValues = f'Your selected numbers are: {numOne}, {numTwo}, {numThree}'

print(userValues)

average = (numOne + numTwo + numThree) / 2

finalOutput = f'The average of your selected numbers is: {average}'

print(finalOutput)

questions = [
    inquirer.List('option',
                  message="What would you like to do next?",
                  choices=['Add', 'Subtract', 'Multiply', 'Exit'],
                  ),
]
answers = inquirer.prompt(questions)

# print(answers)

if answers == {'option': 'Add'}:
    add = numOne + numTwo + numThree
    print(f"Your selected numbers sum is: {add}")
    answers = inquirer.prompt(questions)
elif answers == {'option': 'Subtract'}:
    sub = numOne - numTwo - numThree
    print(f"Your selected numbers subtracted is: {sub}")
    answers = inquirer.prompt(questions)
elif answers == {'option': 'Multiply'}:
    mult = numOne * numTwo * numThree
    print(f"Your selected numbers multiplied is: {mult}")
    answers = inquirer.prompt(questions)
elif answers == {'option': 'Exit'}:
    exit()
