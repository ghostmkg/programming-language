#include<bits/stdc++.h>

using namespace std;

// Brute Force TC->O(N*N) SC->O(N)[to store the answer]
// vector<int>Leader(vector<int>&arr,int size){
//     vector<int>ans;
//     for(int i=0;i<size;i++){
//         bool leader = true;
//         for(int j=i+1;j<size;j++){
//             if(arr[i]<arr[j]){
//                 leader = false;
//                 break;
//             }
//         }
//         if(leader == true){
//             ans.push_back(arr[i]);
//         }
//     }
//     return ans;
// }

// Optimal Solution TC->O(N)+ O(N*log2N)[sorting] SC->O(N)
vector<int>Leader(vector<int>&arr,int size){
    vector<int>ans;
    int maxi = INT_MIN;
    for(int i=size-1;i>=0;i--){
        if(arr[i]>maxi){
            ans.push_back(arr[i]);
        }
        maxi = max(maxi,arr[i]);
    }
    sort(ans.begin(),ans.end());
    return ans;
}


int main(){
    int size;
    cout << "Enter the size of array: "<< endl;
    cin >> size;
    vector<int>arr(size);
    cout << "Enter the elements: "<< endl;
    for(int i=0;i<size;i++){
        cin >> arr[i];
    }
    vector<int>result;
    result = Leader(arr,size);
    cout << "Your Output: "<<endl;
    for(int i=0;i<result.size();i++){
        cout << result[i] << " ";
    }
    return 0;
}
