import csv

employee = []
rownum = 0
header = ''

with open("Lab12\\q6_input.csv", "w", encoding = "utf-8", newline='') as infile:
    writer = csv.writer(infile)
    writer.writerow(['이름', '입사년도', '퇴직년도'])
    while True:
        data1 = input("이름 ==> ")
        if data1 == "":
            break
        data2 = input("입사년도 ==> ")
        data3 = input("퇴직년도 ==> ")
        writer.writerow([data1, data2, data3])

with open("Lab12\\q6_input.csv", "r", encoding = "utf-8") as infile:
    output = open("Lab12\\q6_output.csv", "w", encoding="utf-8", newline='')
    csv_data = csv.reader(infile)
    writer = csv.writer(output)
    writer.writerow(['이름', '재직기간'])
    
    print("이름    입사연도    퇴직연도    재직기간")
    print('-' * 50)

    maxEmp = ''
    maxYear = 0

    for row in csv_data:
        if rownum == 0:
            header = row
        else:
            employee.append(row)
            name = row[0]  
            year = int(row[2]) - int(row[1]) + 1
            if maxYear < year:
                maxEmp = name
                maxYear = year
            print("%s    %s    %s    %s년" % (name, row[1], row[2], year))
            writer.writerow([name, year])
        rownum += 1
    output.close()

    print("재직기간이 가장 긴 사람은 <%s>이다" % maxEmp)
    print("%s의 재직 기간은 <%d년>이다" % (maxEmp, maxYear))