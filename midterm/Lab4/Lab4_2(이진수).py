num = int(input("숫자를 입력하세요: "))
i = 0
binary = 0
while num > 0:
    binary += int(num % 2) * pow(10,i)
    num /= 2
    i += 1

print(binary)