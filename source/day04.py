# x = 10
# under_20 = x < 20   # True
# print("under_20: ", under_20)
# print("not under_20: ", not under_20)

# # 입력을 받습니다.
# number = input("정수 입력> ")
# number = int(number)

# # 양수 조건
# if number > 0:
#     print("양수입니다.")

# # 음수 조건
# if number < 0:
#     print("음수입니다")

# # 0 조건
# if number == 0:
#     print("0입니다")

# 날짜/시간과 관련된 기능을 가져옵니다.
# import datetime

# 현재 날짜/시간을 구합니다.
# now = datetime.datetime.now()

# # 출력합니다.
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")

# 다른 방법으로 출력합니다.
# print("{}년 {}월 {}일 {}시 {}분 {}초".format(
#     now.year,
#     now.month,
#     now.day,
#     now.hour,
#     now.minute,
#     now.second
# ))

# num = input("정수 입력> ")
# num = int(num)
# if num >= 10:
#     print("num은 두자리 양수이다.")
# else:
#     print("num은 두자리 양수가 아니다.")

# 날짜/시간과 관련된 기능을 가져옵니다.
# import datetime

# # 현재 날짜/시간을 구합니다.
# now = datetime.datetime.now()

# # 오전 구분
# if now.hour < 12:
#     print("현재 시각은 {}로 오전입니다!".format(now.hour))

# # 오후 구분
# if now.hour >= 12:
#     print("현재 시각은 {}시로 오후입니다!".format(now.hour))

# # 봄 구분
# if 3 <= now.month <= 5:
#     print("이번 달은 {}월로 봄입니다!".format(now.month))

# # 여름 구분
# if 6 <= now.month <= 8:
#     print("이번 달은 {}월로 여름입니다!".format(now.month)) 

# # 가을 구분
# if 9 <= now.month <= 11:
#     print("이번 달은 {}월로 여름입니다!".format(now.month)) 

# # 겨울 구분
# if now.month == 12 or 1 <= now.month <= 2:
#     print("이번 달은 {}월로 겨울입니다!".format(now.month))

# # 입력을 받습니다.
# number = input("정수 입력> ")

# # 마지막 자리 숫자를 추출
# last_character = number[-1]

# # 숫자로 변환하기
# last_number = int(last_character)

# # 짝수 확인
# if last_number == 0 \
#     or last_number == 2 \
#     or last_number == 4 \
#     or last_number == 6 \
#     or last_number == 8:
#     print("짝수입니다")

# # 홀수 확인
# if last_number == 1 \
#     or last_number == 3 \
#     or last_number == 5 \
#     or last_number == 7 \
#     or last_number == 9:
#     print("홀수입니다")

# # 입력을 받습니다.
# number = input("정수 입력> ")
# last_character = number[-1]

# # 짝수 조건
# if last_character in "02468":
#     print("짝수입니다")

# # 홀수 조건
# if last_character in "13579":
#     print("홀수입니다")

# a = int(input("> 1번째 숫자: "))
# b = int(input("> 2번째 숫자: "))
# print()

# if a > b:
#     print("처음 입력했던 {}가 {}보다 더 큽니다".format(a, b))
# if a < b:
#     print("두 번째로 입력했던 {}가 {}보다 더 큽니다".format(b, a))

# # 입력을 받습니다.
# number = input("정수 입력> ")
# number = int(number)

# # 조건문을 사용합니다.
# if number % 2 == 0:
#     # 조건이 참일 때, 즉 짝수 조건
#     print("짝수입니다.")
# else:
#     # 조건이 거짓일 때, 즉 홀수 조건
#     print("홀수입니다.")

# # 날짜/시간과 관련된 기능을 가져옵니다.
# import datetime

# # 현재 날짜/시간을 구하고
# # 쉽게 사용할 수 있게 월을 변수에 저장합니다.
# now = datetime.datetime.now()
# month = now.month

# # 조건문으로 계절을 확인합니다.
# if 3 <= month <= 5:
#     print("현재는 봄입니다.")
# elif 6 <= month <= 8:
#     print("현재는 여름입니다.")
# elif 9 <= month <= 11:
#     print("현재는 가을입니다.")
# else:
#     print("현재는 겨울입니다.")

# # 변수를 선언합니다.
# score = float(input("학점 입력> "))

