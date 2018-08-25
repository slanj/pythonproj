import re

hand = open('story.txt', 'r', encoding='UTF-8')
for line in hand:
    line = line.rstrip()
    #Finding any paragraph with Alice and Door
    if re.search('^Alice.*door', line):
        print(line)
    #Find what rabbit is doing
    #using non-blank [^ ] pattern
    rabbit = re.findall('rabbit.[^ ]+', line)
    #separate what to find and what to extract with ()
    rabbit2 = re.findall('(rabbit.[a-z]+)\s', line)
    if rabbit and rabbit == rabbit2:
        print(rabbit2, '\n')

