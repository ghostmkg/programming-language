#include <iostream>
#include <stack>
using namespace std;

class MyQueue {
public:
    stack<int> s1;
    stack<int> s2;

    MyQueue() {
        // constructor (no initialization needed)
    }

    void push(int x) {
        // Move all elements from s1 to s2
        while (!s1.empty()) {
            s2.push(s1.top());
            s1.pop();
        }

        // Push new element onto s1
        s1.push(x);

        // Move all elements back from s2 to s1
        while (!s2.empty()) {
            s1.push(s2.top());
            s2.pop();
        }
    }

    int pop() {
        if (s1.empty()) {
            cout << "Queue is empty! Cannot pop.\n";
            return -1;
        }
        int ans = s1.top();
        s1.pop();
        return ans;
    }

    int peek() {
        if (s1.empty()) {
            cout << "Queue is empty!\n";
            return -1;
        }
        return s1.top();
    }

    bool empty() {
        return s1.empty();
    }
};

int main() {
    MyQueue q;

    cout << "Pushing elements: 10, 20, 30\n";
    q.push(10);
    q.push(20);
    q.push(30);

    cout << "Front element: " << q.peek() << endl; // Should print 10
    cout << "Popping element: " << q.pop() << endl; // Should remove 10
    cout << "Front element now: " << q.peek() << endl; // Should print 20

    cout << "Popping all remaining elements:\n";
    while (!q.empty()) {
        cout << q.pop() << " ";
    }
    cout << endl;

    cout << "Queue empty? " << (q.empty() ? "Yes" : "No") << endl;

    return 0;
}
