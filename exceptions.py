'''
Exceptions raised by any statement in body of TRY are
handled by the EXCEPT statement and execution continues
after the body of the EXCEPT statement
'''

# TRY says: try to execute each of these instructions in turn.
# But if an exception is raised, stop that processing,
# jump to EXCEPT clause and execute those statements.
try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print(a/b)
    print("Zashibis podelili")
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Cannot divide by zero")
except:
    print("Bug in user input")
else:
    print("Everything is OK!")
finally:
    print("Done")

print('Outside')
