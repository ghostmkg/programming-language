#include<bits/stdc++.h>

using namespace std;

// Function for Left Rotation by one place
vector<int> LeftRotation(vector<int>&v, int size){
    int temp;
    temp = v[0];
    for(int i=0;i<=size-1;i++){
        v[i] = v[i+1];
    }
    v[size-1] = temp;
    return v;
}

int main(){
    int size,input;
    vector<int>v;
    cout << "Enter the size:" << endl;
    cin >> size;
    cout << "Enter the elements: " << endl;
    for(int i=0;i<size;i++){
        cin >> input; //You can't take i of for loop for input as there value effect the loop
        v.push_back(input);
    }
    LeftRotation(v,size);
    cout << "Your Output:" << endl;
    for(int i=0;i<size;i++){
        cout << v[i] << " ";
    }
    return 0;
}
