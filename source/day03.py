# # 정수
# output_a = "{:d}".format(52)

# # 특정 칸에 출력하기
# output_b = "{:5d}".format(52)       # 5칸
# output_c = "{:10d}".format(52)      # 10칸

# # 빈칸을 0으로 채우기
# output_d = "{:05d}".format(52)      # 양수
# output_e = "{:05d}".format(-52)     # 음수

# print("#기본")
# print(output_a)
# print("# 특정 칸에 출력하기")
# print(output_b)
# print(output_c)
# print("# 빈칸을 0으로 채우기")
# print(output_d)
# print(output_e)

# # 기호와 함께 출력하기
# output_f = "{:+d}".format(52)   # 양수
# output_g = "{:+d}".format(-52)  # 음수
# output_h = "{: d}".format(52)   # 양수 : 기호 부분 공백
# output_i = "{: d}".format(-52)  # 음수 : 기호 부분 공백

# print("# 기호와 함께 출력하기")
# print(output_f)
# print(output_g)
# print(output_h)
# print(output_i)

# # 조합하기
# output_h = "{:+5d}".format(52)
# output_i = "{:+5d}".format(-52)
# output_j = "{:=+5d}".format(52)
# output_k = "{:=+5d}".format(-52)
# output_l = "{:+05d}".format(52)
# output_m = "{:+05d}".format(-52)

# print("# 조합하기")
# print(output_h)
# print(output_i)
# print(output_j)
# print(output_k)
# print(output_l)
# print(output_m)

# output_a = "{:f}".format(52.273)
# output_b = "{:15f}".format(52.273)      # 15칸 만들기
# output_c = "{:+15f}".format(52.273)     # 15칸에 부호 추가하기
# output_d = "{:+015f}".format(52.273)    # 15칸에 부호 추가하고 0으로 채우기

# print(output_a)
# print(output_b)
# print(output_c)
# print(output_d)

## 소수점 아래 자릿수 지정하기
# output_a = "{:15.3f}".format(52.273)
# output_b = "{:15.2f}".format(52.273)
# output_c = "{:15.1f}".format(52.273)

# print(output_a)
# print(output_b)
# print(output_c)

# 의미 없는 소수점 제거하기
# output_a = 52.0
# output_b = "{:g}".format(output_a)
# print(output_a)
# print(output_b)

# a = input("> 1번째 숫자: ")
# b = input("> 2번째 숫자: ")
# print()

# print("{} + {} = {}".format(a, b, int(a) + int(b)))

# string = "hello"

# # string.upper()를 실행하고, string 출력하기
# string.upper()
# print("A 지점: ", string)

# # string.upper() 실행하기
# print("B 지점: ", string.upper())

# print("# if 조건문에 0 넣기")
# if 0:
#     print("0은 True로 반환됩니다.")
# else:
#     print("0은 False로 반환됩니다.")

# print("# if 조건문에 빈 문자열 넣기")
# if "":
#     print("빈 문자열은 True로 반환됩니다.")
# else:    
#     print("빈 문자열은 False로 반환됩니다.")


# # 입력을 받습니다.
# number = input("정수 입력> ")
# number = int(number)

# # 조건문 사용
# if number > 0:
#     pass
# else:
#     pass

# x = 10
# y = 2
# if x > 4:
#     if y > 2:
#         print(x * y)
# else:
#     print(x + y)

str_input = input("태어난 해를 입력해 주세요.> ")
birth_year = int(str_input)

if birth_year % 12 == 0:
    print("원숭이 띠입니다.")
if birth_year % 12 == 1:
    print("닭 띠입니다.")
if birth_year % 12 == 2:
    print("개 띠입니다.")
if birth_year % 12 == 3:
    print("돼지 띠입니다.")
if birth_year % 12 == 4:
    print("쥐 띠입니다.")
if birth_year % 12 == 5:
    print("소 띠입니다.")
if birth_year % 12 == 6:
    print("호랑이 띠입니다.")
if birth_year % 12 == 7:
    print("토끼 띠입니다.")
if birth_year % 12 == 8:
    print("용 띠입니다.")
if birth_year % 12 == 9:
    print("뱀 띠입니다.")
if birth_year % 12 == 10:
    print("말 띠입니다.")
if birth_year % 12 == 11:
    print("양 띠입니다.")