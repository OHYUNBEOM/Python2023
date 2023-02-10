# Python2023
부경대_IOT

## 1일차
1. 기본구성
    - Git/Github 설치 및 연동
    - Visual Studio Code 설치 및 연동
    - Python 설치
2. 파이썬 기본
    - 콘솔 출력
    - 주석



```python
# desc : 콘솔출력 
print('vsc 설정 단축키는 ctrl + , 입니다')
print('Hello Python')
```

## 2일차
1. 파이썬 기본
    - 변수
    - 자료형
    - 연산자
    
```python
full_name='Oh Yun Beom'
age=26
print(f"Hello I'm {full_name}, and I'm {age:2.0f} ages.")
# 출력 결과 : Hello I'm Oh Yun Beom, and I'm 26 ages.
int1=1566.555555
print(f"{int1:2.2f}")
print(f"{int1:1.3f}")
print(f"{int1:3.4f}")
# 출력 결과 : 
# 1566.56
# 1566.556
# 1566.5556
```

## 3일차
1. 파이썬 기본
    - 흐름제어
        - if
        - for(별찍기)
        - while
    - 구구단 
    - 함수
    
## 4일차
1. 파이썬 기본
    - 가상환경
    - 객체지향 OOP
        - class
        ```python
        # 생성자
        def __init__(self,number='15더 8117') -> None:
        print('생성자 생성')
        self.__number=number
        ```
    - 패키지

## 5일차
1. 파이썬 기본
    - 패키지
    - 입/출력
    ```python
    inputs=list(map(int,input('정수 입력> ').split()))
    print(inputs)
    ```
    - 예외처리

## 6일차
1. 파이썬 기본
    - 콘솔출력 보충
    - 객체지향 
        - 객체지향 특징
        - 상속, 다중 상속
2. 파이썬 응용
    - 주소록 프로그램 [SourceCode](https://github.com/OHYUNBEOM/Python2023/blob/main/Project/address_app.py)

실행화면 -> 
![실행화면](https://github.com/OHYUNBEOM/Python2023/blob/main/images/%EC%8B%A4%ED%96%89%ED%99%94%EB%A9%B4.png?raw=true)


## 7일차
1. 파이썬 응용
    - 주피터 노트북 사용법
    - List 연산 추가
    - 라이브러리 사용법
        - folium(지도 라이브러리)

## 8일차
1. 파이썬 응용
    - 라이브러리 사용법
        - urllib.request
    - 웹 크롤링 [SourceCode](https://github.com/OHYUNBEOM/Python2023/blob/main/Day08/code44_web_crawling_tutorial.ipynb)
        - 기상청 오늘의 날씨 크롤링
        - 데이터포털 OpenAPI 크롤링
        - BeautifulSoup 크롤링

![실행화면](https://raw.githubusercontent.com/OHYUNBEOM/Python2023/main/images/jupyter_folium.png)

### Folium OpenAPI 연동

## 9일차
1. 파이썬 응용
    - GUI 개발
        - Tkinter 
        - PyQt 소개,설치
        - PyQt 기본 사용법
        - PyQt 위젯

## 10일차
1. 파이썬 응용
    -GUI 개발
        -PyQt 위젯