import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

def distance(x1, y1, x2, y2):
    d = math.sqrt((x1 - x2)**2 + (y1 + y2)**2)
    print(float("{0:.5f}".format(d)))

distance(x1, y1, x2, y2)

#def distance(x1, y1, x2, y2):
#    res = ((x1- x2)**2 + (y1 - y2)**2) ** 0.5
#    return res
#print(distance(x1, y1, x2, y2))
