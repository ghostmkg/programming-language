#include <iostream>

using namespace std;

// Node structure for the linked list
struct Node {
    int data;
    Node* next;
};

// Function to create a new node
Node* newNode(int data) {
    Node* temp = new Node();
    temp->data = data;
    temp->next = nullptr;
    return temp;
}

// Function to detect cycle using Floyd's Tortoise and Hare algorithm
bool detectCycle(Node* head) {
    if (head == nullptr)
        return false;

    Node* slow = head; // Tortoise moves 1 step at a time
    Node* fast = head; // Hare moves 2 steps at a time

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;           // Move slow pointer by 1
        fast = fast->next->next;     // Move fast pointer by 2

        if (slow == fast) {          // Cycle detected
            return true;
        }
    }

    // No cycle
    return false;
}

int main() {
    // Creating nodes
    Node* head = newNode(1);
    head->next = newNode(2);
    head->next->next = newNode(3);
    head->next->next->next = newNode(4);
    head->next->next->next->next = newNode(5);

    // Creating a cycle for testing: last node points to the second node
    head->next->next->next->next->next = head->next;

    if (detectCycle(head))
        cout << "Cycle detected in the linked list.\n";
    else
        cout << "No cycle detected.\n";

    return 0;
}
//Final check