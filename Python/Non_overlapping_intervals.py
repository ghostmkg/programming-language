def remove_overlapping(intervals):
    overlaps = 0
    for i in intervals:
        i[0], i[1] = i[1], i[0] 
    intervals.sort()
    for i in intervals:
        i[0], i[1] = i[1], i[0] 
    
    prev = intervals[0]
    for i in range(1, len(intervals)):
        if prev[1] > intervals[i][0]:
            overlaps += 1
        else:
            prev = intervals[i]
    return overlaps

intervals = [[1,2],[2,3],[3,4],[1,3]]
print(remove_overlapping(intervals))  # Output: 1
# Function to remove overlapping intervals
# and return the minimum number of intervals to remove