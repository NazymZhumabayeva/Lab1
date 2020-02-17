x = float(input())
y = float(input())

def IsPointInSquare(x, y):
    if -1 <= x <= 1:
        if -1 <= y <= 1:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

IsPointInSquare(x, y)

#def IsPointInSquare(x, y):
#    if abs(x) <= 1 and abs(y) <= 1:
#        return "YES"
#    else:
#        return "NO"
#print(IsPointInSquare(x, y))