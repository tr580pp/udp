from collections import Counter

n = int(input())
tasks = list(map(int, input().split()))

freq = Counter(tasks)
rounds = 0

for count in freq.values():
    if count == 1:
        print(-1)
        exit()
    rounds += count // 3
    if count % 3 != 0:
        rounds += 1

print(rounds)