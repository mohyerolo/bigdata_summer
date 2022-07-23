import random

print("  << 덧셈 문제 연습 게임>>  ")
print("---------------------------")
result = 0
correct = 0
cnt = 0

while correct < 5:
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    result = int(input(f"{num1} + {num2} = "))
    if result == (num1 + num2): 
        correct += 1
        print("맞았다.")
    else: print("틀렸다.")
    cnt += 1

print("시도횟수:", cnt)
print(">>>")