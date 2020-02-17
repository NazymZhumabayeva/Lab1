a = int(input())
b = int(input())
c = int(input())
d = int(input())

def min4(a, b, c, d):
    d = min(min(min(a,b),c),d)
    print(d)

min4(a, b, c, d)