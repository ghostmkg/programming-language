public class LinkedListCycle {

    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }
    
    // Function to detect and remove cycle in a linked list
    public static void detectAndRemoveCycle(ListNode head) {
        if (head == null || head.next == null) return;

        ListNode slow = head;
        ListNode fast = head;
        boolean hasCycle = false;

        // Detect cycle using Floyd's Cycle Detection algorithm
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            // Cycle detected
            if (slow == fast) {
                hasCycle = true;
                System.out.println("Cycle Detected");
                break;
            }
        }

        // If there is no cycle, return
        if (!hasCycle){
            System.out.println("No Cycle Detected");
            return;
        }

        // Find the start of the cycle
        slow = head;
        ListNode prev = null;
        while (slow != fast) {
            prev = fast;
            slow = slow.next;
            fast = fast.next;
        }

        // Remove the cycle by setting the `next` of the last node to `null`
        prev.next = null;
        System.out.println("Cycle removed");
    }

    // Helper function to print the linked list
    public static void printList(ListNode head) {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        // Creating a linked list with a cycle
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);
        head.next.next.next.next.next = head.next; // Creates a cycle

        detectAndRemoveCycle(head);
        printList(head); // Should print the list without a cycle
    }
}
