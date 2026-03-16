from collections import defaultdict

nH, nP = map(int, input().split())

out_deg = defaultdict(int)
in_deg = defaultdict(int)
graph = defaultdict(list)

for _ in range(nP):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    out_deg[a] += 1
    in_deg[b] += 1

tanks = [h for h in range(1, nH+1) if out_deg[h] > 0 and in_deg[h] == 0]
taps = [h for h in range(1, nH+1) if in_deg[h] > 0 and out_deg[h] == 0]

INF = float('inf')
dist = defaultdict(lambda: defaultdict(lambda: INF))

for u in graph:
    for v, d in graph[u]:
        dist[u][v] = min(dist[u][v], d)

for k in range(1, nH+1):
    for i in range(1, nH+1):
        for j in range(1, nH+1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

results = []
for t in tanks:
    for tap in taps:
        if dist[t][tap] != INF:
            results.append((t, tap, dist[t][tap]))

print(len(results))
for r in results:
    print(*r)