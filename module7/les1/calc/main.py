from calc import calc
from print_mode import printMode

a = int(input(': '))
b = int(input(': '))
c = str(input(': '))
answer = calc(a,b,c)
print(printMode(a,b,c,answer))