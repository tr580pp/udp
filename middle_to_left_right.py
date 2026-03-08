class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

head = Node(values[0])
curr = head
for v in values[1:]:
    curr.next = Node(v)
    curr = curr.next

arr = []
curr = head
while curr:
    arr.append(curr.data)
    curr = curr.next

mid = n // 2
result = []
if n % 2 == 1:
    recurse(arr, mid, mid, result)
else:
    result.append(arr[mid - 1])
    result.append(arr[mid])
    recurse(arr, mid - 2, mid + 1, result)

print(", ".join(map(str, result)))