ages = [24, 29, 20, 18, 13, 54, 10]
f = lambda x : x >= 19
result = list(filter(f, ages))
print("성년 리스트:", end=" ")
for i in result:
    print(i, end=" ")