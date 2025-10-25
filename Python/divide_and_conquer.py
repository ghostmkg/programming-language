"""
Divide and Conquer Algorithms
==============================

Classic divide and conquer algorithms including merge operations,
binary search variants, and optimization problems.

Author: Hacktoberfest 2025 Contributor
"""

from typing import List, Tuple, Optional
import math


class DivideAndConquer:
    """Collection of divide and conquer algorithms"""
    
    @staticmethod
    def binary_search(arr: List[int], target: int) -> int:
        """
        Binary Search - Classic divide and conquer
        
        Time: O(log n)
        Space: O(1) iterative, O(log n) recursive
        """
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    @staticmethod
    def binary_search_first_occurrence(arr: List[int], target: int) -> int:
        """
        Find first occurrence of target
        
        Time: O(log n)
        """
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                result = mid
                right = mid - 1  # Continue searching left
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    @staticmethod
    def binary_search_last_occurrence(arr: List[int], target: int) -> int:
        """
        Find last occurrence of target
        
        Time: O(log n)
        """
        left, right = 0, len(arr) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                result = mid
                left = mid + 1  # Continue searching right
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
    
    @staticmethod
    def search_rotated_array(arr: List[int], target: int) -> int:
        """
        Search in rotated sorted array
        
        Time: O(log n)
        """
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                return mid
            
            # Left half is sorted
            if arr[left] <= arr[mid]:
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
    
    @staticmethod
    def find_peak_element(arr: List[int]) -> int:
        """
        Find a peak element (greater than neighbors)
        
        Time: O(log n)
        """
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left
    
    @staticmethod
    def find_min_rotated(arr: List[int]) -> int:
        """
        Find minimum in rotated sorted array
        
        Time: O(log n)
        """
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid] > arr[right]:
                left = mid + 1
            else:
                right = mid
        
        return arr[left]
    
    @staticmethod
    def median_of_two_sorted(nums1: List[int], nums2: List[int]) -> float:
        """
        Find median of two sorted arrays
        
        Time: O(log(min(m, n)))
        Space: O(1)
        """
        # Ensure nums1 is smaller
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1
        
        return 0.0
    
    @staticmethod
    def quick_select(arr: List[int], k: int) -> int:
        """
        Find kth smallest element using Quick Select
        
        Time: O(n) average, O(n^2) worst
        Space: O(1)
        """
        def partition(left, right):
            pivot = arr[right]
            i = left
            
            for j in range(left, right):
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            
            arr[i], arr[right] = arr[right], arr[i]
            return i
        
        left, right = 0, len(arr) - 1
        
        while left <= right:
            pivot_index = partition(left, right)
            
            if pivot_index == k:
                return arr[k]
            elif pivot_index < k:
                left = pivot_index + 1
            else:
                right = pivot_index - 1
        
        return arr[k]
    
    @staticmethod
    def majority_element(arr: List[int]) -> Optional[int]:
        """
        Find majority element (appears > n/2 times)
        Using divide and conquer
        
        Time: O(n log n)
        Space: O(log n)
        """
        def majority_helper(left, right):
            if left == right:
                return arr[left]
            
            mid = left + (right - left) // 2
            left_majority = majority_helper(left, mid)
            right_majority = majority_helper(mid + 1, right)
            
            if left_majority == right_majority:
                return left_majority
            
            # Count occurrences
            left_count = sum(1 for i in range(left, right + 1) if arr[i] == left_majority)
            right_count = sum(1 for i in range(left, right + 1) if arr[i] == right_majority)
            
            return left_majority if left_count > right_count else right_majority
        
        if not arr:
            return None
        
        candidate = majority_helper(0, len(arr) - 1)
        
        # Verify candidate
        count = sum(1 for x in arr if x == candidate)
        return candidate if count > len(arr) // 2 else None
    
    @staticmethod
    def count_inversions(arr: List[int]) -> int:
        """
        Count number of inversions (pairs where i < j but arr[i] > arr[j])
        
        Time: O(n log n)
        Space: O(n)
        """
        def merge_count(left, right):
            i = j = 0
            count = 0
            merged = []
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    count += len(left) - i  # All remaining in left are inversions
                    j += 1
            
            merged.extend(left[i:])
            merged.extend(right[j:])
            
            return merged, count
        
        def merge_sort_count(arr):
            if len(arr) <= 1:
                return arr, 0
            
            mid = len(arr) // 2
            left, left_count = merge_sort_count(arr[:mid])
            right, right_count = merge_sort_count(arr[mid:])
            merged, merge_count_val = merge_count(left, right)
            
            return merged, left_count + right_count + merge_count_val
        
        _, count = merge_sort_count(arr.copy())
        return count
    
    @staticmethod
    def closest_pair_1d(arr: List[int]) -> Tuple[int, int]:
        """
        Find closest pair of points in 1D
        
        Time: O(n log n)
        """
        arr.sort()
        min_diff = float('inf')
        result = (arr[0], arr[1])
        
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                result = (arr[i], arr[i + 1])
        
        return result
    
    @staticmethod
    def max_subarray_sum(arr: List[int]) -> int:
        """
        Maximum subarray sum using divide and conquer
        
        Time: O(n log n)
        Space: O(log n)
        """
        def max_crossing_sum(left, mid, right):
            left_sum = float('-inf')
            current_sum = 0
            
            for i in range(mid, left - 1, -1):
                current_sum += arr[i]
                left_sum = max(left_sum, current_sum)
            
            right_sum = float('-inf')
            current_sum = 0
            
            for i in range(mid + 1, right + 1):
                current_sum += arr[i]
                right_sum = max(right_sum, current_sum)
            
            return left_sum + right_sum
        
        def max_subarray_helper(left, right):
            if left == right:
                return arr[left]
            
            mid = left + (right - left) // 2
            
            left_max = max_subarray_helper(left, mid)
            right_max = max_subarray_helper(mid + 1, right)
            cross_max = max_crossing_sum(left, mid, right)
            
            return max(left_max, right_max, cross_max)
        
        return max_subarray_helper(0, len(arr) - 1)


