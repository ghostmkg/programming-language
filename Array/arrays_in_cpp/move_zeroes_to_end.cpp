#include <iostream>
#include <vector>
using namespace std;

void moveZeros(vector<int>& arr) {
    int nonZeroIndex = 0;
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] != 0)
            swap(arr[i], arr[nonZeroIndex++]);
    }
}

int main() {
    vector<int> arr;
    int n;

    cout<<"\nenter size of the array :\n";
    cin>>n;

    cout<<"\nenter the array elements :\n";
    for(int i=0; i<n; i++){
        int ele;
        cin>>ele;
        arr.push_back(ele);
    }
    
    moveZeros(arr);
    cout << "After moving zeros: ";
    for (int i : arr) cout << i << " ";
    return 0;
}
