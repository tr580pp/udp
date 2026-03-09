class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def rearrange(head):
    curr = head
    flag = True
    while curr and curr.next:
        if flag:
            if curr.data > curr.next.data:
                curr.data, curr.next.data = curr.next.data, curr.data
        else:
            if curr.data < curr.next.data:
                curr.data, curr.next.data = curr.next.data, curr.data
        flag = not flag
        curr = curr.next
    return head

n = int(input())
values = list(map(int, input().split()))

head = Node(values[0])
curr = head
for v in values[1:]:
    curr.next = Node(v)
    curr = curr.next

head = rearrange(head)

result = []
curr = head
while curr:
    result.append(str(curr.data))
    curr = curr.next

print(" -> ".join(result))