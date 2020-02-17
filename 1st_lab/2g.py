n = int(input())
k = int(input())
d1 = 1
for i in range(1, n+1, 1):
    d1 *= i
d2 = 1
for j in range(1, k+1, 1):
    d2 *= j
d3 = 1 
for k in range(1, n-k+1, 1):
    d3 *= k 
print(int((d1)/(d2*d3)))