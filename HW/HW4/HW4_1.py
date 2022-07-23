num = int(input("수강 과목 수 입력: "))
scores = []
ok = 0
notOk = 0

for i in range(0, num):
    scores.append(int(input(f"score {i + 1}: ")))

for score in scores:
    if score >= 80: ok += 1
    else: notOk += 1

print("합격 과목 수 :", ok)
print("불합격과목 수 :", notOk)