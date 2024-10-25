from typing import List
class MergeArrays:
    def merge_sorted(nums1: List[int], m: int, nums2: List[int], n: int) -> list:
      index1 = m - 1
      index2 = n - 1
      i = 1
      while i <= n:
        nums1.append(0)
        i+=1

      right = m + n - 1

      while index2 >= 0:
            if index1 >= 0 and nums1[index1] > nums2[index2]:
                nums1[right] = nums1[index1]
                index1 -= 1
            else:
                nums1[right] = nums2[index2]
                index2 -= 1

            right -= 1
      return nums1

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    arr1 = input('Enter elements of 1st list separated by space \n')
    arr2 = input('Enter elements of 2nd list separated by space \n')

    list1 = arr1.split()
    list2 = arr2.split()
    n = len(list1)
    m = len(list2)

    print("The merged array")
    print(MergeArrays.merge_sorted(list1, len(list1), list2, len(list2)))
