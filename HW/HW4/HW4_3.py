import random
lotto = []

print("<<추천 로또 번호>>")
print("-----------------------")
for i in range(0, 5):
    while len(lotto) < 6:
        num = random.randint(1, 45)
        if lotto.count(num) != 0: continue;
        lotto.append(num)
        print(lotto[len(lotto) - 1], end=" ")
    lotto = []
    print()