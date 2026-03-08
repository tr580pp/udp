import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_lists(head1, head2):
    dummy = Node(0)
    tail = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2

    return dummy.next

def build_list(values):
    if not values:
        return None
    head = Node(int(values[0]))
    current = head
    for val in values[1:]:
        current.next = Node(int(val))
        current = current.next
    return head

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n1 = int(input_data[0])
    n2 = int(input_data[1])

    list1_vals = input_data[2 : 2 + n1]
    list2_vals = input_data[2 + n1 : 2 + n1 + n2]

    head1 = build_list(list1_vals)
    head2 = build_list(list2_vals)

    merged_head = merge_lists(head1, head2)

    result = []
    temp = merged_head
    while temp:
        result.append(str(temp.data))
        temp = temp.next
    
    print(" ".join(result))

if __name__ == "__main__":
    main()