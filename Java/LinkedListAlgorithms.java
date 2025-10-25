/**
 * Comprehensive Linked List Implementation in Java
 * =================================================
 * 
 * Singly and Doubly Linked List with all common operations
 * including reversal, cycle detection, and merging.
 * 
 * @author Hacktoberfest 2025 Contributor
 */

package algorithms.datastructures;

public class LinkedListAlgorithms {
    
    // Node for Singly Linked List
    static class Node {
        int data;
        Node next;
        
        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }
    
    // Singly Linked List
    static class SinglyLinkedList {
        Node head;
        
        /**
         * Insert at beginning - O(1)
         */
        public void insertAtBeginning(int data) {
            Node newNode = new Node(data);
            newNode.next = head;
            head = newNode;
        }
        
        /**
         * Insert at end - O(n)
         */
        public void insertAtEnd(int data) {
            Node newNode = new Node(data);
            
            if (head == null) {
                head = newNode;
                return;
            }
            
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
        
        /**
         * Delete node with given value - O(n)
         */
        public void delete(int data) {
            if (head == null) return;
            
            if (head.data == data) {
                head = head.next;
                return;
            }
            
            Node current = head;
            while (current.next != null && current.next.data != data) {
                current = current.next;
            }
            
            if (current.next != null) {
                current.next = current.next.next;
            }
        }
        
        /**
         * Reverse the linked list - O(n)
         */
        public void reverse() {
            Node prev = null;
            Node current = head;
            Node next;
            
            while (current != null) {
                next = current.next;
                current.next = prev;
                prev = current;
                current = next;
            }
            
            head = prev;
        }
        
        /**
         * Find middle element using slow-fast pointer - O(n)
         */
        public Node findMiddle() {
            if (head == null) return null;
            
            Node slow = head;
            Node fast = head;
            
            while (fast != null && fast.next != null) {
                slow = slow.next;
                fast = fast.next.next;
            }
            
            return slow;
        }
        
        /**
         * Detect cycle using Floyd's algorithm - O(n)
         */
        public boolean hasCycle() {
            if (head == null) return false;
            
            Node slow = head;
            Node fast = head;
            
            while (fast != null && fast.next != null) {
                slow = slow.next;
                fast = fast.next.next;
                
                if (slow == fast) return true;
            }
            
            return false;
        }
        
        /**
         * Find nth node from end - O(n)
         */
        public Node findNthFromEnd(int n) {
            if (head == null) return null;
            
            Node first = head;
            Node second = head;
            
            // Move first pointer n steps ahead
            for (int i = 0; i < n; i++) {
                if (first == null) return null;
                first = first.next;
            }
            
            // Move both pointers until first reaches end
            while (first != null) {
                first = first.next;
                second = second.next;
            }
            
            return second;
        }
        
        /**
         * Remove duplicates from sorted list - O(n)
         */
        public void removeDuplicates() {
            if (head == null) return;
            
            Node current = head;
            
            while (current != null && current.next != null) {
                if (current.data == current.next.data) {
                    current.next = current.next.next;
                } else {
                    current = current.next;
                }
            }
        }
        
        /**
         * Check if list is palindrome - O(n)
         */
        public boolean isPalindrome() {
            if (head == null || head.next == null) return true;
            
            // Find middle
            Node slow = head;
            Node fast = head;
            
            while (fast.next != null && fast.next.next != null) {
                slow = slow.next;
                fast = fast.next.next;
            }
            
            // Reverse second half
            Node secondHalf = reverseList(slow.next);
            Node firstHalf = head;
            
            // Compare both halves
            while (secondHalf != null) {
                if (firstHalf.data != secondHalf.data) return false;
                firstHalf = firstHalf.next;
                secondHalf = secondHalf.next;
            }
            
            return true;
        }
        
        private Node reverseList(Node head) {
            Node prev = null;
            Node current = head;
            
            while (current != null) {
                Node next = current.next;
                current.next = prev;
                prev = current;
                current = next;
            }
            
            return prev;
        }
        
        /**
         * Print list - O(n)
         */
        public void print() {
            Node current = head;
            while (current != null) {
                System.out.print(current.data + " -> ");
                current = current.next;
            }
            System.out.println("null");
        }
        
        /**
         * Get length - O(n)
         */
        public int length() {
            int count = 0;
            Node current = head;
            
            while (current != null) {
                count++;
                current = current.next;
            }
            
            return count;
        }
    }
    
