low = 0
high = 100
ans = (high + low)//2
inp = ""

print("Please think of a number between 0 and 100!")

while True:
    print("Is your secret number " + str(ans) + "?")
    print("Enter 'h' to indicate the guess is too high.", end = " ")
    print("Enter 'l' to indicate the guess is too low.", end = " ")
    inp = input("Enter 'c' to indicate I guessed correctly. ")

    if inp == "h":
        high = ans
    elif inp == "l":
        low = ans
    elif inp == "c":
        print("Game over. Your secret number was: " + str(ans))
        break
    else:
        print("Sorry, I did not understand your input.")
    ans = (high + low)//2
