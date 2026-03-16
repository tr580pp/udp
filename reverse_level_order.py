from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def reverse_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return result[::-1]

n = int(input())
values = list(map(int, input().split()))

root = None
for v in values:
    root = insert(root, v)

print(*reverse_level_order(root))