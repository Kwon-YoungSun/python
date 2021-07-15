# # 리스트를 선언하고 뒤집는다.
# list_a = [1,2,3,4,5]
# list_reversed = reversed(list_a)

# # 출력한다.
# print("# reversed() 함수")
# print("reversed([1,2,3,4,5]):", list_reversed)
# print("list(reversed([1,2,3,4,5]))", list(list_reversed))
# print()

# # 반복문을 적용해 본다.
# print("# reversed() 함수의 반복문")
# print("for i in reversed([1,2,3,4,5]):")
# for i in reversed(list_a):
#     print("-", i)

# temp = reversed([1,2,3,4,5,6])

# for i in temp:
#     print("첫 번째 반복문: {}".format(i))

# for i in temp:
#     print("두 번째 반복문: {}".format(i))

numbers = [1,2,3,4,5,6]

for i in reversed(numbers):
    print("첫 번째 반복문: {}".format(i))

for i in reversed(numbers):
    print("두 번째 반복문: {}".format(i))