#include <bits/stdc++.h>
using namespace std;

// Cyclic Sort: works only for arrays containing numbers 1..N (no duplicates)
void cyclicSort(vector<int> &arr) {
    int i = 0;
    int n = arr.size();

    while (i < n) {
        int correctIndex = arr[i] - 1;  // correct position for arr[i]
        if (arr[i] != arr[correctIndex]) {
            swap(arr[i], arr[correctIndex]);
        } else {
            i++;
        }
    }
}

int main() {
    vector<int> arr = {3, 5, 2, 1, 4};

    cout << "Original array:\n";
    for (int x : arr) cout << x << " ";
    cout << "\n";

    cyclicSort(arr);

    cout << "Sorted array:\n";
    for (int x : arr) cout << x << " ";
    cout << "\n";

    return 0;
}
