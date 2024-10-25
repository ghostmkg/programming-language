//{ Driver Code Starts
#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>
#include <cstdio>
#include <ios>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct Node {
    int data;
    struct Node *next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};


// } Driver Code Ends
/*
struct Node {
  int data;
  struct Node *next;
  Node(int x) {
    data = x;
    next = NULL;
  }
};
*/

class Solution {
  public:
    // Function to check whether the list is palindrome.
    bool isPalindrome(Node *head) {
        // Your code here
         if(head->next==NULL) return 1;
        if(head->next->next==NULL && head->data==head->next->data) return 1;
        if(head->next->next==NULL && head->data!=head->next->data) return 0;
        
        
        Node *fast=head;
        Node*curr=head;
        Node *fr=head->next;
        Node *prev=NULL;
        
        
        while(fast!=NULL && fast->next!=NULL)
        {
            fast=fast->next->next;
            curr->next=prev;
            prev=curr;
            curr=fr;
            fr=fr->next;
        }
        // prev=fr;  
        if(fast!=NULL)
         curr=fr;
         
         
        while(prev!=NULL)
        {
            if(prev->data!=curr->data)
            return 0;
            
            prev=prev->next;
            curr=curr->next;
            
        }
       
        
        return 1;
    }
};


//{ Driver Code Starts.

/* Function to print nodes in a given linked list */
void printList(struct Node *head) {
    struct Node *temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        if (arr.empty()) {
            cout << "empty" << endl;
            continue;
        }

        struct Node *head = new Node(arr[0]);
        struct Node *tail = head;
        for (int i = 1; i < arr.size(); ++i) {
            tail->next = new Node(arr[i]);
            tail = tail->next;
        }
        Solution ob;
        if (ob.isPalindrome(head))
            cout << "true" << endl;
        else
            cout << "false" << endl;

        // Clean up the remaining nodes to avoid memory leaks
        while (head != NULL) {
            struct Node *temp = head;
            head = head->next;
            delete temp;
        }
    }
    return 0;
}

// } Driver Code Ends
