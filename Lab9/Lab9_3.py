# 람다식을 이용하여 화씨 온도를 섭씨온도로 변환하는 프로그램을 작성하시오
f = int(input("화씨 온도: "))
c = round((f - 32) / 1.8, 2)
print("섭씨 온도:", c)

#  1에서 30까지 수 중에서 2와 3의 배수를 구하여 출력하시오
result = [i for i in range(1, 31) if i % 2 == 0 or i % 3 == 0]
print("2와 3의 배수: ", result)