while True:
    try:
        n = input('Please enter an integer: ')
        n = int(n)
        break
    except ValueError:
        print("Input not an integer. Try again")

print("Correct input of an integer! Thank you!")
