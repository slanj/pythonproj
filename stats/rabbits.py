import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    if CURRENTRABBITPOP >= 10:
        for rabbit in range(CURRENTRABBITPOP):
            if (1.0 - (CURRENTRABBITPOP / MAXRABBITPOP)) > random.random():
                CURRENTRABBITPOP += 1

def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    for fox in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            if (CURRENTRABBITPOP / MAXRABBITPOP) > random.random():
                CURRENTRABBITPOP -= 1
                if (1/3.0) >= random.random():
                    CURRENTFOXPOP += 1
            else:
                if 0.1 >= random.random() and CURRENTFOXPOP > 10:
                    CURRENTFOXPOP -= 1

def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []

    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)

    rabbit_coeff = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
    fox_coeff = pylab.polyfit(range(len(fox_populations)), fox_populations, 2)

    pylab.plot(pylab.polyval(rabbit_coeff, range(len(rabbit_populations))))
    pylab.plot(pylab.polyval(fox_coeff, range(len(fox_populations))))

    pylab.plot(rabbit_populations, 'g')
    pylab.plot(fox_populations, 'r')
    pylab.show()

    return (rabbit_populations, fox_populations)



runSimulation(200)