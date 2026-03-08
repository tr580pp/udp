class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

k = int(input())
all_elements = []

for _ in range(k):
    n = int(input())
    values = list(map(int, input().split()))
    all_elements.extend(values)

all_elements.sort()

head = Node(all_elements[0])
curr = head
for v in all_elements[1:]:
    curr.next = Node(v)
    curr = curr.next

result = []
curr = head
while curr:
    result.append(str(curr.data))
    curr = curr.next

print(" -> ".join(result))