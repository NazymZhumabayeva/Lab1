import math
a = int(input())
b = int(input())
n = math.gcd(a,b)

def drob(a, b):
    print(a//n) 
    print(b//n)

drob(a, b)