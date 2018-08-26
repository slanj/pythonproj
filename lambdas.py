# lambda used to create anonymous functions

f1 = lambda x: x
print(f1("Hello lambda"))
print(f1(42))

f2 = lambda x,y: x+y
print(f2(40, 15))
print(f2('More', ' lambda'))

f3 = lambda x,y: 'factor' if (x%y == 0) else 'not factor'
print(f3(25, 5))
print(f3(42, 55))
