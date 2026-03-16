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

def inorder(node, result):
    if not node:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)

values = input().split()
if '-1' in values:
    values = values[:values.index('-1')]

k = int(input())
root = build_tree(values)

result = []
inorder(root, result)
print(result[k-1])