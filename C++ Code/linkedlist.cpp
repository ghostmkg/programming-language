#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node *next;
};

class List {
    Node *listptr, *temp;
public:
    List() {
        listptr = NULL;
        temp = NULL;
    }

    void create();
    void display();
    void insert_start();
    void insert_end();
    void insert_intermediate();
    void insert_after_element();
    void delete_start();
    void delete_end();
    void delete_intermediate();
    void delete_after_element();
    void reverse();
    void concat(List l2);
    void merge(List l2);
};

void List::create() {
    int x, n;
    cout << "Enter how many nodes : ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Enter value for node " << i << " : ";
        cin >> x;
        Node *newNode = new Node;
        newNode->data = x;
        newNode->next = NULL;
        if (listptr == NULL) {
            listptr = newNode;
            temp = newNode;
        } else {
            temp->next = newNode;
            temp = newNode;
        }
    }
}

void List::display() {
    temp = listptr;
    while (temp != NULL) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

void List::insert_start() {
    Node *newnode = new Node;
    int x;
    cout << "Enter the value to insert at start: ";
    cin >> x;
    newnode->data = x;
    newnode->next = listptr;
    listptr = newnode;
}

void List::insert_end() {
    int x;
    Node *newnode = new Node;
    cout << "Enter value: ";
    cin >> x;
    newnode->data = x;
    newnode->next = NULL;
    if (listptr == NULL) {
        listptr = newnode;
        return;
    }
    temp = listptr;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newnode;
}

void List::insert_intermediate() {
    int pos, x;
    Node *newnode = new Node;
    cout << "Enter position: ";
    cin >> pos;
    cout << "Enter value: ";
    cin >> x;
    newnode->data = x;            //1 -> 2 -> 3 -> 4 -> NULL
    temp = listptr;
    for (int i = 1; i < pos - 1; i++) {
        temp = temp->next;
    }
    newnode->next = temp->next;
    temp->next = newnode;
}

void List::insert_after_element() {
    int key, x;
    cout << "Enter element after which to insert: ";
    cin >> key;
    cout << "Enter value: ";
    cin >> x;
    Node *newnode = new Node;
    newnode->data = x;
    temp = listptr;
    while (temp != NULL && temp->data != key) {
        temp = temp->next;
    }
    if (temp != NULL) {
        newnode->next = temp->next;
        temp->next = newnode;
    }
}

void List::delete_start() {
    temp = listptr;
    listptr = listptr->next;
    delete(temp);
}

void List::delete_end() {
    temp = listptr;
    while (temp->next->next != NULL) {
        temp = temp->next;
    }
    delete(temp->next);
    temp->next = NULL;
}

void List::delete_intermediate() {
    int pos, i = 0;
    Node *q;
    temp = listptr;
    cout << "Enter position: ";
    cin >> pos;
    while (i < pos - 1) {
        temp = temp->next;
        i++;
    }
    q = temp->next;
    temp->next = q->next;
    delete(q);
}

void List::delete_after_element() {
    int key;
    Node *q;
    cout << "Enter element after which to delete: ";
    cin >> key;
    temp = listptr;
    while (temp != NULL && temp->data != key) {
        temp = temp->next;
    }
    if (temp != NULL && temp->next != NULL) {
        q = temp->next;
        temp->next = q->next;
        delete(q);
    }
}

void List::reverse() {
    Node *prev = NULL, *curr = listptr, *next = NULL;
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    listptr = prev;
}

void List::concat(List l2) {
    if (listptr == NULL) {
        listptr = l2.listptr;
        return;
    }
    temp = listptr;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = l2.listptr;
}

void List::merge(List l2) {
    // You can implement sorted merge if needed
}

int main() {
    int p = 1, ch;
    List l1, l2;
    while (p == 1) {
        cout << "\nEnter Choice:\n";
        cout << "1) Create\n";
        cout << "2) Display\n";
        cout << "3) Insert at Start\n";
        cout << "4) Insert at End\n";
        cout << "5) Insert at Intermediate\n";
        cout << "6) Insert after Element\n";
        cout << "7) Delete Start\n";
        cout << "8) Delete End\n";
        cout << "9) Delete Intermediate\n";
        cout << "10) Delete after Element\n";
        cout << "11) Reverse\n";
        cout << "12) Concat\n";
        cout << "13) Merge\n";
        cout << "Enter your choice: ";
        cin >> ch;

        switch (ch) {
            case 1: l1.create(); break;
            case 2: l1.display(); break;
            case 3: l1.insert_start(); l1.display(); break;
            case 4: l1.insert_end(); l1.display(); break;
            case 5: l1.insert_intermediate(); l1.display(); break;
            case 6: l1.insert_after_element(); l1.display(); break;
            case 7: l1.delete_start(); l1.display(); break;
            case 8: l1.delete_end(); l1.display(); break;
            case 9: l1.delete_intermediate(); l1.display(); break;
            case 10: l1.delete_after_element(); l1.display(); break;
            case 11: l1.reverse(); l1.display(); break;
            case 12: l2.create(); l1.concat(l2); l1.display(); break;
            case 13: l2.create(); l1.merge(l2); l1.display(); break;
            default: cout << "Invalid choice!\n";
        }
        cout << "\nPress 1 to continue: ";
        cin >> p;
    }
    return 0;
}
