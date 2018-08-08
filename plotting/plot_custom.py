import pylab as plt
from data import *

plt.figure('lin quad')
plt.clf()
plt.subplot(211)
plt.ylim(0, 900)
plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
plt.subplot(212)
plt.ylim(0, 900)
plt.plot(mySamples, myQuadratic, 'ro', label = 'quadratic', linewidth = 3.0)
plt.legend(loc = "upper left")
plt.title('Linear vs. Quadratic')

plt.figure('cube exp')
plt.clf()
plt.subplot(121)
plt.ylim(0, 140000)
plt.plot(mySamples, myCubic, 'g^', label = 'cubic', linewidth = 4.0)
plt.subplot(122)
plt.ylim(0, 140000)
plt.plot(mySamples, myExponential, 'r--', label = 'exponential', linewidth = 4.0)
plt.legend()
plt.title('Cubic vs. Exponential')

plt.figure('cube exp log')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label = 'cubic', linewidth = 4.0)
plt.plot(mySamples, myExponential, 'r--', label = 'exponential', linewidth = 4.0)
plt.yscale('log')
plt.legend()
plt.title('Cubic vs. Exponential')

plt.show()