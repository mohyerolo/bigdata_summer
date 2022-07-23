import csv
france_data = []
header = []
rownum = 0

with open("Lab12\\csv\\customers.csv", "r", encoding = "cp949") as p_file:
    csv_data = csv.reader(p_file)
    for row in csv_data:
        if rownum == 0:
            header = row
        # 원래 csv는 콤마를 기준으로 구분해서 문자로 받을 필요가 없음
        if row[10].upper() == "FRANCE":
            france_data.append(row)
            print(row)
        rownum += 1

with open("Lab12\\csv\\france_data2.csv", "w", encoding="cp949", newline='') as s_p_file:
    writer = csv.writer(s_p_file)
    writer.writerow(header)
    for row in france_data:
        print(row)
        writer.writerow(row)