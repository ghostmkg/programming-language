# Solution for No Idea Problem on Hackerrank
'''
There is an array of n integers. There are also 2 disjoint sets, a and b, each containing m integers. You like all the integers in set a and dislike all the integers in set b. Your initial happiness is 0. For each i integer in the array belongs to A you add 1 to your happiness. If it is in b, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
'''
n, m = map(int, input().split())

elements = list(map(int, input().split()))

a = set(map(int, input().split()[:n]))

b = set(map(int, input().split()[:m]))

happiness = 0

for item in elements:
  if item in a:
    happiness += 1
  elif item in b:
    happiness -= 1
print(happiness)


