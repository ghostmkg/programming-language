def generate_parentheses(n):
    res = []
    def backtrack(open_count, close_count, path):
        if len(path) == 2 * n:
            res.append("".join(path))
            return
        if open_count < n:
            path.append('(')
            backtrack(open_count + 1, close_count, path)
            path.pop()
        if close_count < open_count:
            path.append(')')
            backtrack(open_count, close_count + 1, path)
            path.pop()
    backtrack(0, 0, [])
    return res

# Examples
for n in range(1, 5):
    combos = generate_parentheses(n)
    print(f"n = {n}, count = {len(combos)}")
    print(combos)
    print()
STDOUT/STDERR
n = 1, count = 1
['()']

n = 2, count = 2
['(())', '()()']

n = 3, count = 5
['((()))', '(()())', '(())()', '()(())', '()()()']

n = 4, count = 14
['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']