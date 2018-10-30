N = int(input())
cards = []
Asum = 0
Bsum = 0
input = input()

for i in range(N):
    cards.append(int(input.split(" ")[i]))

for i in range(N):
    if i%2 == 0:
        Asum += max(cards)
        cards[cards.index(max(cards))] = 0
    else:
        Bsum += max(cards)
        cards[cards.index(max(cards))] = 0
print(Asum-Bsum)
