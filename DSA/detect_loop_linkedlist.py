class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def create_loop(self, position):
        """Creates a loop in the linked list by connecting the last node to the node at the given position (0-based index)."""
        if position < 0:
            return
        loop_start = self.head
        last_node = self.head
        count = 0

        while last_node.next:
            last_node = last_node.next
        while count < position:
            loop_start = loop_start.next
            count += 1

        last_node.next = loop_start

    def detect_loop(self):
        """Detects if a loop is present in the linked list."""
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  
                return True

        return False

    def display(self):
        """Prints the linked list (useful for visual verification without a loop)."""
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    ll = LinkedList()
    elements = [1, 2, 3, 4, 5]

    
    for element in elements:
        ll.insert(element)

    print("Linked List before creating a loop:")
    ll.display()

    
    ll.create_loop(1)

    
    if ll.detect_loop():
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")
