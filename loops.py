x = 5
guess = int(input('Enter a value betveen 1 and 25: '))

while guess > x:
    guess -= 1
    print("Guessing...", "Maybe x is", guess)

while guess <  x:
    guess += 1
    print("Guessing...", "Maybe x is", guess)


print("Got it! x is", guess)

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))

