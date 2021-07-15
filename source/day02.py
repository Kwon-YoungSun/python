# print("이름\t나이\t지역")
# print("권영선\t23\t수지구")
# print("권영선\t23\t수지구")
# print("권영선\t23\t수지구")

# print("\\ \\ \\ \\")

# print("""동해물과 백두산이 마르고 닳도록
# 하느님이 보우하사 우리나라 만세
# 무궁화 삼천리 화려강산 대한사람
# 대한으로 길이 보전하세""")

# print()

# print("""\
# 동해물과 백두산이 마르고 닳도록
# 하느님이 보우하사 우리나라 만세
# 무궁화 삼천리 화려강산 대한사람
# 대한으로 길이 보전하세\
# """)

# print("문자 선택 연산자")
# print("안녕하세요"[0])
# print("안녕하세요"[1])
# print("안녕하세요"[2])
# print("안녕하세요"[3])
# print("안녕하세요"[4])

# print()

# print("안녕하세요"[-1])
# print("안녕하세요"[-2])
# print("안녕하세요"[-3])
# print("안녕하세요"[-4])
# print("안녕하세요"[-5])

# print()

# print("# 연습 문제")
# print("\\\\\\\\")
# print("-" * 8)

# print()

# print("안녕하세요"[1:3])
# print("안녕하세요"[2:4])
# print("안녕하세요"[1:])
# print("안녕하세요"[:3])

##############################################################################

# pi = 3.14159265
# r = 10
# print("원주율 = ", pi)
# print("반지름 = ", r)
# print("원의 둘레 = ", pi * r * 2)
# print("원의 넓이 = ", pi * r * r)

# number = 100
# number **= 10

# 입력을 받습니다.
#string = input("입력 > ")

# 출력합니다.
# print("자료 : ", string)
# print("자료형 : ", type(string))

# string_a = input("입력A> ")
# int_a = int(string_a)

# string_b = input("입력B> ")
# int_b = int(string_b)

# print("문자열 자료 : ", string_a + string_b)
# print("숫자 자료 : ", int_a + int_b)

# output_a = str(52)
# output_b = str(52.273)
# print(type(output_a), output_a)
# print(type(output_b), output_b)

# str_input = input("숫자 입력> ")
# num_input = int(str_input)

# print()
# print(num_input, "inch")
# print((num_input * 2.54), "cm")

# str_input = input("원의 반지름 입력>")
# num_input = float(str_input)
# print()
# print("반지름 : ", num_input)
# print("둘레 : ", 2 * 3.14 * num_input)
# print("넓이 : ", 3.14 * num_input ** 2)

# sinput = input("문자열 입력>")
# sinput2 = input("문자열 입력>")
# print(sinput, sinput2)
# temp = ''

# temp = sinput2
# sinput2 = sinput
# sinput = temp
# print(sinput, sinput2)

# format_a = "{}만 원".format(5000)
# format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
# format_c = "{} {} {}".format(3000, 4000, 5000)
# format_d = "{} {} {}".format(1, "문자열", True)

# # 출력하기
# print(format_a)
# print(format_b)
# print(format_c)
# print(format_d)

# 정수
output_a = "{:d}".format(52)

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

# 빈칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)

# format() 함수로 숫자를 문자열로 변환하기
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

# 출력하기
print(format_a)
print(format_b)
print(format_c)
print(format_d)