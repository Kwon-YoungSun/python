# example_list = ["요소A", "요소B", "요소C"]
# i = 0
# for item in example_list:
#     print("{}번째 요소는 {}입니다.".format(i, item))
#     i += 1
# for i in range(len(example_list)):
#     print("{}번째 요소는 {}입니다.".format(i, example_list[i]))

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

# # for 반복문과 enumerate() 함수 조합해서 사용하기
# print("# 반복문과 조합하기")
# for i, value in enumerate(example_list):
#     print("{}번째 요소는 {}입니다.".format(i, value))

# # 변수를 선언합니다.
# example_dictionary = {
#     "키A": "값A",
#     "키B": "값B",
#     "키C": "값C",
# }

# # 딕셔너리의 items() 함수 결과 출력하기
# print("# 딕셔너리의 items() 함수")
# print("items():", example_dictionary.items())
# print()

# # for 반복문과 items() 함수 조합해서 사용하기
# print("# 딕셔너리의 items() 함수와 반복문 조합하기")

# for key, element in example_dictionary.items():
#     print("dictionary[{}] = {}".format(key, element))

# 변수를 선언합니다.
array = []

# 반복문을 적용합니다.
for i in range(0, 20, 2):
    array.append(i * i)

# 출력합니다.
print(array)