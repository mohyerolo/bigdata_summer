import random

def init(chanllengers, win, lose, same, challenger):
    challengers.append(challenger)
    win.append(0)
    lose.append(0)
    same.append(0)

def winOrLose(status, index, usingList):
    if status == 0:
        print("비겼습니다.")
    elif status == 1:
        print("사람 승!")
    else:
        print("컴퓨터 승!")
    usingList[index] += 1

def printResult(challengers, win, same, lose):
    for i in range(len(challengers)):
        print(f"{challengers[i]}: {win[i]}승 {same[i]}무 {lose[i]}패")
    print()

rps_dic = {1:'가위', 2:'바위', 3:'보'}
match_table = {'가위':'보', '바위':'가위', '보':'바위'}

challengers = []
win = []
lose = []
same = []

challenger = input("도전자 이름: ")

while challenger != "":
    if challenger not in challengers:
        init(challengers, win, lose, same, challenger)

    index = challengers.index(challenger)

    mine = input("가위, 바위, 보 입력: ")
    com = random.randint(1, 3)
    print("컴퓨터:", rps_dic[com])

    if mine == rps_dic[com]:
        winOrLose(0, index, same)
    elif match_table[mine] == rps_dic[com]:
        winOrLose(1, index, win)
    else: 
        winOrLose(-1, index, lose)
    
    printResult(challengers, win,same, lose)
        
    challenger = input("도전자 이름: ")