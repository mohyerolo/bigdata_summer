import csv

employees = []

with open("Lab12\\csv\\q6_input.csv", "w", encoding="utf-8", newline='') as input_file:
    writer = csv.writer(input_file)
    writer.writerow(['이름', '입사년도', '퇴직연도'])

    while 1:
        name = input("이름==> ")
        if name == '':
            break
        hire_date = int(input("입사년도==> "))
        end_date = int(input("퇴직연도==> "))

        employee = [name, hire_date, end_date]
        writer.writerow(employee)

with open("Lab12\\csv\\q6_output.csv", "w", encoding="utf-8", newline='') as output:
    writer = csv.writer(output)
    
    infile = open("Lab12\\csv\\q6_input.csv", "r", encoding="utf-8")
    data_file = csv.reader(infile)
    maxYear = 0
    maxEmp = ''
    rownum = 0
    print("이름      입사년도     퇴직연도     재직기간")
    print("-" * 30)
    for data in data_file:
        if rownum == 0:
            writer.writerow(['이름', '재직기간'])
        else:
            name = data[0]
            year = int(data[2]) - int(data[1]) + 1
            if year > maxYear:
                maxYear = year
                maxEmp = name
            print("%s %5d %5d %5s년" % (data[0], int(data[1]), int(data[2]), year))
            writer.writerow([name, str(year)])
        rownum += 1
    infile.close()
        
    print("재직기간이 가장 긴 사람은 <%s>이다" % maxEmp)
    print("%s의 재직 기간은 <%d년>이다" % (maxEmp, maxYear))


