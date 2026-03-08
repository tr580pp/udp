class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

max_twin = 0
for i in range(n // 2):
    max_twin = max(max_twin, arr[i] + arr[n - 1 - i])
print(max_twin)