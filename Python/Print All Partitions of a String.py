lst = []
temp = []
def all_partitions(s):
    helper(s)
    return lst
def helper(s):
    if s == '':
        lst.append(temp[:])
        return
    for i in range(len(s)):
        st = s[:i+1]
        temp.append(st)
        helper(s[i+1:])
        temp.pop()