from typing import List

def fallingSquares(positions: List[List[int]]) -> List[int]:
    # store intervals as tuples: (left, right, height_top)
    intervals = []
    ans = []
    current_max = 0

    for left, size in positions:
        right = left + size
        # base height is the maximum top height among intervals that overlap [left, right)
        base = 0
        for l, r, h in intervals:
            # overlap iff l < right and r > left  (strict overlap along x-axis)
            if l < right and r > left:
                base = max(base, h)
        new_top = base + size
        intervals.append((left, right, new_top))
        current_max = max(current_max, new_top)
        ans.append(current_max)

    return ans

