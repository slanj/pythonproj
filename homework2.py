s = 'obobobbobobpnbobobboobcbobobb'

i = 0
j = 0
count = 0
appear = False

while i < (len(s) - 2):
  j = i
  for char in 'bob':
    if char == s[j]:
      appear = True
      j += 1
    else:
      appear = False
      break
  i += 1
  if appear == True:
    count += 1

print("Number of times bob occurs is: " + str(count))
