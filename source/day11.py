# def print_3_times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")

# print_3_times()

# def print_n_times(value, n):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요", 5)

# print()

# def print_n_times(value, n=2):
#     # n번 반복합니다.
#     for i in range(n):
#         print(value)

# # 함수를 호출합니다.
# print_n_times("안녕하세요")

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

# # 함수를 정의합니다.
# def return_test():
#     print("A 위치입니다.")
#     return  # 리턴합니다.
#     print("B 위치입니다.")

# # 함수를 호출합니다.
# return_test()

# def return_test2():
#     return "리턴!!!"

# value = return_test2()
# print(value)

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

# def f(x):
#     return x
# print(f(10))

# def f(x):
#     return x**2 + 2*x + 1
# print(f(10))

def mul(*values):
    result = 1
    for value in values:
        result *= value
    return result

# 함수를 호출합니다.
print(mul(5, 7, 9, 10))