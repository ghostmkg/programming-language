def generate_fibonacci_series(N):
    last_term = 1
    second_last_term = 0
    for i in range(1, N+1):
        if i == 1:
            print(second_last_term, end=" ")
        elif i == 2:
            print(last_term, end=" ")
        else:
            curr_term = last_term + second_last_term
            print(curr_term, end=" ")
            second_last_term = last_term
            last_term = curr_term

n = int(input())
generate_fibonacci_series(n)