import heapq
def findKthLargest(nums, k):
    heap=[]
    for i in nums:
        heapq.heappush(heap,-i)
    for i in range(k):
        if i!=k-1:
            heapq.heappop(heap)
        else:
            return -heap[0]