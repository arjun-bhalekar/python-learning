# in python all exceptions are checked only.
import builtins

#help(builtins)
# ZeroDivisionError
#print(1/0)

#values = [1,'2']
#sum(values) # TypeError

try:
    i=10
    result = 10/i
    ans = result + '20'
#except ZeroDivisionError:
except (ZeroDivisionError, TypeError) as e:
    print(e)
    result = 0
else:
    print('exception is not occured')
finally:
    print(result)