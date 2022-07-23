scores = [[49, 43, 49], [80, 60, 82], [20, 85, 48],
 [100, 30, 50] ,[80, 90, 100]]
avgList = []
sum = 0
avg = 0
for i in scores:
    for score in i:
        sum += score
    avg = sum / 3
    avgList.append(avg)
    sum = 0

print(avgList)