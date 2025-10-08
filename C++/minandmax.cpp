#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

class MinMaxFinder {
private:
    std::vector<int> arr;

public:
    // Constructor to initialize with random values
    MinMaxFinder(size_t size) {
        // Use modern random number generation
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(1, 1000);

        arr.reserve(size);
        for(size_t i = 0; i < size; ++i) {
            arr.push_back(dis(gen));
        }
    }

    // Method 1: Using STL algorithms
    std::pair<int, int> findMinMaxSTL() const {
        auto [min_it, max_it] = std::minmax_element(arr.begin(), arr.end());
        return {*min_it, *max_it};
    }

    // Method 2: Linear search with single traversal
    std::pair<int, int> findMinMaxLinear() const {
        if (arr.empty()) return {0, 0};
        
        int min = arr[0], max = arr[0];
        for (size_t i = 1; i < arr.size(); i++) {
            if (arr[i] < min) min = arr[i];
            if (arr[i] > max) max = arr[i];
        }
        return {min, max};
    }

    // Method 3: Divide and conquer approach
    std::pair<int, int> findMinMaxDivideConquer(size_t low, size_t high) const {
        // Base cases
        if (low == high) return {arr[low], arr[low]};
        if (high - low == 1) return {std::min(arr[low], arr[high]), 
                                   std::max(arr[low], arr[high])};

        // Divide the array
        size_t mid = (low + high) / 2;
        auto left = findMinMaxDivideConquer(low, mid);
        auto right = findMinMaxDivideConquer(mid + 1, high);

        // Combine results
        return {std::min(left.first, right.first), 
                std::max(left.second, right.second)};
    }

    // Display array content
    void displayArray() const {
        std::cout << "Array content: ";
        for (const auto& num : arr) {
            std::cout << num << " ";
        }
        std::cout << "\n\n";
    }
};

int main() {
    const size_t ARRAY_SIZE = 15;
    MinMaxFinder finder(ARRAY_SIZE);
    
    // Display the array
    finder.displayArray();

    // Test all methods
    auto [stl_min, stl_max] = finder.findMinMaxSTL();
    std::cout << "STL Method - Min: " << stl_min << ", Max: " << stl_max << '\n';

    auto [linear_min, linear_max] = finder.findMinMaxLinear();
    std::cout << "Linear Search - Min: " << linear_min << ", Max: " << linear_max << '\n';

    auto [dc_min, dc_max] = finder.findMinMaxDivideConquer(0, ARRAY_SIZE - 1);
    std::cout << "Divide & Conquer - Min: " << dc_min << ", Max: " << dc_max << '\n';

    return 0;
}