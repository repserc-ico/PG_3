import random

suit = ["♠", "♦", "♥", "♣"]
cards = []
for i in range(1,53):
    cards.append(i)

print(cards)    #シャッフル前
random.shuffle(cards)
print(cards)    #シャッフル後

pick = int(input("何枚目のカードを引きますか(1-52) >>"))
#(引いたカードはcards[pick-1]になります)

#スートを特定する
s = cards[pick-1]//13
print(s)
#ナンバーを特定する
number = cards[pick-1]%13
if number == 0:
    s-=1
    number=13

print(f"あなたが引いたのは{suit[s]}の{number}です")