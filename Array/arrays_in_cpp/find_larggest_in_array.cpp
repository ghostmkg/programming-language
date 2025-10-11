#include <iostream>
#include <vector>
using namespace std;

int findLargest(const vector<int>& arr) {
    int largest = arr[0];
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] > largest)
            largest = arr[i];
    }
    return largest;
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
    
    cout << "Largest element: " << findLargest(arr);
    return 0;
}
