from threading import currentThread


birthYear = int(input("태어난 년도: "))
currentYear = int(input("현재 년도: " ))
age = currentYear - birthYear + 1
print("나이 =", age)