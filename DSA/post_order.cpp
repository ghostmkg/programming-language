                            
#include <iostream>
#include <vector>

using namespace std;

// Node structure for the binary tree
struct Node {
    int data;
    Node* left;
    Node* right;
    // Constructor to initialize
    // the node with a value
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

// Function to perform postorder
// traversal recursively
void postorder(Node* root, vector<int>& arr){
    // Base case: if root is null, return
    if(root==NULL){
        return;
    }
    // Traverse left subtree
    postorder(root->left, arr);
    // Traverse right subtree
    postorder(root->right, arr);
    // Visit the node
    // (append node's data to the array)
    arr.push_back(root->data);
}

// Function to get the postorder
// traversal of a binary tree
vector<int> postOrder(Node* root){
    // Create a vector to
    // store the traversal result
    vector<int> arr;
    // Perform postorder traversal
    // starting from the root
    postorder(root, arr);
    // Return the postorder
    // traversal result
    return arr;
}

// Function to print the
// elements of a vector
void printVector(const vector<int>& vec) {
    // Iterate through the vector
    // and print each element
    for (int num : vec) {
        cout << num << " ";
    }
    cout << endl;
}

// Main function
int main()
{
    // Creating a sample binary tree
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);

    // Getting postorder traversal
    vector<int> result = postOrder(root);

    // Printing the postorder
    // traversal result
    cout << "Postorder traversal: ";
    printVector(result);

    return 0;
}
                            
                        
