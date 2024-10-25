#include<bits/stdc++.h>

using namespace std;

int findMaxConsequtiveOne(vector<int>&nums,int size){
    int cnt = 0;
    int max = 0;
    for(int i=0;i<size;i++){
        if(nums[i]==1){
            cnt++; 
            if(cnt >= max){
                max = cnt;
            }
        }else{
            cnt = 0;
        }
    }
    return max;
}

int main(){
    int size;
    cout << "Enter the size of an array: "<< endl;
    cin >> size;
    vector<int>v(size);
    cout << "Enter the elements: " << endl;
    for(int i=0;i<size;i++){
        cin >> v[i];
    }
    cout << "Your output: " << findMaxConsequtiveOne(v,size);
    return 0; 
}
