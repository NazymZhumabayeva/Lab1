a = int(input())
b = int(input())
c = int(input())
if c>=a and b<=c:
    print(c)
elif a>=b and c<=a:
    print(a)
else:
    print(b)