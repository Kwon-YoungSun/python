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
# # 리스트에 반복문을 적용합니다.
# for element in array:
#     # 출력합니다.
#     print(element)

# # 리스트를 선언합니다.
# array = [273, 32, 103, 57, 52]

# # 리스트에 반복문을 적용합니다.
# for i in range(len(array)):
#     # 출력합니다.
#     print("{}번째 반복: {}".format(i, array[i]))

# # 역반복문
# for i in range(4, 0-1, -1):
#     # 출력합니다.
#     print("현재 반복 변수: {}".format(i))

# for i in reversed(range(5)):
#     # 출력합니다.
#     print("현재 반복 변수: {}".format(i))

# # while 반복문을 사용합니다.
# while True:
#     # "."을 출력합니다.
#     # 기본적으로 end가 "\n"이라 줄바꿈이 일어나는데
#     # 빈 문자열 ""로 바꿔서 줄바꿈이 일어나지 않게 됩니다.
#     print(".", end="")

# # 반복 변수를 기반으로 반복하기
# i = 0
# while i < 10:
#     print("{}번째 반복입니다.".format(i))
#     i += 1

# while 반복문: 시간을 기반으로 반복하기
# # 시간과 관련된 기능을 가져온다.
# import time

# # 변수를 선언한다.
# number = 0

# # 5초 동안 반복한다.
# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number += 1

# # 출력한다.
# print("5초 동안 {}번 반복했습니다.".format(number))

# # 변수를 선언한다.
# i = 0

# # 무한 반복한다.
# while True:
#     # 몇 번째 반복인지 출력한다.
#     print("{}번째 반복문입니다.".format(i))
#     i = i + 1
#     # 반복을 종료한다.
#     input_text = input("> 종료하시겠습니까?(y/n): ")
#     if input_text in ["y", "Y"]:
#         print("반복을 종료합니다.")
#         break

# # 변수를 선언한다.
# numbers = [5, 15, 6, 20, 7, 25]

# # 반복을 돌린다.
# for number in numbers:
#     # number가 10보다 작으면 다음 반복으로 넘어간다.
#     if number < 10:
#         continue
#     # 출력합니다.
#     print(number)

# # 숫자는 무작위로 입력해도 상관없습니다.
# key_list = ["name", "hp", "mp", "level"]
# value_list = ["기사", 200, 30, 5]
# character = {}

# for i in range(0,4):
#     character[key_list[i]] = value_list[i]

# # 최종 출력
# print(character)

# limit = 10000
# i = 1
# # sum은 파이썬 내부에서 사용하는 식별자이므로 sum_value 라는 변수 이름을 사용합니다.
# sum_value = 0
# while sum_value < limit:
#     sum_value += i
#     i += 1

# print("{}를 더할 때 {}를 넘으며 그때의 값은 {} 입니다.".format(i-1, limit, sum_value))

max_value = 0
a = 0
b = 0

for i in range(1, 100):
    j = 100 - i

    # 최댓값 구하기
    if max_value < (i * j):
        max_value = i * j
        a = i
        b = j

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))