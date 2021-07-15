# # 리스트를 선언합니다.
# list_a = [1,2,3]
# list_b = [4,5,6]

# # 출력합니다.
# print("# 리스트")
# print("list_a =", list_a)
# print("list_b =", list_b)
# print()

# # 기본 연산자
# print("# 리스트 기본 연산자")
# print("list_a + list_b =", list_a + list_b)
# print("list_a * 3 =", list_a * 3)
# print()

# # 함수
# print("# 길이 구하기")
# print("len(list_a) =", len(list_a))

# # 리스트를 선언합니다.
# list_a = [1,2,3]

# # 리스트 뒤에 요소 추가하기
# print("# 리스트 뒤에 요소 추가하기")
# list_a.append(4)
# list_a.append(5)

# print(list_a)
# print()

# # 리스트 중간에 요소 추가하기
# print("# 리스트 중간에 요소 추가하기")
# list_a.insert(0, 10)
# print(list_a)

# list_a = [0,1,2,3,4,5]
# print("# 리스트의 요소 하나 제거하기")

# # 제거 방법[1] - del
# del list_a[1]
# print("del list_a[1]:", list_a)

# # 제거 방법[2] - pop()
# list_a.pop(2)
# print("pop(2):", list_a)

# # 리스트를 선언합니다.
# array = [273, 32, 103, 57, 52]

# # 리스트에 반복문을 적용합니다.
# for element in array:
#     # 출력합니다.
#     print(element)

# for character in "안녕하세요":
#     print("-", character)

# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# for num in numbers:
#     if num % 2 == 0:
#         print("{:d} 는 짝수입니다.".format(num))
#     else:
#         print("{:d} 는 홀수입니다.".format(num))

# for num in numbers:
#     if num / 100 >= 1:
#         print("{:d} 는 {:3d} 자릿수입니다.".format(num, 3))
#     elif num / 10 >= 1:
#         print("{:d} 는 {:3d} 자릿수입니다.".format(num, 2))
#     else:
#         print("{:d} 는 {:3d} 자릿수입니다.".format(num, 1))

# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[], [], []]

# for number in numbers:
#     output[(number-1) % len(output)].append(number)

# print(output)

# 딕셔너리를 선언합니다.
# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin": "필리핀"
# }

# # 출력합니다.
# print("name:", dictionary["name"])
# print("type:", dictionary["type"])
# print("ingredient:", dictionary["ingredient"])
# print("origin:", dictionary["origin"])
# print()

# # 값을 변경합니다.
# dictionary["name"] = "8D 건조 망고"
# print("name:", dictionary["name"])

# # 딕셔너리를 선언한다.
# dictionary = {}

# # 요소 추가 전에 내용을 출력해 준다.
# print("요소 추가 이전: ", dictionary)

# # 딕셔너리에 요소를 추가한다.
# dictionary["name"] = "새로운 이름"
# dictionary["head"] = "새로운 정신"
# dictionary["body"] = "새로운 몸"

# # 출력한다.
# print("요소 추가 이후:", dictionary)

# # 딕셔너리를 선언한다.
# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임"
# }

# # 요소 제거 전에 내용을 출력해 준다.
# print("요소 제거 이전:", dictionary)

# # 딕셔너리의 요소를 제거한다.
# del dictionary["name"]
# del dictionary["type"]

# # 요소 제거 후에 내용을 출력해 준다.
# print("요소 제거 이후: ", dictionary)

# # 사용자로부터 입력을 받습니다.
# key = input("> 접근하고자 하는 키: ")

# # 출력합니다.
# if key in dictionary:
#     print(dictionary[key])
# else:
#     print("존재하지 않는 키에 접근하고 있습니다.")

# # 존재하지 않는 키에 접근해 봅니다.
# value = dictionary.get("존재하지 않는 키")
# print("값:", value)

# # None 확인 방법
# if value == None:
#     print("존재하지 않는 키에 접근했습니다.")

