#include <iostream>
#include <vector>
using namespace std;

void reverseArray(vector<int>& arr) {
    int start = 0, end = arr.size() - 1;
    while (start < end) {
        swap(arr[start], arr[end]);
        start++;
        end--;
    }
}

int main() {
    vector<int> arr;
    int n;

    cout<<"\nenter the size of the array :\n";
    cin>>n;

    cout<<"n\enter the array elements :\n";
    for(int i=0; i<n; i++){
        int ele;
        cin>>ele;
        arr.push_back(ele);
    }
    
    reverseArray(arr);
    cout << "Reversed array: ";
    for (int i : arr) cout << i << " ";
    return 0;
}
