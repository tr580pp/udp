import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    if n <= 0:
        print("False")
        return
        
    values = input_data[1:n+1]
    pos = int(input_data[n+1])

    nodes = [Node(int(v)) for v in values]
    for i in range(n - 1):
        nodes[i].next = nodes[i+1]

    if pos > 0 and pos <= n:
        nodes[n-1].next = nodes[pos-1]
    elif pos != -1 and pos != 0:
        print("Invalid")
        return

    if has_cycle(nodes[0]):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()