# Demonstration
def demonstrate_divide_and_conquer():
    print("=" * 70)
    print("DIVIDE AND CONQUER ALGORITHMS DEMONSTRATION")
    print("=" * 70)
    
    algo = DivideAndConquer()
    
    # Binary Search
    print("\n1. BINARY SEARCH")
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"   Array: {arr}")
    print(f"   Search 7: index {algo.binary_search(arr, 7)}")
    print(f"   Search 11: index {algo.binary_search(arr, 11)}")
    
    # First/Last Occurrence
    print("\n2. FIRST/LAST OCCURRENCE")
    arr = [1, 2, 2, 2, 3, 4, 5]
    print(f"   Array: {arr}")
    print(f"   First occurrence of 2: {algo.binary_search_first_occurrence(arr, 2)}")
    print(f"   Last occurrence of 2: {algo.binary_search_last_occurrence(arr, 2)}")
    
    # Rotated Array Search
    print("\n3. SEARCH IN ROTATED ARRAY")
    arr = [4, 5, 6, 7, 0, 1, 2]
    print(f"   Array: {arr}")
    print(f"   Search 0: index {algo.search_rotated_array(arr, 0)}")
    print(f"   Min element: {algo.find_min_rotated(arr)}")
    
    # Peak Element
    print("\n4. FIND PEAK ELEMENT")
    arr = [1, 3, 20, 4, 1, 0]
    print(f"   Array: {arr}")
    print(f"   Peak at index: {algo.find_peak_element(arr)}")
    
    # Median of Two Sorted Arrays
    print("\n5. MEDIAN OF TWO SORTED ARRAYS")
    nums1 = [1, 3]
    nums2 = [2]
    print(f"   Array 1: {nums1}")
    print(f"   Array 2: {nums2}")
    print(f"   Median: {algo.median_of_two_sorted(nums1, nums2)}")
    
    # Quick Select
    print("\n6. QUICK SELECT (KTH SMALLEST)")
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    print(f"   Array: {arr}")
    print(f"   3rd smallest: {algo.quick_select(arr.copy(), k - 1)}")
    
    # Majority Element
    print("\n7. MAJORITY ELEMENT")
    arr = [2, 2, 1, 1, 1, 2, 2]
    print(f"   Array: {arr}")
    print(f"   Majority: {algo.majority_element(arr)}")
    
    # Count Inversions
    print("\n8. COUNT INVERSIONS")
    arr = [8, 4, 2, 1]
    print(f"   Array: {arr}")
    print(f"   Inversions: {algo.count_inversions(arr)}")
    
    # Max Subarray Sum
    print("\n9. MAXIMUM SUBARRAY SUM")
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"   Array: {arr}")
    print(f"   Max sum: {algo.max_subarray_sum(arr)}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    demonstrate_divide_and_conquer()
