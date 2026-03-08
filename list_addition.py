class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def build(values):
    head = Node(values[0])
    curr = head
    for v in values[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head

def to_list(head):
    arr = []
    while head:
        arr.append(head.data)
        head = head.next
    return arr

m = int(input())
list1 = list(map(int, input().split()))
n = int(input())
list2 = list(map(int, input().split()))

h1 = build(list1)
h2 = build(list2)

arr1 = to_list(h1)
arr2 = to_list(h2)

num1 = int("".join(map(str, arr1[::-1])))
num2 = int("".join(map(str, arr2[::-1])))

total = num1 + num2
digits = [int(d) for d in str(total)][::-1]

head = Node(digits[0])
curr = head
for d in digits[1:]:
    curr.next = Node(d)
    curr = curr.next

result = []
curr = head
while curr:
    result.append(str(curr.data))
    curr = curr.next

print(" ".join(result))