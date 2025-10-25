/**
 * Bit Manipulation Algorithms in C++
 * ===================================
 * 
 * Advanced bit manipulation techniques and algorithms
 * for efficient computations and problem solving.
 * 
 * Author: Hacktoberfest 2025 Contributor
 */

#include <iostream>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>

using namespace std;

class BitManipulation {
public:
    /**
     * Check if number is power of 2
     * Time: O(1)
     */
    static bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
    
    /**
     * Count number of set bits (1s)
     * Time: O(log n)
     */
    static int countSetBits(int n) {
        int count = 0;
        while (n) {
            n &= (n - 1);  // Clear rightmost set bit
            count++;
        }
        return count;
    }
    
    /**
     * Get ith bit (0-indexed from right)
     * Time: O(1)
     */
    static bool getBit(int n, int i) {
        return (n & (1 << i)) != 0;
    }
    
    /**
     * Set ith bit to 1
     * Time: O(1)
     */
    static int setBit(int n, int i) {
        return n | (1 << i);
    }
    
    /**
     * Clear ith bit (set to 0)
     * Time: O(1)
     */
    static int clearBit(int n, int i) {
        return n & ~(1 << i);
    }
    
    /**
     * Toggle ith bit
     * Time: O(1)
     */
    static int toggleBit(int n, int i) {
        return n ^ (1 << i);
    }
    
    /**
     * Find XOR of all numbers from 1 to n
     * Time: O(1)
     */
    static int xorFrom1ToN(int n) {
        switch (n % 4) {
            case 0: return n;
            case 1: return 1;
            case 2: return n + 1;
            case 3: return 0;
        }
        return 0;
    }
    
    /**
     * Find missing number in array [0, n]
     * Time: O(n), Space: O(1)
     */
    static int findMissing(const vector<int>& arr) {
        int xorAll = 0;
        int n = arr.size();
        
        // XOR all array elements
        for (int num : arr) {
            xorAll ^= num;
        }
        
        // XOR with all numbers from 0 to n
        for (int i = 0; i <= n; i++) {
            xorAll ^= i;
        }
        
        return xorAll;
    }
    
    /**
     * Find two non-repeating elements
     * All others appear twice
     * Time: O(n), Space: O(1)
     */
    static pair<int, int> findTwoNonRepeating(const vector<int>& arr) {
        int xorAll = 0;
        
        // Get XOR of two non-repeating numbers
        for (int num : arr) {
            xorAll ^= num;
        }
        
        // Find rightmost set bit
        int rightmostBit = xorAll & -xorAll;
        
        int x = 0, y = 0;
        
        // Divide numbers into two groups
        for (int num : arr) {
            if (num & rightmostBit) {
                x ^= num;
            } else {
                y ^= num;
            }
        }
        
        return {x, y};
    }
    
    /**
     * Generate all subsets using bit manipulation
     * Time: O(2^n * n)
     */
    static vector<vector<int>> generateSubsets(const vector<int>& arr) {
        int n = arr.size();
        int totalSubsets = 1 << n;  // 2^n
        vector<vector<int>> subsets;
        
        for (int i = 0; i < totalSubsets; i++) {
            vector<int> subset;
            
            for (int j = 0; j < n; j++) {
                if (i & (1 << j)) {
                    subset.push_back(arr[j]);
                }
            }
            
            subsets.push_back(subset);
        }
        
        return subsets;
    }
    
    /**
     * Swap two numbers without temp variable
     * Time: O(1)
     */
    static void swapWithoutTemp(int& a, int& b) {
        if (a != b) {
            a ^= b;
            b ^= a;
            a ^= b;
        }
    }
    
    /**
     * Reverse bits of a number
     * Time: O(log n)
     */
    static unsigned int reverseBits(unsigned int n) {
        unsigned int result = 0;
        
        for (int i = 0; i < 32; i++) {
            result <<= 1;
            result |= (n & 1);
            n >>= 1;
        }
        
        return result;
    }
    
    /**
     * Count bits needed to convert A to B
     * Time: O(log n)
     */
    static int bitConversionCount(int a, int b) {
        int xorResult = a ^ b;
        return countSetBits(xorResult);
    }
    
    /**
     * Position of rightmost set bit
     * Time: O(1)
     */
    static int rightmostSetBit(int n) {
        if (n == 0) return -1;
        return log2(n & -n) + 1;
    }
    
    /**
     * Check if bits are alternating
     * Time: O(1)
     */
    static bool hasAlternatingBits(int n) {
        int shifted = n ^ (n >> 1);
        return (shifted & (shifted + 1)) == 0;
    }
    
