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

    def is_palindrome(self):
        if not self.head or not self.head.next:
            return True

        
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        
        first_half, second_half = self.head, prev
        while second_half:
            if first_half.value != second_half.value:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    def display(self):
        """Prints the linked list."""
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    ll = LinkedList()
    elements = [1, 2, 3, 2, 1]

    
    for element in elements:
        ll.insert(element)

    print("Linked List:")
    ll.display()

    
    if ll.is_palindrome():
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")
