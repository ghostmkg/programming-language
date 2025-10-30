class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Save next node
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_node       # Move current forward
    return prev  # New head of reversed list

# Helper to print the list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original List:")
print_list(head)

reversed_head = reverse_linked_list(head)
print("Reversed List:")
print_list(reversed_head)