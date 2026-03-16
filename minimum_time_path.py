import heapq
from collections import defaultdict

def solve():
    n = int(input())
    m = int(input())
    
    roads = []
    for _ in range(m):
        line = list(map(int, input().split()))
        roads.append(line)
    
    T = int(input())
    C = int(input())
    
    graph = defaultdict(list)
    for road in roads:
        a, b = road[0], road[1]
        graph[a].append(b)
        graph[b].append(a)
    
    def get_wait(time):
        cycle = time // C
        if cycle % 2 == 0:
            return 0
        else:
            return C - (time % C)
    
    # dist[node][0] = min, dist[node][1] = second min
    dist = [[float('inf')] * 2 for _ in range(n+1)]
    dist[1][0] = 0
    
    heap = [(0, 1)]
    
    while heap:
        d, u = heapq.heappop(heap)
        
        if d > dist[u][1]:
            continue
        
        wait = get_wait(d)
        depart = d + wait
        
        for v in graph[u]:
            nd = depart + T
            if nd < dist[v][0]:
                dist[v][1] = dist[v][0]
                dist[v][0] = nd
                heapq.heappush(heap, (nd, v))
            elif dist[v][0] < nd < dist[v][1]:
                dist[v][1] = nd
                heapq.heappush(heap, (nd, v))
    
    print(dist[n][1])

solve()