#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string minRemoveToMakeValid(string s) {
        int n = s.size();
        stack<int> st;

        // Traverse string and mark invalid ')'
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                st.push(i);
            } else if (s[i] == ')') {
                if (!st.empty()) {
                    st.pop();
                } else {
                    // mark invalid ')'
                    s[i] = '#';
                }
            }
        }

        // Mark remaining unmatched '('
        while (!st.empty()) {
            s[st.top()] = '#';
            st.pop();
        }

        // Build result string without '#'
        string res = "";
        for (char ch : s) {
            if (ch != '#')
                res += ch;
        }
        return res;
    }
};

int main() {
    Solution sol;
    string s;

    cout << "Enter a string with parentheses: ";
    getline(cin, s);

    string result = sol.minRemoveToMakeValid(s);
    cout << "Valid string: " << result << endl;

    return 0;
}
