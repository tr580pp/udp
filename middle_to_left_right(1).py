import sys
input = sys.stdin.readline

def recurse(arr, left, right, result):
    if left < 0 and right >= len(arr):
        return
    if left == right:
        result.append(arr[left])
        return
    if left >= 0:
        result.append(arr[left])
    if right < len(arr) and right != left:
        result.append(arr[right])
    recurse(arr, left - 1, right + 1, result)

n = int(input())
values = list(map(int, input().split()))

mid = n // 2

result = []
if n % 2 == 1:
    recurse(values, mid, mid, result)
else:
    result.append(values[mid - 1])
    result.append(values[mid])
    recurse(values, mid - 2, mid + 1, result)

print(", ".join(map(str, result)))