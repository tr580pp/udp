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

def inorder(node, result):
    if not node:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)

values = list(map(int, input().split()))
if -1 in values:
    values = values[:values.index(-1)]

root = None
for v in values:
    root = insert(root, v)

result = []
inorder(root, result)

min_diff = float('inf')
for i in range(1, len(result)):
    min_diff = min(min_diff, result[i] - result[i-1])

print(min_diff)