class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경한다: From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

ddwu = SoccerPlayer("동덕", "골키퍼", 3)
print(ddwu.name)

ddwu.change_back_number(5)
print(ddwu.back_number)