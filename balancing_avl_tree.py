class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def rotate_right(y):
    x = y.left
    t = x.right
    x.right = y
    y.left = t
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    y = x.right
    t = y.left
    y.left = x
    x.right = t
    update_height(x)
    update_height(y)
    return y

def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    update_height(root)
    balance = get_balance(root)

    if balance > 1 and data < root.left.data:
        return rotate_right(root)
    if balance < -1 and data > root.right.data:
        return rotate_left(root)
    if balance > 1 and data > root.left.data:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if balance < -1 and data < root.right.data:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    return root

def inorder(node, result):
    if not node:
        return
    inorder(node.left, result)
    result.append(node.data)
    inorder(node.right, result)

n = int(input())
values = list(map(int, input().split()))

root = None
for v in values:
    root = insert(root, v)

result = []
inorder(root, result)
print(*result)