import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py: return False
    if rank[px] < rank[py]: px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]: rank[px] += 1
    return True

def mst_with_edge(n, edges, forced_idx):
    parent = list(range(n+1))
    rank = [0] * (n+1)
    u, v, w = edges[forced_idx]
    union(parent, rank, u, v)
    total = w
    cnt = 1
    for i, (eu, ev, ew) in enumerate(sorted(edges, key=lambda x: x[2])):
        if eu == u and ev == v and ew == w and i == forced_idx:
            continue
        if union(parent, rank, eu, ev):
            total += ew
            cnt += 1
    if cnt < n: return -1
    return total

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

for i in range(m):
    print(mst_with_edge(n, edges, i))