# # 조건문을 적용합니다.
# if score == 4.5:
#     print("신")
# elif 4.2 <= score < 4.5:
#     print("교수님의 사랑")
# elif 3.5 <= score < 4.2:
#     print("현 체제의 수호자")
# elif 2.8 <= score < 3.5:
#     print("일반인")
# elif 2.3 <= score < 2.8:
#     print("일탈을 꿈꾸는 소시민")
# elif 1.75 <= score < 2.3:
#     print("오락문화의 선구자")
# elif 1.0 <= score < 1.75:
#     print("불가촉천민")
# elif 0.5 <= score < 1.0:
#     print("자벌레")
# elif 0 < score < 0.5:
#     print("플랑크톤")
# else:
#     print("시대를 앞서가는 혁명의 씨앗")

# # 변수를 선언합니다.
# score = float(input("학점 입력> "))

# # 조건문을 적용합니다.
# if score == 4.5:
#     print("신")
# elif 4.2 <= score:
#     print("교수님의 사랑")
# elif 3.5 <= score:
#     print("현 체제의 수호자")
# elif 2.8 <= score:
#     print("일반인")
# elif 2.3 <= score:
#     print("일탈을 꿈꾸는 소시민")
# elif 1.75 <= score:
#     print("오락문화의 선구자")
# elif 1.0 <= score:
#     print("불가촉천민")
# elif 0.5 <= score:
#     print("자벌레")
# elif 0 < score:
#     print("플랑크톤")
# else:
#     print("시대를 앞서가는 혁명의 씨앗")

# False로 변환되는 값
# print("# if 조건문에 0 넣기")
# if 0:
#     print("0은 True로 변환됩니다")
# else:
#     print("0은 False로 변환됩니다")
# print()

# print("# if 조건문에 빈 문자열 넣기")
# if "":
#     print("빈 문자열은 True로 변환됩니다")
# else:
#     print("빈 문자열은 False로 변환됩니다")
# print()

# # 입력을 받습니다.
# number = input("정수 입력>")
# number = int(number)

# # 조건문 사용
# if number > 0:
#     # 양수일 때: 아직 미구현 상태입니다.
#     pass
# else:
#     # 음수일 때: 아직 미구현 상태입니다.
#     pass

###############################################
# str_input = input("태어난 해를 입력해 주세요> ")
# birth_year = int(str_input)

# if birth_year % 12 == 0:
#     print("원숭이 띠입니다.")
# elif birth_year % 12 == 1:
#     print("닭 띠입니다.")
# elif birth_year % 12 == 2:
#     print("개 띠입니다.")
# elif birth_year % 12 == 3:
#     print("돼지 띠입니다.")
# elif birth_year % 12 == 4:
#     print("쥐 띠입니다.")
# elif birth_year % 12 == 5:
#     print("소 띠입니다.")
# elif birth_year % 12 == 6:
#     print("범 띠입니다.")
# elif birth_year % 12 == 7:
#     print("토끼 띠입니다.")
# elif birth_year % 12 == 8:
#     print("용 띠입니다.")
# elif birth_year % 12 == 9:
#     print("뱀 띠입니다.")
# elif birth_year % 12 == 10:
#     print("말 띠입니다.")
# elif birth_year % 12 == 11:
#     print("양 띠입니다.")

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

# numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# # for number in numbers:
# #     if number >= 100:
# #         print("- 100 이상의 수:", number)

# # for number in numbers:
# #     if(number % 2 != 0):
# #         print("{}는 홀수입니다.".format(number))
# #     else:
# #         print("{}는 짝수입니다.".format(number))
# holzzak = ['짝수', '홀수']
# for number in numbers:
#     print("{}는 {}입니다.".format(number, holzzak[number % 2]))

# for number in numbers:
#     if(number % 2 != 0):
#         print("{}는 홀수입니다.".format(number))
#     else:
#         print("{}는 짝수입니다.".format(number))

# for number in numbers:
#     if(number // 100 > 0):
#         print("{}는 {}자릿수입니다.".format(number, 3))
#     elif(number // 10 > 0):
#         print("{}는 {}자릿수입니다.".format(number, 2))
#     else:
#         print("{}는 {}자릿수입니다.".format(number, 1))

# list_of_list = [[1,2,3], [4,5,6,7], [8,9]]

