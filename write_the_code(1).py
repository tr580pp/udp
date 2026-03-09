n = int(input())
values = list(map(int, input().split()))
k = int(input())

k = k % n
if k == 0:
    print(" ".join(map(str, values)))
else:
    rotated = values[n-k:] + values[:n-k]
    print(" ".join(map(str, rotated)))