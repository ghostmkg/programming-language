#include <bits/stdc++.h>
using namespace std;


int minEatingSpeedBrute(vector<int>& piles, int h) {
    int maxp = *max_element(piles.begin(), piles.end());
    for (int k = 1; k <= maxp; ++k) {
        long long t = 0;
        for (int p : piles) {
            t += (p + k - 1) / k;
            if (t > h) break;
        }
        if (t <= h) return k;
    }
    return maxp;
}

int minEatingSpeedOptimal(vector<int>& piles, int H) {
    long long lo = 1, hi = *max_element(piles.begin(), piles.end());
    while (lo < hi) {
        long long mid = lo + (hi - lo) / 2;
        long long hours = 0;
        for (int p : piles) hours += (p + mid - 1) / mid;
        if (hours <= H) hi = mid;
        else lo = mid + 1;
    }
    return (int)lo;
}


int minEatingSpeedOptimalII(vector<int>& piles, int h) {
    auto ok = [&](int k) {
        long long t = 0;
        for (int p : piles) {
            t += (p + k - 1) / k;
            if (t > h) return false;
        }
        return true;
    };
    int l = 1, r = *max_element(piles.begin(), piles.end());
    while (l < r) {
        int m = (l + r) / 2;
        if (ok(m)) r = m;
        else l = m + 1;
    }
    return l;
}

int main() {
    vector<int> piles = {3, 6, 7, 11};
    int h = 8;

    cout << "Brute Force Result: " << minEatingSpeedBrute(piles, h) << endl;
    cout << "Optimal Result: " << minEatingSpeedOptimal(piles, h) << endl;
    cout << "Optimal II Result: " << minEatingSpeedOptimalII(piles, h) << endl;

    return 0;
}
