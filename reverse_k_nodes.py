class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

values = list(map(int, input().split()))
values = values[:values.index(-1)]
k = int(input())

head = Node(values[0])
curr = head
for v in values[1:]:
    curr.next = Node(v)
    curr = curr.next

dummy = Node(0)
dummy.next = head
prev = dummy
curr = head

while curr:
    group = []
    temp = curr
    for _ in range(k):
        if temp:
            group.append(temp.data)
            temp = temp.next
    group.reverse()
    for val in group:
        curr.data = val
        curr = curr.next
    prev = curr if curr else prev

result = []
curr = dummy.next
while curr:
    result.append(str(curr.data))
    curr = curr.next
print(" ".join(result))