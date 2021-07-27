# 모듈을 가져옵니다.
import math

# 클래스를 선언합니다.
class Circle:
    def __init__(self, radius):
        self.__radius = radius      # __<변수이름> 의 형태
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

    # 게터와 세터를 선언합니다.
    # 게터
    @property
    def radius(self):
        return self.__radius
    # 세터
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value

# 원의 둘레와 넓이를 구합니다.
print("# 데코레이터를 사용한 Getter와 Setter")
circle = Circle(10)
print("원래 원의 반지름:", circle.radius)
# 자동으로 세터함수가 호출되어 radius 값을 변경합니다.
circle.radius = 2
# 자동으로 게터함수가 호출되어 radius 값을 반환합니다.
print("변경된 원의 반지름:", circle.radius)
print()

# 강제로 예외를 발생시킵니다.
print("# 강제로 예외를 발생시킵니다.")
circle.radius = -10