# # for 반복문을 사용합니다.
# for key in dictionary:
#     # 출력합니다.
#     print(key, ":", dictionary[key])

# # 딕셔너리의 리스트를 선언합니다.
# pets = [
#     {"name": "구름", "age": 5},
#     {"name": "초코", "age": 3},
#     {"name": "아지", "age": 1},
#     {"name": "호랑이", "age": 1}
# ]

# print("# 우리 동네 애완 동물들")
# for row in pets:
#     print(row.get("name"), " ", row.get("age"), "살")

# # 숫자는 무작위로 입력해도 상관 없습니다.
# numbers = [1,2,4,5,6,5,6,4,8]
# counter = {}

# for number in numbers:
#     if number in counter:
#         counter[number] += 1
#     else:
#         counter[number] = 1

# # 최종 출력
# print(counter)

# # 딕셔너리를 선언합니다.
# character = {
#     "name": "기사",
#     "level": 12,
#     "items": {
#         "sword": "불꽃의 검",
#         "armor": "풀플레이트"
#     },
#     "skill": ["베기", "세게 베기", "아주 세게 베기"]
# }

# # for 반복문을 사용합니다.
# for key in character:
#     if type(character[key]) is list:
#         for i in range(len(character[key])):
#             print(key, ":", character[key][i]) 
#     elif type(character[key]) is dict:
#         for item in character[key]:
#             print(item, ":", character[key].get(item))
#     else:
#         print(key, ":", character[key])

# def print_3_times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")

# print_3_times()

# print()
# def print_n_times(value, n):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요")

# 함수를 호출합니다.

# def print_n_times(n, *values):
#     # n번 반복합니다.
#     for i in range(n):
#         # values는 리스트처럼 활용합니다.
#         for value in values:
#             print(value)
#         # 단순한 줄바꿈
#         print()

# # 함수를 호출합니다.
# print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

# def print_n_times(*values, n=2):
#     # n번 반복합니다.
#     for i in range(n):
#         # values는 리스트처럼 활용합니다.
#         for value in values:
#             print(value)
#         # 단순한 줄바꿈
#         print()

# # 함수를 호출합니다.
# print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)

# def test(a, b=10, c=100):
#     print(a + b + c)

# # 1) 기본 형태
# test(10, 20, 30)

# # 2) 키워드 매개변수로 모든 매개변수를 지정한 형태
# test(a=10, b=100, c=200)

# # 3) 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
# test(c=10, a=100, b=200)

# # 4) 키워드 매개변수로 일부 매개변수만 지정한 형태
# test(10, c=200)

# # 함수를 선언합니다.
# def sum_all(start, end):
#     # 변수를 선언합니다.
#     output = 0
#     # 반복문을 돌려 숫자를 더합니다.
#     for i in range(start, end + 1):
#         output += i
#     # 리턴합니다.
#     return output

# # 함수를 호출합니다.
# print("0 to 100:", sum_all(0, 100))
# print("0 to 1000:", sum_all(0, 1000))
# print("50 to 100:", sum_all(50, 100))
# print("500 to 1000:", sum_all(500, 1000))

# # 함수를 선언합니다.
# def sum_all(start=0, end=100, step=1):
#     # 변수를 선언합니다.
#     output = 0
#     # 반복문을 돌려 숫자를 더합니다.
#     for i in range(start, end + 1, step):
#         output += i
#     # 리턴합니다.
#     return output

# # 함수를 호출합니다.
# print("A.", sum_all(0, 100, 10))
# print("B.", sum_all(end=100))
# print("C.", sum_all(end=100, step=2))

# 함수를 선언한다.
def 함수이름(매개변수1, 매개변수2, 매개변수3, 매개변수4):
    print("안녕하세요" + str(매개변수1))
    print("안녕하세요" + str(매개변수2))
    return 매개변수1 + 매개변수2 + 매개변수3 + 매개변수4
    print("안녕하세요" + str(매개변수3))
    print("안녕하세요" + str(매개변수4))

# 함수를 호출한다.
print(함수이름(1, 2, 3, 4))