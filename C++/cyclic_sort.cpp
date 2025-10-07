#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

class CyclicSort {
private:
    std::vector<int> arr;

    void swap(int& a, int& b) {
        int temp = a;
        a = b;
        b = temp;
    }

public:
    // Constructor to initialize with random values from 1 to size
    CyclicSort(size_t size) {
        // Use modern random number generation
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(1, size);

        arr.reserve(size);
        for(size_t i = 0; i < size; ++i) {
            arr.push_back(dis(gen));
        }
    }

    // Cyclic sort implementation
    void sort() {
        int i = 0;
        while (i < arr.size()) {
            // Since array contains numbers from 1 to N
            // correct position for element arr[i] is arr[i] - 1
            int correct_pos = arr[i] - 1;
            
            if (arr[i] != arr[correct_pos]) {
                swap(arr[i], arr[correct_pos]);
            } else {
                i++;
            }
        }
    }

    // Display array content
    void displayArray(const std::string& message = "") const {
        std::cout << message;
        for (const auto& num : arr) {
            std::cout << num << " ";
        }
        std::cout << "\n";
    }

    // Verify if array is sorted
    bool isSorted() const {
        for (size_t i = 1; i < arr.size(); ++i) {
            if (arr[i] < arr[i-1]) return false;
        }
        return true;
    }
};

int main() {
    const size_t ARRAY_SIZE = 10;
    CyclicSort sorter(ARRAY_SIZE);
    
    // Display original array
    sorter.displayArray("Original array: ");
    
    // Perform cyclic sort
    sorter.sort();
    
    // Display sorted array
    sorter.displayArray("Sorted array:   ");
    
    // Verify sorting
    std::cout << "\nArray is " << (sorter.isSorted() ? "correctly" : "not") 
              << " sorted!" << std::endl;

    return 0;
}