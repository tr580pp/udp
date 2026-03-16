import bisect

n, m = map(int, input().split())
difficulty = list(map(int, input().split()))
profit = list(map(int, input().split()))
worker = list(map(int, input().split()))

jobs = sorted(zip(difficulty, profit))

best = []
max_profit = 0
for d, p in jobs:
    max_profit = max(max_profit, p)
    best.append((d, max_profit))

total = 0
for ability in worker:
    idx = bisect.bisect_right(best, (ability, float('inf'))) - 1
    if idx >= 0:
        total += best[idx][1]

print(total)