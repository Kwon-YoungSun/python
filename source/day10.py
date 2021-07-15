# # 리스트 내포를 사용해본 코드입니다.
# output = [num for num in range(1, 100+1) 
#             if "{:b}".format(num).count("0") == 1]

# for i in output:
#     print("{} : {}".format(i, "{:b}".format(i)))

# print("합계:", sum(output))

# # 리스트 내포를 사용해본 코드입니다.
# output = [num for num in range(1, 100+1)]

# for i in output:
#     print("{} : {} | {}".format(i, "{:b}".format(i), bin(i)))

# print("합계:", sum(output))

# def print_3_times():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")

# print_3_times()

# def print_n_times(value, n):
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요", 5)

def print_n_times(n, *values):
    # n번 반복합니다.
    for i in range(n):
        # values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        # 단순한 줄바꿈
        print()

# 함수를 호출합니다.    
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")