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

def is_perfect_family(node):
    if not node:
        return True
    left = node.left
    right = node.right
    if left and right:
        return False
    if not left and not right:
        return True
    return is_perfect_family(left) and is_perfect_family(right)

m = int(input())
values = list(map(int, input().split()))

root = None
for v in values:
    root = insert(root, v)

print(1 if is_perfect_family(root) else 0)