# for list in list_of_list:
#     for i in list:
#         print(i)

# numbers = [1,2,3,4,5,6,7,8,9]
# output = [[], [], []]

# for number in numbers:
#     output[(number-1) % 3].append(number)

# print(output)





# 한 번 도전해보기
# 1. 피라미드 만들기
# *
# **
# ***
# ****
# *****

# itor = 5

# for row in range(itor):
#     for col in range(row + 1):
#         print("*", end='')
#     print()

# # 2. 홀수 피라미드 만들기
# itor2 = 101

# for row in range(itor2):
#     if row % 2 == 1:
#         for blank in range(((itor2 - 1) - row) // 2):
#             print(" ", end='')
#         for col in range(row):
#             print("*", end='')
#         print()

# from typing import Dict


# dict = {
#     "키A" : "값A",
#     "키B" : "값B",
#     "키C" : "값C"
# }

# print(dict["키A"])
# print(dict["키B"])
# print(dict["키C"])


# dict2 = {
#     True: False,
#     273: [1,2,3,4]
# }

# print(dict2[True])

# for key in dict:
#     print("{} : {}".format(key, dict[key]))

# print()

# dict["키D"] = "키D"

# for key in dict:
#     print("{} : {}".format(key, dict[key]))

# del dict["키D"]
# print()

# for key in dict:
#     print("{} : {}".format(key, dict[key]))


# # 딕셔너리를 선언합니다.
# dictionary = {
#     "name" : "7D 건조 망고",
#     "type" : "당절임",
#     "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "차지황색소"],
#     "origin" : "필리핀"
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

# # 값을 삭제합니다.
# del dictionary["ingredient"][0]

# for key in dictionary["ingredient"]:
#     print(key)

# # 딕셔너리를 선언합니다.
# dictionary = {}

# # 요소 추가 전에 내용을 출력해 줍니다.
# print("요소 추가 이전:", dictionary)

# # 딕셔너리에 요소를 추가합니다.
# dictionary["name"] = "새로운 이름"
# dictionary["head"] = "새로운 정신"
# dictionary["body"] = "새로운 몸"

# # 출력합니다.
# print("요소 추가 이후:", dictionary)

# # 딕셔너리의 요소를 제거합니다.
# del dictionary["name"]
# del dictionary["head"]

# # 출력합니다.
# print("요소 제거 이후:", dictionary)

# 딕셔너리를 선언합니다.
# dictionary = {
#     "name" : "7D 건조 망고",
#     "type" : "당절임",
#     "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "차지황색소"],
#     "origin" : "필리핀"
# }

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
# for pet in pets:
#     print("{} {}살".format(pet["name"], pet["age"]))

# # 숫자는 무작위로 입력해도 상관 없습니다.
# numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
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
#     "skill": ["베기", "세게 베기","아주 세게 베기"]
# }

# # for 반복문을 사용합니다.
# for key in character:
#     # 문자열인 경우
#     if type(character[key]) is str or type(character[key]) is int:
#         print("{} : {}".format(key, character[key]))
#     # 딕셔너리인 경우    
#     elif type(character[key]) is dict:
#         for weapon in character[key]:
#             print("{} : {}".format(weapon, character[key][weapon]))
#     # 리스트인 경우
#     else:
#         for num in range(len(character[key])):
#             print("{} : {}".format(key, character[key][num]))

# # for 반복문과 범위를 함께 조합해서 사용합니다.
# for i in range(5):
#     print(str(i) + "= 반복 변수")
# print()

# for i in range(5, 10):
#     print(str(i) + "= 반복 변수")
# print()

# for i in range(0, 10, 3):
#     print(str(i) + "= 반복 변수")
# print()

# # 리스트를 선언합니다.
# array = [273, 32, 103, 57, 52]

# i = 0
# for element in array:
#     print("{}번째 반복:{}".format(i, element))
#     i += 1

# print()

# # 역반복문
# for i in range(4, 0 - 1, -1):
#     # 출력합니다.
#     print("현재 반복 변수:{}".format(i))

# print()

# # 반대로 반복하기2
# for i in reversed(range(5)):
#     # 출력합니다.
#     print("현재 반복 변수:{}".format(i))

# # 시간과 관련된 기능을 가져옵니다.
# import time

