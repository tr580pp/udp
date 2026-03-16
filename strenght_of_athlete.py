n, k = map(int, input().split())
strengths = list(map(int, input().split()))

visited = set()
for s in strengths:
    for spot in range(s, k+1, s):
        visited.add(spot)

print(k - len(visited))