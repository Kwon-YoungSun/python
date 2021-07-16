# import random
# print("# random 모듈")

# # random(): 0.0 <= x < 1.0 사이의 float를 리턴합니다.
# print("- random():", random.random())

# # uniform(min, max): 지정한 범위 사이의 float를 리턴합니다.
# print("- uniform(10, 20):", random.uniform(10, 20))

# # randrange(): 지정한 범위의 int를 리턴합니다.
# # - randrange(max): 0부터 max 사이의 값을 리턴합니다.
# # - randrange(min, max): min부터 max 사이의 값을 리턴합니다.
# print("- randrange(10):", random.randrange(10))

# # choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택합니다.
# print("- choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))

# # shuffle(list): 리스트의 요소들을 랜덤하게 섞습니다.
# print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))

# # sample(list, k=<숫자>): 리스트의 요소 중에 k개를 뽑습니다.
# print("- sample([1, 2, 3, 4, 5]), k=2):", random.sample([1, 2, 3, 4, 5], k=2))


# ---------------------------------------------------------------------------------------
# # sys 모듈
# # 모듈을 읽어 들입니다.
# import sys

# # 명령 매개변수를 출력합니다
# print(sys.argv)
# print("---")

# # 컴퓨터 환경과 관련된 정보를 출력합니다.
# print("getwindowsversion:()", sys.getwindowsversion())
# print("---")
# print("copyright:", sys.copyright)
# print("---")
# print("version:", sys.version)

# # 프로그램을 강제로 종료합니다.
# sys.exit()

# -------------------------------------------------------------------------------------------------------------------------

# # os 모듈 : 운영체제와 관련된 기능을 가진 모듈로, 새로운 폴더를 만들거나 폴더 내부의 파일 목록을 보는 일을 할 때 활용함
# # 모듈을 읽어 들입니다.
# import os

# # 기본 정보를 몇 개 출력해 봅시다.
# print("현재 운영체제:", os.name)
# print("현재 폴더:", os.getcwd())
# print("현재 폴더 내부의 요소:", os.listdir())

# # 폴더를 만들고 제거합니다[폴더가 비어있을 때만 제거 가능]
# os.mkdir("hello")
# os.rmdir("hello")

# # 파일을 생성하고 + 파일 이름을 변경합니다.
# with open("original.txt", "w") as file:
#     file.write("hello")
# os.rename("original.txt", "new.txt")

# # 파일을 제거합니다.
# os.remove("new.txt")
# # os.unlink("new.txt")    # remove와 unlink는 같은 기능을 가진 함수이고 이름만 다를 뿐이다.

# # 시스템 명령어 실행
# os.system("dir")

# -------------------------------------------------------------------------------------------------------------------------
# # datetime 모듈
# # 모듈을 읽어 들입니다.
# import datetime

# # 현재 시각을 구하고 출력하기
# print("# 현재 시각 출력하기")
# now = datetime.datetime.now()
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")
# print()

# # 시간 출력 방법
# print("# 시간을 포맷에 맞춰 출력하기")
# output_a = now.strftime("%Y.%m.%d %H:%M:%S")
# output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
#     now.month,\
#     now.day,\
#     now.hour,\
#     now.minute,\
#     now.second)
# output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")    # strftime(): 시간을 형식에 맞춰 출력
# print(output_a)
# print(output_b)
# print(output_c)
# print()

# -------------------------------------------------------------------------------------------------------------------------
# # datetime 모듈
# # 모듈을 읽어 들입니다.
# import datetime
# now = datetime.datetime.now()

# # 특정 시간 이후의 시간 구하기
# print("# datetime.timedelta로 시간 더하기")

# # timedelta() 함수를 사용하면 특정한 시간의 이전 또는 이후를 구할 수 있다.
# # timedelta() 함수는 1년 후, 2년 후 등의 몇 년후를 구하는 기능이 없다.
# # 따라서 1년 후를 구할 때는 replace() 함수를 사용해 아예 날짜 값을 교체하는 것이 일반적이다.
# after = now + datetime.timedelta(\
#     weeks=1,\
#     days=1,\
#     hours=1,\
#     minutes=1,\
#     seconds=1)
# print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
# print()

# # 특정 시간 요소 교체하기
# print("# now.replace()로 1년 더하기")
# output = now.replace(year=(now.year + 1))
# print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
# -------------------------------------------------------------------------------------------------------------------------

# # time 모듈
# import time

# print("지금부터 5초 동안 정지합니다!")
# time.sleep(5)
# print("프로그램을 종료합니다")

# -------------------------------------------------------------------------------------------------------------------------

# # urllib 모듈
# # 모듈을 읽어 들입니다.
# from urllib import request

# # urlopen() 함수로 구글의 메인 페이지를 읽습니다.
# target = request.urlopen("https://google.com")
# output = target.read()

# # 출력합니다.
# print(output)

# -------------------------------------------------------------------------------------------------------------------------
# 7-1 확인문제 3-1
# # 모듈을 읽어 들입니다.
# import os

# # 현재 폴더의 파일/폴더를 출력합니다.
# output = os.listdir(".")
# print("os.listdir():", output)
# print()

# # 현재 폴더의 파일/폴더를 구분합니다.
# print("# 폴더와 파일 구분하기")
# for path in output:
#     if os.path.isdir(path):
#         print("폴더:", path)
#     else:
#         print("파일:", path)

# -------------------------------------------------------------------------------------------------------------------------
# 7-1 확인문제 3-2

# 모듈을 읽어 들입니다.
import os

# # 폴더를 읽어 들이는 함수
# def read_folder(path):
#     print("---------------------------------- 재귀함수 작동..!!")
#     print("*** " + path + "내의 파일과 폴더 구하기")
#     # 폴더의 요소 읽어 들이기
#     output = os.listdir(path)
#     print(path + "내의 요소 : " + str(output))
#     # 폴더의 요소 구분하기
#     for item in output:
#         if os.path.isdir(path + "/" + item):
#             print(item + " 는 폴더입니다.")
#             # 폴더라면 계속 읽어 들이기
#             read_folder(path+"/"+item)
#         else:
#             # 파일이라면 출력하기
#             print("파일:", item)

# # 현재 폴더의 파일/폴더를 출력합니다.
# read_folder(".")


## 다른 방법
# 폴더를 읽어 들이는 함수
def read_folder(path):
#    print("---------------------------------- 재귀함수 작동..!!")
#    print("*** " + path + "내의 파일과 폴더 구하기")
    # 폴더의 요소 읽어 들이기
    output = os.listdir(path)
#    print(path + "내의 요소 : " + str(output))
    # 폴더의 요소 구분하기
    for item in output:
        if os.path.isdir(path + "/" + item):
            print("******************************************************************************")
            print(path + "/" + item + "(dir)")
            # 폴더라면 계속 읽어 들이기
            read_folder(path+"/"+item)
        else:
            # 파일이라면 출력하기
            print("파일:", item)

# 현재 폴더의 파일/폴더를 출력합니다.
read_folder(".")