import random
num = random.randint(1, 100)

print("숫자를 맞혀 보세요. (1 ~ 100)")
userNum = int(input())
while userNum != num:
    if (userNum > num): print("숫자가 너무 큽니다.")
    elif (userNum < num): print("숫자가 너무 작습니다.")
    userNum = int(input())
else:
    print("정답입니다. 입력한 숫자는", num, "입니다.")