#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 0; i < nums.size(); i++) {
            ans = ans ^ nums[i];  // XOR cancels out duplicates
        }
        return ans;
    }
};

int main() {
    Solution sol;

    // Example input where every number appears twice except one
    vector<int> nums = {4, 1, 2, 1, 2};

    int result = sol.singleNumber(nums);
    cout << "The single number is: " << result << endl;

    // Another test case
    vector<int> nums2 = {2, 2, 3};
    cout << "The single number is: " << sol.singleNumber(nums2) << endl;

    return 0;
}
