#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

Node* insertAtBeginning(Node* head, int data) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->data = data;

    if (head == NULL) {
        newNode->next = newNode; 
        head = newNode;
    } else {
        Node* temp = head;
        while (temp->next != head) {
            temp = temp->next;
        }
        newNode->next = head;
        temp->next = newNode;
        head = newNode; 
    }

    return head;
}

Node* insertAtEnd(Node* head, int data) {
    Node* newNode = (Node*) malloc(sizeof(Node));
    newNode->data = data;

    if (head == NULL) {
        newNode->next = newNode;
        head = newNode;
    } else {
        Node* temp = head;
        while (temp->next != head) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->next = head; 
    }

    return head;
}

Node* deleteNode(Node* head, int key) {
    if (head == NULL) {
        printf("List is empty.\n");
        return NULL;
    }

    Node* curr = head, *prev = NULL;

    if (head->data == key) {
        if (head->next == head) {
            free(head);
            return NULL;
        }
        while (curr->next != head) {
            curr = curr->next;
        }
        curr->next = head->next;
        free(head);
        head = curr->next;
        return head;
    }

    prev = head;
    curr = head->next;
    while (curr != head) {
        if (curr->data == key) {
            prev->next = curr->next;
            free(curr);
            return head;
        }
        prev = curr;
        curr = curr->next;
    }

    printf("Node with data %d not found.\n", key);
    return head;
}

Node* deleteAtBeginning(Node* head) {
    if (head == NULL) {
        printf("List is empty.\n");
        return NULL;
    }

    if (head->next == head) {
        free(head);
        return NULL;
    }

    Node* last = head;
    while (last->next != head) {
        last = last->next;
    }

    Node* temp = head;
    last->next = head->next;
    head = head->next;
    free(temp);

    return head;
}

Node* deleteAtEnd(Node* head) {
    if (head == NULL) {
        printf("List is empty.\n");
        return NULL;
    }

    if (head->next == head) {
        free(head);
        return NULL;
    }

    Node* temp = head;
    Node* prev = NULL;

    while (temp->next != head) {
        prev = temp;
        temp = temp->next;
    }

    prev->next = head; 
    free(temp);        

    return head;
}

void displayList(Node* head) {
    if (head == NULL) {
        printf("The list is empty.\n");
    } else {
        Node* current = head;
        do {
            printf("%d ", current->data);
            current = current->next;
        } while (current != head);
        printf("\n");
    }
}

int main() {
    Node* head = NULL;
    int choice, data;

    while (1) {
        printf("\nCircular Linked List Operations:\n");
        printf("1. Insert at beginning\n");
        printf("2. Insert at end\n");
        printf("3. Delete at beginning\n");
        printf("4. Delete at end\n");
        printf("5. Delete a specific node by key\n");
        printf("6. Display the list\n");
        printf("7. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the data to insert at beginning: ");
                scanf("%d", &data);
                head = insertAtBeginning(head, data);
                break;

            case 2:
                printf("Enter the data to insert at end: ");
                scanf("%d", &data);
                head = insertAtEnd(head, data);
                break;

            case 3:
                head = deleteAtBeginning(head);
                break;

            case 4:
                head = deleteAtEnd(head);
                break;

            case 5:
                printf("Enter the data of the node to delete: ");
                scanf("%d", &data);
                head = deleteNode(head, data);
                break;

            case 6:
                printf("Current List: ");
                displayList(head);
                break;

            case 7:
                exit(0);

            default:
                printf("Invalid choice. Please enter a valid option.\n");
        }
    }

    return 0;
}
