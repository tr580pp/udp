from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] == 'null':
        return None
    root = Node(int(values[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] != 'null':
            node.left = Node(int(values[i]))
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'null':
            node.right = Node(int(values[i]))
            queue.append(node.right)
        i += 1
    return root

def lca(root, a, b):
    if not root:
        return None
    if a < root.data and b < root.data:
        return lca(root.left, a, b)
    if a > root.data and b > root.data:
        return lca(root.right, a, b)
    return root

values = input().split()
if '-1' in values:
    values = values[:values.index('-1')]

a, b = map(int, input().split())
root = build_tree(values)
print(lca(root, a, b).data)