def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    max_len = 1
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[j] not in s[i:j]:
                max_len = max(max_len, j-i+1)
            else:
                break
    return max_len


if __name__ == '__main__':
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))