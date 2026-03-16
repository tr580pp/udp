data = list(map(int, input().split()))
n = data[0]
c = sorted(data[1:n+1])

total = 0
for i in range(n):
    total += abs(c[i] - (i+1))

print(total)