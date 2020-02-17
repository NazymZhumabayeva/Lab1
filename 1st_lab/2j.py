n = int(input())
#sum = 0
#for i in range(1, n+1,1):
#    sum += i*(i-1)
#print(sum)

print("+".join("{}*{}".format(k, k + 1) for k in range(1, n)), end="=")
print(sum(k * (k + 1) for k in range(1, n)))