    /**
     * Merge two sorted linked lists - O(n + m)
     */
    public static Node mergeSorted(Node l1, Node l2) {
        Node dummy = new Node(0);
        Node current = dummy;
        
        while (l1 != null && l2 != null) {
            if (l1.data <= l2.data) {
                current.next = l1;
                l1 = l1.next;
            } else {
                current.next = l2;
                l2 = l2.next;
            }
            current = current.next;
        }
        
        current.next = (l1 != null) ? l1 : l2;
        
        return dummy.next;
    }
    
    /**
     * Find intersection point of two lists - O(n + m)
     */
    public static Node findIntersection(Node head1, Node head2) {
        if (head1 == null || head2 == null) return null;
        
        Node ptr1 = head1;
        Node ptr2 = head2;
        
        while (ptr1 != ptr2) {
            ptr1 = (ptr1 == null) ? head2 : ptr1.next;
            ptr2 = (ptr2 == null) ? head1 : ptr2.next;
        }
        
        return ptr1;
    }
    
    /**
     * Demonstration of all linked list operations
     */
    public static void demonstrate() {
        System.out.println("=".repeat(70));
        System.out.println("LINKED LIST ALGORITHMS DEMONSTRATION");
        System.out.println("=".repeat(70));
        
        SinglyLinkedList list = new SinglyLinkedList();
        
        // Insert operations
        System.out.println("\n1. INSERTION");
        list.insertAtEnd(1);
        list.insertAtEnd(2);
        list.insertAtEnd(3);
        list.insertAtEnd(4);
        list.insertAtEnd(5);
        System.out.print("   List: ");
        list.print();
        
        // Find middle
        System.out.println("\n2. FIND MIDDLE");
        Node middle = list.findMiddle();
        System.out.println("   Middle element: " + (middle != null ? middle.data : "null"));
        
        // Reverse
        System.out.println("\n3. REVERSE LIST");
        list.reverse();
        System.out.print("   Reversed: ");
        list.print();
        
        // Nth from end
        System.out.println("\n4. NTH FROM END");
        Node nth = list.findNthFromEnd(2);
        System.out.println("   2nd from end: " + (nth != null ? nth.data : "null"));
        
        // Length
        System.out.println("\n5. LENGTH");
        System.out.println("   Length: " + list.length());
        
        // Palindrome check
        System.out.println("\n6. PALINDROME CHECK");
        SinglyLinkedList palindrome = new SinglyLinkedList();
        palindrome.insertAtEnd(1);
        palindrome.insertAtEnd(2);
        palindrome.insertAtEnd(3);
        palindrome.insertAtEnd(2);
        palindrome.insertAtEnd(1);
        System.out.print("   List: ");
        palindrome.print();
        System.out.println("   Is Palindrome: " + palindrome.isPalindrome());
        
        // Remove duplicates
        System.out.println("\n7. REMOVE DUPLICATES");
        SinglyLinkedList duplicates = new SinglyLinkedList();
        duplicates.insertAtEnd(1);
        duplicates.insertAtEnd(1);
        duplicates.insertAtEnd(2);
        duplicates.insertAtEnd(3);
        duplicates.insertAtEnd(3);
        System.out.print("   Before: ");
        duplicates.print();
        duplicates.removeDuplicates();
        System.out.print("   After: ");
        duplicates.print();
        
        System.out.println("\n" + "=".repeat(70));
    }
    
    public static void main(String[] args) {
        demonstrate();
    }
}
