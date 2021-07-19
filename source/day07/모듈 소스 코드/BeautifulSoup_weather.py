# 모듈을 읽어 들입니다.
from urllib import request      # URL을 다루는 라이브러리
from bs4 import BeautifulSoup   # HTML 문자열과 "html.parser"라는 문자열을 넣으면 BeautifulSoup이라는 특수한 객체 리턴

# urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# BeautifulSoup를 사용해 웹페이지를 분석한다.
soup = BeautifulSoup(target, "html.parser")

# location 태그를 찾습니다.
for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()