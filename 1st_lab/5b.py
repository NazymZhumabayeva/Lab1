# n = int(input())
# i = 2
# #while i <= n:
# #    i = i + 1
# #    if n % i == 0:
# #        print(i)
# #        break
# while n % i:
#     i += 1
# print(i)
n = int(input())
i = 2
cnt = 0
b = 0
import math
while i < math.sqrt(n) + 1:
    if cnt != 1:
        if n % 2 == 0:
            cnt += 1
            b = i
    i += 1
if cnt != 1:
    print(n)
else:
    print(b)