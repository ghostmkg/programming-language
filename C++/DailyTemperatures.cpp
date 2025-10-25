#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> st;
        int n = temperatures.size();
        vector<int> answer(n, 0);

        // Traverse from the end
        for (int i = n - 1; i >= 0; i--) {
            // Pop all indices with temperatures <= current
            while (!st.empty() && temperatures[st.top()] <= temperatures[i]) {
                st.pop();
            }

            // If stack not empty, next warmer day exists
            if (!st.empty())
                answer[i] = st.top() - i;

            // Push current index
            st.push(i);
        }

        return answer;
    }
};

int main() {
    Solution sol;
    vector<int> temperatures = {73, 74, 75, 71, 69, 72, 76, 73};

    vector<int> result = sol.dailyTemperatures(temperatures);

    cout << "Temperatures: ";
    for (int t : temperatures) cout << t << " ";
    cout << endl;

    cout << "Days until warmer temperature: ";
    for (int r : result) cout << r << " ";
    cout << endl;

    return 0;
}
