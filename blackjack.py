- 👋 Hi, I’m @chocowein
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
chocowein/chocowein is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
import random

spade  = [1,2,3,4,5,6,7,8,9,10,10,10,10]
heart   = [1,2,3,4,5,6,7,8,9,10,10,10,10]
dia     = [1,2,3,4,5,6,7,8,9,10,10,10,10]
clover  = [1,2,3,4,5,6,7,8,9,10,10,10,10]
cards   = [spade,heart,dia,clover]
marks = ["♤","♡","♢","♧"]
cardsum = 0
cardsum2 = 0

print("カード追加 =「hit」")
print("勝負 = 「stand」")

cardmark2   = random.randint(0,(len(cards)-1))
cardnumber2 = random.randint(0,(len(cards[cardmark2])-1))
outcard2 = cards[cardmark2][cardnumber2]
cardsum2 += outcard2
print("enemy--")
print("?")
cardmark2   = random.randint(0,(len(cards)-1))
cardnumber2 = random.randint(0,(len(cards[cardmark2])-1))
outcard2 = cards[cardmark2][cardnumber2]
cardsum2 += outcard2
print(marks[cardmark2] ,end = "")
print(outcard2)
print("-----------")

cardmark   = random.randint(0,(len(cards)-1))
cardnumber = random.randint(0,(len(cards[cardmark])-1))
outcard = cards[cardmark][cardnumber]
cardsum += outcard
print("you------")
print(marks[cardmark] ,end = "")
print(outcard)
cardmark   = random.randint(0,(len(cards)-1))
cardnumber = random.randint(0,(len(cards[cardmark])-1))
outcard = cards[cardmark][cardnumber]
cardsum += outcard
print(marks[cardmark] ,end = "")
print(outcard)
print("-----------")

yesno = "hit"

while yesno == "hit":
    if cardsum2 <= 16:
        cardmark2   = random.randint(0,(len(cards)-1))
        cardnumber2 = random.randint(0,(len(cards[cardmark2])-1))
        outcard2 = cards[cardmark2][cardnumber2]
        del cards[cardmark2][cardnumber2]
        cardsum2 += outcard2
        if cardsum2 > 21:
          print("enemy lose")
          break;
        print("enemy--")
        print(marks[cardmark2] ,end = "")
        print(outcard2)
        print("-----------")
    else:
        print("enemy--")
        print("stand")
        print("-----------")
    yesno = input()
    if yesno == "stand":
      break;
    cardmark   = random.randint(0,(len(cards)-1))
    cardnumber = random.randint(0,(len(cards[cardmark])-1))
    outcard = cards[cardmark][cardnumber]
    del cards[cardmark][cardnumber]
    cardsum += outcard
    if cardsum > 21:
      print("you lose")
      break;
    print("you------")
    print(marks[cardmark] ,end = "")
    print(outcard)
    print("-----------")


if cardsum > cardsum2:
  if cardsum <= 21:
    print("you win")
elif cardsum == cardsum2:
  print("draw")
if cardsum < cardsum2:
  if cardsum2 <= 21:
    print("you lose")
elif cardsum == cardsum2:
  print("draw")

print("gameset------")
print("you" + str(cardsum))
print("enemy" + str(cardsum2))
print("------------------")


# print(spade)
# print(heart)
# print(dia)
# print(clover)
