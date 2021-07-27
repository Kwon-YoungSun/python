# 원의 넓이와 둘레길이를 구하는 클래스를 만들고, 원하는 숫자를 입력하면 
# 그에 맞는 원의 넓이와 둘레길이를 출력하는 프로그램을 작성하시오.

# 모듈을 가져옵니다.
import math

# 클래스를 선언합니다.
class Circle:
    radius = 0
    circumference = 0.0
    area = 0.0
    # 생성자
    def __init__(self, radius):
        self.set_radius(radius)
        self.set_circumference(radius)
        self.set_area(radius)

    # 반지름 getter/setter
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value

    # 원 둘레 getter/setter
    def get_circumference(self):
        return self.__circumference
    def set_circumference(self, radius):
        self.__circumference = 2 * math.pi * radius * radius

    # 원 넓이 getter/setter
    def get_area(self):
        return self.__area
    def set_area(self, radius):
        self.__area = math.pi * radius**2

    def __str__(self):
        return "반지름:{}\t둘레:{}\t넓이:{}".format(
            self.radius,
            self.get_circumference(),
            self.get_area()
        )

# 원하는 숫자를 입력받아 객체 생성
circle = Circle(10)
print(str(circle))