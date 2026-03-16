import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

n, m, k = map(int, input().split())
costs = list(map(int, input().split()))

roads = []
for _ in range(m):
    line = list(map(int, input().split()))
    u, v, l = line[0], line[1], line[2]
    tokens = set(line[3:3+l])
    roads.append((u, v, tokens))

best = -1
for mask in range(1 << k):
    token_set = set()
    for i in range(k):
        if mask & (1 << i):
            token_set.add(i+1)
    
    parent = list(range(n+1))
    rank = [0] * (n+1)
    connected = 0
    
    for u, v, tokens in roads:
        if tokens.issubset(token_set):
            if union(parent, rank, u, v):
                connected += 1
    
    if connected == n-1:
        cost = sum(costs[i] for i in range(k) if mask & (1 << i))
        if best == -1 or cost < best:
            best = cost

print(best)