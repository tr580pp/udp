n = int(input())
values = list(map(int, input().split()))

for i in range(0, n - 1, 2):
    values[i], values[i+1] = values[i+1], values[i]

print(" ".join(map(str, values)))