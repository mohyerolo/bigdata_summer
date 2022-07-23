scores = []

scores.append(int(input("성적을 입력하시오:")))
scores.append(int(input("성적을 입력하시오:")))
scores.append(int(input("성적을 입력하시오:")))
scores.append(int(input("성적을 입력하시오:")))
scores.append(int(input("성적을 입력하시오:")))

print(scores)

sumList = sum(scores)
avg = sumList / len(scores)

print("성적의 합 =", sumList)
print("평균 =", avg)