# # 변수를 선언합니다.
# number = 0

# # 5초 동안 반복합니다.
# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number += 1

# # 출력합니다.
# print("5초 동안 {}번 반복했습니다.".format(number))

# # 변수를 선언합니다.
# i = 0

# # 무한 반복합니다.
# while True:
#     # 몇 번째 반복인지 출력합니다.
#     print("{}번째 반복문입니다.".format(i))
#     i += 1

#     # 반복을 종료합니다.
#     input_text = input("> 종료하시겠습니까?(y/n): ")
#     if input_text in ["y", "Y"]:
#         print("반복을 종료합니다.")
#         break

# # 변수를 선언합니다.
# numbers = [5, 15, 6, 20, 7, 25]

# # 반복을 돌립니다.
# for number in numbers:
#     # number가 10보다 작으면 다음 반복으로 넘어갑니다.
#     if number < 10:
#         continue
#     # 출력합니다.
#     print(number)

# # 숫자는 무작위로 입력해도 상관없습니다.
# key_list = ["name", "hp", "mp", "level"]
# value_list = ["기사", 200, 30, 5]
# character = {}

# for i in range(len(key_list)):
#     character[key_list[i]] = value_list[i]

# # 최종 출력
# print(character)

# limit = 10000
# i = 1

# sum_value = 0
# while sum_value < 10000:
#     sum_value += i
#     i += 1

# print("{}를 더할 때 {}를 넣으며 그때의 값은 {}입니다.".format(i-1, limit, sum_value))

# max_value = 0
# a = 0
# b = 0

# for i in range(1, 100, 1):   # 곱할 수 지정
#     j = 100 - i

#     # 최댓값 구하기
#     if (i*j) > max_value:
#         a = i
#         b = j
#         max_value = i * j

# # 리스트를 선언하고 뒤집습니다.
# list_a = [1,2,3,4,5]
# list_reversed = reversed(list_a)

# # 출력합니다.
# print("# reversed() 함수")
# print("reversed([1,2,3,4,5]):", list_reversed)
# print("list(reversed([1,2,3,4,5])):", list(list_reversed))
# print()

# # 반복문을 적용해 줍니다.
# print("# reversed() 함수와 반복문")
# print("for i in reversed([1,2,3,4,5]):")
# for i in reversed(list_a):
#     print("-", i)

# # 변수를 선언합니다.
# example_list = ["요소A", "요소B", "요소C"]

# # 그냥 출력합니다.
# print("# 단순 출력")
# print(example_list)
# print()

# # enumerate() 함수를 적용해 출력합니다.
# print("# enumerate() 함수 적용 출력")
# print(enumerate(example_list))
# print()

# # list() 함수로 강제 변환해 출력합니다.
# print("# list() 함수로 강제 변환 출력")
# print(list(enumerate(example_list)))
# print()

# # for 반복문과 enumerate() 함수 조합해서 사용하기
# print("# 반복문과 조합하기")
# for i, value in enumerate(example_list):
#     print("{}번째 요소는 {}입니다.".format(i, value))

# # 변수를 선언합니다.
# example_dictionary = {
#     "키A" : "값A",
#     "키B" : "값B",
#     "키C" : "값C"
# }

# # 딕셔너리의 items() 함수 결과 출력하기
# print("# 딕셔너리의 items() 함수")
# print("items():", example_dictionary.items())
# print()

# # for 반복문과 items() 함수 조합해서 사용하기
# print("# 딕셔너리의 items() 함수와 반복문 조합하기")

# for key, element in example_dictionary.items():
#     print("dictionary[{}] = {}".format(key, element))

# # 변수를 선언합니다.
# array = []

# # 반복문을 적용합니다.
# for i in range(0, 20, 2):
#     array.append(i * i)
# # 출력합니다.
# print(array)

# # 리스트를 선언합니다.
# array = [i * i for i in range(0, 20, 2)]

# # 출력합니다.
# print(array)
# 리스트를 선언합니다.
# array = ["사과", "자두", "초콜릿", "바나나", "체리"]
# output = [fruit for fruit in array if fruit != "초콜릿"]

# # 출력합니다.
# print(output)

# 리스트 내포를 사용해본 코드입니다.
output = [num for num in range(1, 100) if "{:b}".format(num).count("0") == 1]

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))