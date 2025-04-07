n = int(input())
sangkeun_cards = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))

dic = {}
for card in sangkeun_cards:
    dic[card] = 1

for i in cards:
    if i in dic:
        print(1, end=' ')
    else:
        print(0, end=' ')



