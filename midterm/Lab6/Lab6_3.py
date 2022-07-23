import random

rps_dic = {1:'가위', 2:'바위', 3:'보'}
match_table = {'가위':'보', '바위':'가위', '보':'바위'}

com = random.randint(1, 3)

mine = input("가위, 바위, 보 입력: ")
print("컴퓨터:", rps_dic[com])

if mine == rps_dic[com]:
   print("비겼습니다.")
elif match_table[mine] == rps_dic[com]:
    print("사람 승!")
else: print("컴퓨터 승!")