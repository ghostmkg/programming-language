def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1  # Initialize two pointers
    left_max, right_max = height[left], height[right]  # Initialize max values
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water_trapped += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water_trapped += right_max - height[right]
            right -= 1

    return water_trapped

# Example usage
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
result = trap(height)
print("Amount of water trapped:", result)
