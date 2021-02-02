userInput = input("Please enter an integer: ")

try:
    userInput = float(userInput)
except:
    numOne = float(39)
    print(f"This is not a valid number. We'll use {userInput} instead.")

print(f"Your selected integer is: {userInput}")

if(userInput % 3 == 0 and userInput % 5 == 0):
    print("This integer is divisible by 3 and 5.")
elif(userInput % 3 == 0):
    print("This integer is divisible by 3.")
elif(userInput % 5 == 0):
    print("This integer is divisible by 5.")
else:
    print("This integer is not divisible by 3 or 5.")
