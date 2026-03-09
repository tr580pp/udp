import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    values = input_data[1:]

    if n == 0:
        return

    # Create Linked List
    head = Node(int(values[0]))
    current = head
    for i in range(1, n):
        current.next = Node(int(values[i]))
        current = current.next

    # Reverse In-place
    new_head = reverse_list(head)

    # Print with space separation and NO trailing space
    res = []
    temp = new_head
    while temp:
        res.append(str(temp.data))
        temp = temp.next
    
    sys.stdout.write(" ".join(res) + "\n")

if __name__ == "__main__":
    main()