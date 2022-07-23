class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def about_me(self):
        print("저의 이름은 %s이고요, 제 나이는 %d살입니다." % (self.name, self.age))


class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date

    def about_me(self):
        super().about_me()
        print("제 급여는 %d원이고 제 입사일은 %s입니다." % (self.salary, self.hire_date))

    def do_work(self):
        print("열심히 일하자")

aPerson = Employee("홍길동", 35, "남자", 50000, '2021-3-4')
aPerson.do_work()
aPerson.about_me()