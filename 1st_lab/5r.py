n = int(input())
i = 2
f0 = 0
f1 = 1

while i <= n:
    cur = f0 + f1
    f0 = f1
    f1 = cur
    i += 1

if n <= 1:
    print(n)
else:
    print(cur)
