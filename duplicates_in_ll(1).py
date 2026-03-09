n = int(input())
values = list(map(int, input().split()))

seen = set()
result = []
for v in values:
    if v not in seen:
        seen.add(v)
        result.append(str(v))

print(" ".join(result))