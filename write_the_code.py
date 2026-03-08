class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n = int(input())
values = list(map(int, input().split()))
k = int(input())

head = Node(values[0])
curr = head
for v in values[1:]:
    curr.next = Node(v)
    curr = curr.next

k = k % n
if k != 0:
    tail = head
    for _ in range(n - 1):
        tail = tail.next
    tail.next = head
    new_tail = head
    for _ in range(n - k - 1):
        new_tail = new_tail.next
    head = new_tail.next
    new_tail.next = None

result = []
curr = head
while curr:
    result.append(str(curr.data))
    curr = curr.next
print(" ".join(result))