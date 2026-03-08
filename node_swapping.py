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

dummy = Node(0)
dummy.next = head
prev = dummy
curr = head

while curr and curr.next:
    a, b = curr, curr.next
    prev.next = b
    a.next = b.next
    b.next = a
    prev = a
    curr = a.next

result = []
curr = dummy.next
while curr:
    result.append(str(curr.data))
    curr = curr.next
print(" ".join(result))