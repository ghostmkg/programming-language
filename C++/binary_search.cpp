#include<iostream>
#include<string>
#include<climits>
using namespace std;

int search(vector<int>& nums, int target) {
        int left=0,right=nums.size()-1;
        while (left<=right){
            int mid=(left+right)/2;
            if(mid==target){
                return mid;
            }
            else if (mid>target){
                right=mid-1;
            }
            else{
                left=mid+1;
            }
        }
        return -1;
    }

int main() {
    vector<int> numbers = {2,7,11,15};
    int target = 9;
    int result= search(numbers, target);

    cout<< result<< endl;
    return 0;
}