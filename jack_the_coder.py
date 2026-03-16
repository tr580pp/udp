import heapq
from collections import Counter, deque

s = input()
dt = int(input())

freq = Counter(s)
max_heap = [(-cnt, char) for char, cnt in freq.items()]
heapq.heapify(max_heap)

result = []
wait_queue = deque()

while max_heap or wait_queue:
    if wait_queue and wait_queue[0][2] <= len(result):
        cnt, char, _ = wait_queue.popleft()
        heapq.heappush(max_heap, (cnt, char))

    if max_heap:
        cnt, char = heapq.heappop(max_heap)
        result.append(char)
        if cnt + 1 < 0:
            wait_queue.append((cnt + 1, char, len(result) + dt - 1))
    else:
        result.append(' ')

res = ''.join(result)
if ' ' in res:
    print("Invalid")
else:
    print(res)