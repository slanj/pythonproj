s = 'azcbobobegghakl'
i = 0
sub = ''
test = s[0]
while i < (len(s)-1):
  if s[i] <= s[i+1]:
    test += s[i+1]
  else:
    if len(sub) < len(test):
      sub = test
    test = s[i+1]
  if len(sub) < len(test):
    sub = test
  i += 1
print("Longest substring in alphabetical order is: " + str(sub))

#>>> chr(97)
#'a'
#>>> ord('a')
#97

