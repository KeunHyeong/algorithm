from itertools import *

n, m = map(int, input().split())
cards = list(map(int, input().split()))

lst = []
for card in combinations(cards, 3):
    lst.append(sum(card))

lst.sort(reverse=True)

for item in lst:
    if item <= m:
        print(item)
        break
