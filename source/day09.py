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

# # 리스트를 선언합니다.
# array = ["사과", "자두", "초콜릿", "바나나", "체리"]
# output = [fruit for fruit in array if fruit != "초콜릿"]

# # 출력합니다.
# print(output)

# # 변수를 선언합니다.
# number = int(input("정수 입력> "))

# # if 조건문으로 홀수 짝수를 구분합니다.
# if number % 2 == 0:
#     print("""\
#         입력한 문자열은 {}입니다.
#         {}는(은) 짝수입니다.""".format(number, number))
# else:
#     print("""\
#         입력한 문자열은 {}입니다.
#         {}는(은) 홀수입니다.""".format(number, number))

# # 변수를 선언합니다.
# test = (
#     "이렇게 입력해도 "
#     "하나의 문자열로 연결되어 "
#     "생성됩니다."
# )

# # 출력합니다.
# print("test:", test)
# print("type(test):", type(test))

# # 변수를 선언합니다.
# number = int(input("정수 입력> "))

# # if 조건문으로 홀수 짝수를 구분합니다.
# if number % 2 == 0:
#     print((
#         "입력한 문자열은 {}입니다.\n"
#         "{}는(은) 짝수입니다."
#     ).format(number, number))
# else:
#     print((
#         "입력한 문자열은 {}입니다.\n"
#         "{}는(은) 홀수입니다."
#     ).format(number, number))

# if number % 2 == 0:
#     print("\n".join([
#         "입력한 문자열은 {}입니다.",
#         "{}는 짝수입니다."
#     ]).format(number, number))
# else:
#     print("\n".join([
#         "입력한 문자열은 {}입니다.",
#         "{}는 홀수입니다."
#     ]).format(number, number))

# 변수를 선언합니다.
numbers = [1,2,3,4,5,6]
r_num = reversed(numbers)

# reversed_numbers 를 출력합니다.
print("reversed_numbers :", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))