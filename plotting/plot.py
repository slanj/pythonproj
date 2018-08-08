from data import *
import pylab as plt

plt.figure('lin')
plt.clf()
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.title('Linear')
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.clf()
plt.plot(mySamples, myQuadratic)
plt.ylabel('qudratic function')
plt.title('Quadratic')

plt.figure('cube')
plt.clf()
plt.xlabel('sample points')
plt.ylabel('cubic function')
plt.plot(mySamples, myCubic)
plt.title('Cubic')

plt.figure('expo')
plt.clf()
plt.ylabel('exponential function')
plt.plot(mySamples, myExponential)
plt.title('Exponential')

plt.show()

