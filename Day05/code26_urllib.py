# urllib 패키지 불러오기
from urllib.request import Request, urlopen
req=Request('https://www.naver.com')#생성자
res=urlopen(req)
print(res.status)#200출력시 url 제대로 들어감 / 404출력시 잘못된 url
