#include <iostream>
#include <vector>
using namespace std;

int findMissing(const vector<int>& arr, int n) {
    int total = n * (n + 1) / 2;
    int sum = 0;
    for (int i : arr) sum += i;
    return total - sum;
}

int main() {
    vector<int> arr;
    int arrsize;

    cout<<"\nenter array size:\n";
    cin>>arrsize;

    cout<<"\nenter array elements:\n";
    for(int i=0; i<arrsize; i++){
        int ele;
        cin>>ele;
        arr.push_back(ele);
    }

    cout << "Missing number: " << findMissing(arr, arrsize+1);
    return 0;
}
