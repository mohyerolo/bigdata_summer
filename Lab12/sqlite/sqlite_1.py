import sqlite3

con, cur = None, None
data1 ,data2, data3, data4 = "", "", "", ""
sql = ""

# 메인 코드
con = sqlite3.connect("Lab12\\bigdata.db")
cur = con.cursor()
cur.execute("create table if not exists userTable (id char(4) primary key, userName char(15), email char(15), birthYear int)")

while (True):
    data1 = input("사용자ID ==> ")
    if data1 == "":
        break
    data2 = input("사용자이름 ==> ")
    data3 = input("이메일 ==> ")
    data4 = input("출생연도 ==> ")
    sql = "insert into userTable values('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    print(sql)
    cur.execute(sql)

con.commit()
con.close()