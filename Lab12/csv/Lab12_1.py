import csv

rownum = 0
sum = 0

# infile = open("Lab12\\rn_20220707131629.csv", "r")
# data = csv.reader(infile)

# for line in data:
#     rownum += 1
#     sum += float(line[2])

# infile.close()
# print("서울 2012년부터 2021년까지의 총 강수량:", sum)
# print("서울 2012년부터 2021년까지의 평균 강수량:", sum / rownum)
    
with open("Lab12\\rn_20220707131629.csv", "r") as infile:
    csv_data = csv.reader(infile)

    for row in csv_data:
        sum += float(row[2])
        rownum += 1
    print("서울 2012년부터 2021년까지의 총 강수량:", sum)
    print("서울 2012년부터 2021년까지의 평균 강수량:", sum / rownum)
