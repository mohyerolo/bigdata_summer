import sqlite3

con, cur = None, None
data1 ,data2, data3 = "", "", ""
sql = ""

# 메인 코드
con = sqlite3.connect("Lab12\\midterm.db")
cur = con.cursor()
cur.execute("drop table mid_6")
cur.execute("drop table output")
cur.execute("create table if not exists mid_6 (name char(15), begin_year int, end_year int)")

while (True):
    data1 = input("이름 ==> ")
    if data1 == "":
        break
    data2 = input("입사년도 ==> ")
    data3 = input("퇴직년도 ==> ")
    sql = "insert into mid_6 values('" + data1 + "'," + data2 + "," + data3 + ")"
    cur.execute(sql)
con.commit()

maxEmp = ""
maxYear = 0

cur.execute("create table if not exists output (name char(15), period int)")

cur.execute("select * from mid_6")
data_list = cur.fetchall()

print("이름    입사연도    퇴직연도    재직기간")
print('-' * 50)
for row in data_list:
    name = row[0]
    data2 = row[1]
    data3 = row[2]
    period = row[2] - row[1] + 1
    if maxYear < period:
        maxEmp = name
        maxYear = period
    print("%s    %s        %s        %s년" % (name, row[1], row[2], period))
    sql = "insert into output values('" + name + "'," + str(period) + ")"
    cur.execute(sql)

print("재직기간이 가장 긴 사람은 <%s>이다" % maxEmp)
print("%s의 재직 기간은 <%d년>이다" % (maxEmp, maxYear))

con.commit()
con.close()