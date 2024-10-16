class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        priority_queue<pair<int, char>> pq;
        if (a > 0)
            pq.push({a, 'a'});
        if (b > 0)
            pq.push({b, 'b'});
        if (c > 0)
            pq.push({c, 'c'});

        string s;
        while (!pq.empty()) {
            int curmax = pq.top().first;
            char curchar = pq.top().second;
            pq.pop();
            if (s.length() >= 2 && s[s.length() - 2] == curchar &&
                s[s.length() - 1] == curchar) {
                if (pq.empty())
                    break;
                int nextmax = pq.top().first;
                char nextchar = pq.top().second;
                pq.pop();
                s.push_back(nextchar);
                nextmax--;
                if (nextmax > 0) {
                    pq.push({nextmax, nextchar});
                }
            } else {
                s.push_back(curchar);
                curmax--;
            }
            if (curmax > 0) {
                pq.push({curmax, curchar});
            }
        }
        return s;
    }
};