    /**
     * Sum of two integers without + operator
     * Time: O(log n)
     */
    static int addWithoutPlus(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
    
    /**
     * Multiply by 7 without * operator
     * Time: O(1)
     */
    static int multiplyBy7(int n) {
        return (n << 3) - n;  // 8n - n = 7n
    }
    
    /**
     * Divide by 2 without / operator
     * Time: O(1)
     */
    static int divideBy2(int n) {
        return n >> 1;
    }
    
    /**
     * Check if number is even
     * Time: O(1)
     */
    static bool isEven(int n) {
        return (n & 1) == 0;
    }
    
    /**
     * Get maximum of two numbers without if-else
     * Time: O(1)
     */
    static int getMax(int a, int b) {
        int diff = a - b;
        int sign = (diff >> 31) & 1;  // 1 if negative, 0 if positive
        return a - sign * diff;
    }
};

// Demonstration
void demonstrateBitManipulation() {
    cout << string(70, '=') << endl;
    cout << "BIT MANIPULATION ALGORITHMS DEMONSTRATION" << endl;
    cout << string(70, '=') << endl;
    
    // Power of 2
    cout << "\n1. CHECK POWER OF 2" << endl;
    cout << "   Is 16 power of 2? " << (BitManipulation::isPowerOfTwo(16) ? "Yes" : "No") << endl;
    cout << "   Is 18 power of 2? " << (BitManipulation::isPowerOfTwo(18) ? "Yes" : "No") << endl;
    
    // Count set bits
    cout << "\n2. COUNT SET BITS" << endl;
    int n = 15;  // 1111 in binary
    cout << "   Number: " << n << " (binary: " << bitset<8>(n) << ")" << endl;
    cout << "   Set bits: " << BitManipulation::countSetBits(n) << endl;
    
    // Bit operations
    cout << "\n3. BIT OPERATIONS" << endl;
    n = 10;  // 1010
    cout << "   Number: " << n << " (binary: " << bitset<8>(n) << ")" << endl;
    cout << "   Get bit 1: " << BitManipulation::getBit(n, 1) << endl;
    cout << "   Set bit 0: " << BitManipulation::setBit(n, 0) 
         << " (binary: " << bitset<8>(BitManipulation::setBit(n, 0)) << ")" << endl;
    cout << "   Toggle bit 3: " << BitManipulation::toggleBit(n, 3)
         << " (binary: " << bitset<8>(BitManipulation::toggleBit(n, 3)) << ")" << endl;
    
    // XOR from 1 to n
    cout << "\n4. XOR FROM 1 TO N" << endl;
    cout << "   XOR(1 to 10): " << BitManipulation::xorFrom1ToN(10) << endl;
    
    // Find missing number
    cout << "\n5. FIND MISSING NUMBER" << endl;
    vector<int> arr = {0, 1, 2, 4, 5};
    cout << "   Array: [0, 1, 2, 4, 5]" << endl;
    cout << "   Missing: " << BitManipulation::findMissing(arr) << endl;
    
    // Find two non-repeating
    cout << "\n6. FIND TWO NON-REPEATING" << endl;
    vector<int> arr2 = {1, 2, 3, 1, 2, 5};
    auto [x, y] = BitManipulation::findTwoNonRepeating(arr2);
    cout << "   Array: [1, 2, 3, 1, 2, 5]" << endl;
    cout << "   Non-repeating: " << x << ", " << y << endl;
    
    // Generate subsets
    cout << "\n7. GENERATE SUBSETS" << endl;
    vector<int> set = {1, 2, 3};
    auto subsets = BitManipulation::generateSubsets(set);
    cout << "   Set: [1, 2, 3]" << endl;
    cout << "   Subsets count: " << subsets.size() << endl;
    
    // Arithmetic operations
    cout << "\n8. ARITHMETIC WITHOUT OPERATORS" << endl;
    cout << "   5 + 3 = " << BitManipulation::addWithoutPlus(5, 3) << endl;
    cout << "   4 * 7 = " << BitManipulation::multiplyBy7(4) << endl;
    cout << "   10 / 2 = " << BitManipulation::divideBy2(10) << endl;
    
    // Reverse bits
    cout << "\n9. REVERSE BITS" << endl;
    unsigned int num = 43261596;
    cout << "   Original: " << bitset<32>(num) << endl;
    cout << "   Reversed: " << bitset<32>(BitManipulation::reverseBits(num)) << endl;
    
    // Alternating bits
    cout << "\n10. ALTERNATING BITS" << endl;
    cout << "   5 (101): " << (BitManipulation::hasAlternatingBits(5) ? "Yes" : "No") << endl;
    cout << "   7 (111): " << (BitManipulation::hasAlternatingBits(7) ? "Yes" : "No") << endl;
    
    cout << "\n" << string(70, '=') << endl;
}

int main() {
    demonstrateBitManipulation();
    return 0;
}
