'''Maximum Subarray Sum using Kadane Algorithm'''

def kadane(arr):
    # Initialize maximumsum and current sum to 1stelement of array
    maxSum=arr[0]
    currSum=arr[0]

    # check the elements from 1'st element of an array to last element.
    for i in range(1,len(arr)):
        # get the current maximum sum
        currSum = max(arr[i], currSum+arr[i])

        # if current sum is greater than maximumsum assign current sum
        # to maximum sum
        if currSum >maxSum:
            maxSum=currSum

    # return maximumsum
    return maxSum


# Test case
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = kadane(arr)
print("Result", result) #6

#  Time complexity O(n)