#include <iostream>
#include <list>
using namespace std;

int main()
{

    // Create a doubly linked list using STL
    list<int> dll;

    // Insert elements at the end
    dll.push_back(10);
    dll.push_back(20);

    // Insert element at the beginning
    dll.push_front(5);

    // Insert element at a specific position (after first element)
    auto it = dll.begin();
    ++it; // move iterator to second position
    dll.insert(it, 15);

    // Forward traversal of the list
    cout << "Forward: ";
    for (int val : dll)
        cout << val << " <-> ";
    cout << "NULL" << endl;

    // Backward traversal of the list
    cout << "Backward: ";
    for (auto rit = dll.rbegin(); rit != dll.rend(); ++rit)
        cout << *rit << " <-> ";
    cout << "NULL" << endl;

    // Remove element from the beginning
    dll.pop_front();

    // Remove element from the end
    dll.pop_back();

    // Forward traversal after deletions
    cout << "After deletion: ";
    for (int val : dll)
        cout << val << " <-> ";
    cout << "NULL" << endl;

    return 0;
}