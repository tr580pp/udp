n = int(input())
values = list(map(int, input().split()))

max_twin = 0
for i in range(n // 2):
    max_twin = max(max_twin, values[i] + values[n - 1 - i])

print(max_twin)