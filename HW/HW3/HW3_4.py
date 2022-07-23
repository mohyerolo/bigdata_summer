num1 = int(input("첫 번째 수 입력: "))
num2 = int(input("두 번째 수 입력: "))
op = input("원하는 연산 기호 하나 입력: (+ - * /): ")

if (op == '+'): result = num1 + num2
elif (op == '-'): result = num1 - num2
elif (op == '*'): result = num1 * num2
else: result = int(num1 / num2)

print(f"{num1} {op} {num2} = {result}")