print("당신이 태어난 연도를 입력하세요.")
birth_year = input()
age = 2020 - int(birth_year) + 1
if (age >= 8):
    if (age < 14): print("초등학생")
    elif (age < 17): print("중학생")
    elif (age < 20): print("고등학생")
    elif (age <= 26): print("대학생")
    else: print("학생이 아닙니다.")
else: print("학생이 아닙니다.")