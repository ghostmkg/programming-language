class Solution {
public:
    int maximumSwap(int num) {
        string s = to_string(num);
        int n = s.size();
        vector<int> v(10, -1);
        for (int i = 0; i < n; i++) {
            int ind = s[i] - '0';
            v[ind] = i;
        }
        for (int i = 0; i < n; i++) {
            int dig = s[i] - '0';
            for (int j = 9; j > dig; j--) {
                if (v[j] > i) {
                    swap(s[i], s[v[j]]);
                    return stoi(s);
                }
            }
        }
        return num;
    }
};
