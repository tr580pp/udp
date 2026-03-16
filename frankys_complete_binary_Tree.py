def cycle_length(a, b):
    dist = 0
    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2
        dist += 1
    return dist + 1

n = int(input())
m = int(input())

results = []
for _ in range(m):
    a, b = map(int, input().split())
    results.append(str(cycle_length(a, b)))

print(' '.join(results))