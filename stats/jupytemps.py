import numpy, pylab

def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

temps = loadFile()
print(temps)

lowTemps, highTemps = temps
diffTemps = list(numpy.array(highTemps) - numpy.array(lowTemps))
pylab.plot(range(1,32), diffTemps)
pylab.show()