import random
num = int(input("내 번호 입력(10 ~ 99): "))
randomNum = random.randint(10, 99)
first = randomNum % 10
second = int(randomNum / 10)

print("당첨번호는", randomNum, "입니다.")
if num % 10 == first:
    if num / 10 == second:
        print("피자 10판 당첨")
    else:
        print("치킨 5마리 당첨")
elif num % 10 == second or num / 10 == first:
    print("치킨 5마리 당첨")
else: print("꽝입니다.")