# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    # 이렇게 __str__ 메소드를 정의해놓으면 str() 함수 호출시 __str__() 함수가 자동으로 호출된다.
    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

    def __eq__(self, value):
        return self.get_average() == value
    def __ne__(self, value):
        return self.get_average() != value
    def __gt__(self, value):
        return self.get_average() > value
    def __ge__(self, value):
        return self.get_average() >= value
    def __lt__(self, value):
        return self.get_average() < value
    def __le__(self, value):
        return self.get_average() <= value

# 학생을 선언합니다.
test = Student("A", 90, 90, 90, 90)

# 출력합니다.
print("test == 90:", test == 90)
print("test != 90:", test != 90)
print("test > 90:", test > 90)
print("test >= 90:", test >= 90)
print("test < 90:", test < 90)
print("test <= 90:", test <= 90)