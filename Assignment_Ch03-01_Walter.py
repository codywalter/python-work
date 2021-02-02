import inquirer

numList = []

numOne = input("First number value: ")
try:
    numOne = float(numOne)
    numList.append(numOne)
except:
    numOne = float(39)
    numList.append(numOne)
    print(f"This is not a valid number. We'll use {numOne} instead.")

numTwo = input("Second number value: ")
try:
    numTwo = float(numTwo)
    numList.append(numTwo)
except:
    numTwo = float(54)
    numList.append(numTwo)
    print(f"This is not a valid number. We'll use {numTwo} instead.")

numThree = input("Third number value: ")
try:
    numThree = float(numThree)
    numList.append(numThree)
except:
    numThree = float(99)
    numList.append(numThree)
    print(f"This is not a valid number. We'll use {numThree} instead.")

userValues = f'Your selected numbers are: {numOne}, {numTwo}, {numThree}'

print(userValues)
numList.sort()
print(f"Your selected numbers in ascending are: {numList}")
