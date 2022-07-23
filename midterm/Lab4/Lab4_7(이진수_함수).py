def decimalToBinary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

num = int(input("숫자를 입력하세요: "))
print(decimalToBinary(num))