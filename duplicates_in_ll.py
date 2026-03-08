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

seen = set()
curr = head
prev = None
while curr:
    if curr.data in seen:
        prev.next = curr.next
    else:
        seen.add(curr.data)
        prev = curr
    curr = curr.next

result = []
curr = head
while curr:
    result.append(str(curr.data))
    curr = curr.next
print(" ".join(result))