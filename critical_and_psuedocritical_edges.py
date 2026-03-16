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

def mst_weight(n, edges, skip=-1, force=-1):
    parent = list(range(n))
    rank = [0] * n
    weight = 0
    cnt = 0
    if force != -1:
        u, v, w = edges[force]
        union(parent, rank, u, v)
        weight += w
        cnt += 1
    for i, (u, v, w) in enumerate(edges):
        if i == skip: continue
        if union(parent, rank, u, v):
            weight += w
            cnt += 1
    if cnt < n-1: return float('inf')
    return weight

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, d = map(int, input().split())
    edges.append((a, b, d))

edges_sorted = sorted(range(m), key=lambda i: edges[i][2])
sorted_edges = [edges[i] for i in edges_sorted]

base = mst_weight(n, sorted_edges)
critical = pseudo = 0

for i in range(m):
    if mst_weight(n, sorted_edges, skip=i) > base:
        critical += 1
    elif mst_weight(n, sorted_edges, force=i) == base:
        pseudo += 1

print(critical, pseudo)