//Using two-pointer approach

#include <iostream>
#include <vector>
using namespace std;

int maxWater(vector<int> &arr) { 
    int left = 1;
    int right = arr.size() - 2;

    // lMax : Maximum in subarray arr[0..left-1]
    // rMax : Maximum in subarray arr[right+1..n-1]
    int lMax = arr[left - 1];
    int rMax = arr[right + 1];

    int res = 0;
    while (left <= right) {
      
        // If rMax is smaller, then we can 
        // decide the amount of water for arr[right]
        if (rMax <= lMax) {
          
            // Add the water for arr[right]
            res += max(0, rMax - arr[right]);

            // Update right max
            rMax = max(rMax, arr[right]);

            // Update right pointer as we have 
            // decided the amount of water for this
            right -= 1;
        } else { 
            // Add the water for arr[left]
            res += max(0, lMax - arr[left]);

            // Update left max
            lMax = max(lMax, arr[left]);

            // Update left pointer as we have 
            // decided water for this
            left += 1;
        }
    }
    return res;
}

int main() {
    vector<int> arr = {2, 1, 5, 3, 1, 0, 4};
    cout << maxWater(arr) << endl;
    return 0;
}