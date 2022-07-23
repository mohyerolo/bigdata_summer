import random

with open("c:\\Users\\USER\\Desktop\\빅데이터처리\\code\\exception&file\\hangman.txt", "r") as file:
    lines = []
    while 1:
        contents = file.readline().strip()
        if not contents:
            break;
        lines.append(contents)

    com = list(lines[random.randint(0, len(lines) - 1)])

    trying = []
    for i in range(len(com)):
        trying.append('_')
    
    cnt = 0
    while com != trying and cnt < 6:
        print(trying)
        guess = input("단어를 추측하세요: ")

        if guess in com:
            for i in range(len(com)):
                if guess == com[i]:
                    trying[i] = guess
        else: cnt += 1

    if com == trying:
        print("성공입니다.")
    else:
        print("실패입니다.")
        


