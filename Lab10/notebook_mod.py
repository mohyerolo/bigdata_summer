class Note:
    def __init__(self, contents):
        self.contents = contents
        print(contents)
    def remove_all(self):
        self.contents = "삭제된 노트이다."

class NoteBook:
    def __init__(self, title):
        self.title = title
        self.pages = 0
        self.notes = {}

    def add_note(self, note, page_number = 0):
        if len(self.notes.keys()) < 300:
            if page_number == 0:
                if self.pages < 301:
                    self.notes[self.pages] = note
                    self.pages += 1
                else:
                    for i in range(300):
                        if i not in list(self.notes.key()):
                            self.notes[self.pages] = note
            else:
                if page_number not in self.notes.keys():
                    self.notes[page_number] = note
                else:
                    print("해당 페이지에는 이미 노트가 존재합니다.")
        else:
            print("더 이상 노트를 추가하지 못합니다")

    def remove_note(self, page_number):
        del self.notes[page_number]

    def __str__(self):
        return self.name