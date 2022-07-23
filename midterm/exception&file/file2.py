infile = open("c:\\Users\\USER\\Desktop\\빅데이터처리\\code\\exception&file\\dream.txt", "r")

# 1번
try:
    # outfile = open("c:\\Users\\USER\\Desktop\\빅데이터처리\\code\\exception&file\\output.txt", "w")
    outfile = open("c:\\Users\\USER\\Desktop\\빅데이터처리\\code\\exception&file\\output2.txt", "w", encoding="utf-8")
    with open("c:\\Users\\USER\\Desktop\\빅데이터처리\\code\\exception&file\\dream.txt", "r", encoding="utf-8") as infile:
        str_contents = infile.read()
        print("문자열:", str_contents);

        word_list = str_contents.split(" ")
        line_list = str_contents.split("\n")

        print("총 글자수:", len(str_contents))
        print("단어 수:", len(word_list))
        print("라인 수:", len(line_list))

        outfile.write("총 글자 수:" + str(len(str_contents)) + "\n")
        outfile.write("총 단어 수:" + str(len(word_list)) + "\n")
        outfile.write("총 라인 수:" + str(len(line_list)) + "\n")

        outfile.close()

    print("\n-- 줄단위 --")
    with open("c:\\Users\\USER\\Desktop\\빅데이터처리\\code\\exception&file\\dream.txt", "r") as infile:
        while 1:
            contents = infile.readline()
            if not contents:
                break;
            # print(contents) # 이렇게 하면 파일에서 엔터가 있을경우 두 번 줄바꿈 됨
            # print(contents, end="") # 이렇게 하면 파일에서 있는 줄바꿈만 반영됨
            print(contents.rstrip()) # 공백 제거 (공백안에 엔터키가 포함됨)

    print('\n-- 줄단위로 한꺼번에 --')
    with open("c:\\Users\\USER\\Desktop\\빅데이터처리\\code\\exception&file\\dream.txt", "r") as infile:
        line_contents = infile.readlines()
        print(line_contents)
except:
    print("오류")
# infile.close()