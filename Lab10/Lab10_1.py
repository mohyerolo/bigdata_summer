from notebook_mod import Note
from notebook_mod import NoteBook

contents = "노트1페이지 내용"
note1 = Note(contents)

note1.remove_all()

contents = "노트 2페이지 내용"
note2 = Note(contents)

contents = "노트 3페이지 내용"
note3 = Note(contents)

ddwu_notebook = NoteBook("파이썬 요약집")
ddwu_notebook.add_note(note2)
print(ddwu_notebook.pages)