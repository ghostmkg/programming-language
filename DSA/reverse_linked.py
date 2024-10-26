class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  
            current.next = prev       
            prev = current            
            current = next_node       
        self.head = prev              

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()


if __name__ == "__main__":
    ll = LinkedList()
    elements = [1, 2, 3, 4, 5]

    
    for element in elements:
        ll.insert(element)

    print("Original Linked List:")
    ll.display()

    
    ll.reverse()

    print("Reversed Linked List:")
    ll.display()
