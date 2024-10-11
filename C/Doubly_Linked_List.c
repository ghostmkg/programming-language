#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
} Node;

Node* head = NULL;  

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}

// Function to add a node at the beginning
void addNodeAtBeginning(int data) {
    Node* newNode = createNode(data);
    newNode->next = head;
    if (head != NULL) {
        head->prev = newNode;
    }
    head = newNode;
}

// Function to add a node at the end
void addNodeAtEnd(int data) {
    Node* newNode = createNode(data);
    if (head == NULL) {
        head = newNode;
        return;
    }
    Node* temp = head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
    newNode->prev = temp;
}

// Function to add a node at a specific position
void addNodeAtPosition(int data, int position) {
    if (position == 0) {
        addNodeAtBeginning(data);
        return;
    }
    
    Node* newNode = createNode(data);
    Node* temp = head;
    for (int i = 0; temp != NULL && i < position - 1; i++) {
        temp = temp->next;
    }
    
    if (temp == NULL) {
        printf("Position out of bounds.\n");
        free(newNode);
        return;
    }
    
    newNode->next = temp->next;
    newNode->prev = temp;
    if (temp->next != NULL) {
        temp->next->prev = newNode;
    }
    temp->next = newNode;
}

// Function to display the list
void displayList() {
    Node* temp = head;
    if (temp == NULL) {
        printf("List is empty.\n");
        return;
    }
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

// Main function for the CLI
int main() {
    int choice, data, position;

    while (1) {
        printf("1. Add Node at Beginning\n");
        printf("2. Add Node at End\n");
        printf("3. Add Node at Position\n");
        printf("4. Display List\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter data for the new node: ");
                scanf("%d", &data);
                addNodeAtBeginning(data);
                break;

            case 2:
                printf("Enter data for the new node: ");
                scanf("%d", &data);
                addNodeAtEnd(data);
                break;

            case 3:
                printf("Enter data for the new node: ");
                scanf("%d", &data);
                printf("Enter position to add the node: ");
                scanf("%d", &position);
                addNodeAtPosition(data, position);
                break;

            case 4:
                displayList();
                break;

            case 5:
                printf("Exiting program.\n");
                // Free the list before exiting (optional)
                while (head != NULL) {
                    Node* temp = head;
                    head = head->next;
                    free(temp);
                }
                exit(0);

            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}
