# 자식 클래스로써 부모의 함수 재정의(오버라이드) 하기
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("##### 내가 만든 오류가 생성되었어요! #####")
    # 부모에 정의되어 있는 함수를 자식에서 다시 정의하는 것(재정의, 오버라이드)
    def __str__(self):
        return "오류가 발생했어요"

raise CustomException