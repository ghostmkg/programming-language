#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    // Helper function to check if substring is balanced
    bool isBalanced(const vector<int>& freq)
    {
        int count = 0;
        for (int f : freq) {
            if (f > 0) {
                if (count == 0)
                    count = f;
                else if (count != f)
                    return false;
            }
        }
        return true;
    }

    // Main function to find longest balanced substring
    int longestBalanced(string s) {
        int maxLen = 0;
        int n = s.size();

        for (int i = 0; i < n; i++) {
            vector<int> freq(26, 0);  // frequency of letters
            for (int j = i; j < n; j++) {
                freq[s[j] - 'a']++;
                if (isBalanced(freq)) {
                    maxLen = max(maxLen, j - i + 1);
                }
            }
        }

        return maxLen;
    }
};

int main() {
    Solution sol;
    
    string s;
    cout << "Enter a string: ";
    cin >> s;

    int result = sol.longestBalanced(s);
    cout << "Length of the longest balanced substring: " << result << endl;

    // Example test case
    string test = "aabbcc";
    cout << "Example: " << test << " -> " << sol.longestBalanced(test) << endl;

    return 0;
}
