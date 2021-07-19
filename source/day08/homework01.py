# 주어진 페이스북의 객체를 바탕으로 클래스를 생성하고, 페이스북에 등록된 회원정보를 꺼내는 프로그램을 작성하시오.

# 멤버 클래스를 선언합니다.
class Member:
    def __init__(self, name, email, age, gen):
        self.name = name
        self.email = email
        self.age = age
        self.gen = gen

    def to_string(self):
        return "{}\t{}\t{}\t{}".format(self.name, self.email, self.age, self.gen)

# 멤버 리스트를 선언합니다.
members = [
    Member("권영선", "sun@ssu.ac.kr", 23, "F"),
    Member("서솔미", "sol@ssu.ac.kr", 27, "F"),
    Member("민진선", "minj@ssu.ac.kr", 28, "F"),
    Member("박정우", "woo@ssu.ac.kr", 29, "M"),
    Member("신영훈", "syh@ssu.ac.kr", 27, "M")
]

# 멤버를 한 명씩 반복합니다.
print("이름", "메일", "나이", "성별", sep="\t")

for member in members:
# 출력합니다.
    print(member.to_string())