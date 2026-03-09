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

def is_palindrome(head):
    if not head or not head.next:
        return True

    # Find the middle using slow and fast pointers
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half
    second_half = reverse_list(slow)
    first_half = head
    
    # Compare halves
    temp_second = second_half
    result = True
    while temp_second:
        if first_half.data != temp_second.data:
            result = False
            break
        first_half = first_half.next
        temp_second = temp_second.next
    
    return result

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    current_idx = 1
    
    for _ in range(t):
        nodes = []
        while current_idx < len(input_data):
            val = int(input_data[current_idx])
            current_idx += 1
            if val == -1:
                break
            nodes.append(val)
        
        if not nodes:
            # Case for an empty list ending immediately with -1
            print("true")
            continue

        # Build Linked List
        head = Node(nodes[0])
        curr = head
        for i in range(1, len(nodes)):
            curr.next = Node(nodes[i])
            curr = curr.next
            
        if is_palindrome(head):
            print("true")
        else:
            print("false")

if __name__ == "__main__":
    main()