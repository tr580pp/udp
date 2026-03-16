from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_max_tree(arr):
    if not arr:
        return None
    max_idx = arr.index(max(arr))
    root = Node(arr[max_idx])
    root.left = build_max_tree(arr[:max_idx])
    root.right = build_max_tree(arr[max_idx+1:])
    return root

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

values = input().split()
if '-1' in values:
    values = values[:values.index('-1')]

val = int(input())

arr = [int(x) for x in values if x != 'null']
arr.append(val)

root = build_max_tree(arr)
print(*level_order(root))