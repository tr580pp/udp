import heapq

k = int(input())
all_elements = []

for _ in range(k):
    n = int(input())
    values = list(map(int, input().split()))
    all_elements.extend(values)

all_elements.sort()
print(" ".join(map(str, all_elements)))