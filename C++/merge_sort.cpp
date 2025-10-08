#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

class MergeSort {
private:
    std::vector<int> arr;

    void merge(size_t left, size_t mid, size_t right) {
        size_t n1 = mid - left + 1;
        size_t n2 = right - mid;

        // Create temporary arrays
        std::vector<int> L(n1), R(n2);

        // Copy data to temporary arrays
        for(size_t i = 0; i < n1; i++)
            L[i] = arr[left + i];
        for(size_t j = 0; j < n2; j++)
            R[j] = arr[mid + 1 + j];

        // Merge the temporary arrays back
        size_t i = 0, j = 0, k = left;
        while(i < n1 && j < n2) {
            if(L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        // Copy remaining elements of L[] if any
        while(i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        // Copy remaining elements of R[] if any
        while(j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    void mergeSortHelper(size_t left, size_t right) {
        if(left < right) {
            size_t mid = left + (right - left) / 2;
            
            // Sort first and second halves
            mergeSortHelper(left, mid);
            mergeSortHelper(mid + 1, right);

            // Merge the sorted halves
            merge(left, mid, right);
        }
    }

public:
    // Constructor to initialize with random values
    MergeSort(size_t size) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(1, 1000);

        arr.reserve(size);
        for(size_t i = 0; i < size; ++i) {
            arr.push_back(dis(gen));
        }
    }

    // Public method to start merge sort
    void sort() {
        if(arr.size() <= 1) return;
        mergeSortHelper(0, arr.size() - 1);
    }

    // Display array content
    void displayArray(const std::string& message = "") const {
        std::cout << message;
        for(const auto& num : arr) {
            std::cout << num << " ";
        }
        std::cout << "\n";
    }

    // Verify if array is sorted
    bool isSorted() const {
        return std::is_sorted(arr.begin(), arr.end());
    }
};

int main() {
    const size_t ARRAY_SIZE = 15;
    MergeSort sorter(ARRAY_SIZE);

    // Display original array
    sorter.displayArray("Original array: ");

    // Perform merge sort
    sorter.sort();

    // Display sorted array
    sorter.displayArray("Sorted array:   ");

    // Verify sorting
    std::cout << "\nArray is " << (sorter.isSorted() ? "correctly" : "not")
              << " sorted!" << std::endl;

    return 0;
}