import module
pi = 3
print(pi)
print(module.pi)

print(module.area(3))

nameHandle = open('kids', 'w')

for i in range(2):
    name = input("Enter name: ")
    nameHandle.write(name + "\n")

nameHandle.close()

nameHandle = open('kids', 'r')

for line in nameHandle:
    print(line)

nameHandle.close()