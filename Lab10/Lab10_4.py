class Student:
    def __init__(self, name, dept, num, gender):
        self.name = name
        self.dept = dept
        self.num = num
        self.__gender = gender
    
    def week_check(self):
        if int(self.num) % 2 == 0:
            return "짝수"
        else: return "홀수"

    def get_gender(self):
        return self.__gender

ddwu = Student("동덕", "컴퓨터학과", "2022001", "여자")
print("ddwu는 %s %s번 이름은 %s입니다." % (ddwu.dept, ddwu.num, ddwu.name))
print("ddwu는", ddwu.week_check(),"주에 학교를 갑니다.")
print(ddwu.get_gender())