def longestPalindrome(s):
    longest = ''
    def findLongest(s, l, r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]
    
    for i in range(len(s)):
        s1 = findLongest(s, i, i)
        if len(s1) > len(longest): longest = s1
        
        s2 = findLongest(s, i, i+1)
        if len(s2) > len(longest): longest = s2
            
    return longest

if __name__ == '__main__':
    s = "babad"
    print(longestPalindrome(s))