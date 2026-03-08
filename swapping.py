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

nodes = []
curr = head
while curr:
    nodes.append(curr)
    curr = curr.next

i, j = k - 1, n - k
if i != j:
    nodes[i].data, nodes[j].data = nodes[j].data, nodes[i].data

curr = head
result = []
while curr:
    result.append(str(curr.data))
    curr = curr.next

print(" -> ".join(result))