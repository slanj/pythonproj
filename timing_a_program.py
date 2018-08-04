import time

def c_to_f(c):
    return c*9/5 + 32

t0 = time.clock()
c_to_f(1000000)
t1 = time.clock() - t0
print("time of execution: ", '{:f}'.format(t1), " seconds")