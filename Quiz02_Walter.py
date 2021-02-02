def yesNo(num):
    if (num % 3 == 0) and (num % 18 == 0) and (num % 54 != 0) or (num % 88 == 0):
        print(
            f"The number {num} is divisible by both 3 and 18 but not 54, or it is divisible by 88")


for x in range(1, 5001):
    yesNo(x)
