#include <iostream>
#include <stack>
#include <vector>
using namespace std;

class StockSpanner {
public:
    stack<pair<int, int>> st; // {price, span}

    StockSpanner() {
        // constructor
    }

    int next(int price) {
        int span = 1;

        // Pop all smaller or equal prices and add their spans
        while (!st.empty() && st.top().first <= price) {
            span += st.top().second;
            st.pop();
        }

        // Push current price and its total span
        st.push({price, span});
        return span;
    }
};

int main() {
    StockSpanner ss;

    vector<int> prices = {100, 80, 60, 70, 60, 75, 85};

    cout << "Stock Prices: ";
    for (int p : prices) cout << p << " ";
    cout << "\nSpans: ";

    for (int p : prices) {
        cout << ss.next(p) << " ";
    }
    cout << endl;

    return 0;
}
