#include <vector>
#include <iostream>
using namespace std;

vector<int> twoSum(vector<int>& numbers, int target) {
    int left = 0;
    int right = numbers.size() - 1;

    while (left < right) {
        int sum = numbers[left] + numbers[right];
        if (sum == target) {
            return {left + 1, right + 1}; // 1-indexed
        } else if (sum < target) {
            left++; // need a bigger sum
        } else {
            right--; // need a smaller sum
        }
    }

    return {}; // just in case, though problem guarantees a solution
}

int main() {
    vector<int> numbers = {2,7,11,15};
    int target = 9;
    vector<int> result = twoSum(numbers, target);

    cout << "[" << result[0] << "," << result[1] << "]" << endl;
    return 0;
}
