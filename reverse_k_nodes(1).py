values = list(map(int, input().split()))
values = values[:values.index(-1)]
k = int(input())

result = []
for i in range(0, len(values), k):
    result.extend(values[i:i+k][::-1])

print(" ".join(map(str, result)))