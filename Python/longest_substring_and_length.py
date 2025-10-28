def longest_substring_and_length(s: str):
    last_index = {}
    left = 0
    max_len = 0
    start_of_max = 0
    for right, ch in enumerate(s):
        if ch in last_index:
            left = max(left, last_index[ch] + 1)
        last_index[ch] = right
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_of_max = left
    return s[start_of_max:start_of_max+max_len], max_len
