def isPalindrome(N):
    original_num=N
    reversed_num=0
    while(N!=0):
        last_digit=N%10
        reversed_num=rev_num*10+last_digit
        N=N//10
    if (reversed_num==original_num):
        return True
    else:
        return False