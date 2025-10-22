import bisect

def maxEnvelopes(envelopes):
    # Step 1: Sort envelopes by width ASC, and height DESC for same width
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    # Step 2: Extract heights
    heights = [h for _, h in envelopes]
    
    # Step 3: Find LIS using binary search (O(n log n))
    lis = []
    for h in heights:
        idx = bisect.bisect_left(lis, h)
        if idx == len(lis):
            lis.append(h)
        else:
            lis[idx] = h
    return len(lis)
