#연산자
#할당연산
print(2==1)

#숫자연산
print(2**10) # 2^10
print(type(10//3))
print(type(10/3))

#문자열 연산
str1 = 'Hello'
str2 = 'World!'
full_str=str1+' '+str2
print(full_str)

print(str1*3)

print(len(str1))
print(len(full_str))

#list 자르기

print()
current = '2023-01-31 15:00:00'
year=current[:4]
month=current[5:7]
day=current[8:10]
hour=current[11:13]
min=current[14:16]
sec=current[-2:]
print(
    year+'년 '+
    month+'월 '+
    day+'일 '+ 
    hour+'시 '+
    min+'분 '+
    sec+'초'
)
print(current[-1])

# 리스트 연산
lst1=[1,2,3,4]
print(lst1)
lst1[0]=99
print(lst1)
lst1.append(999) #마지막에 추가 
print(lst1)
lst1.insert(3,99) #특정 인덱스에 추가 
print(lst1)
lst1.remove(99) # 해당 값 삭제
print(lst1)

#str1='python'
#print(str1)
#str1[0]='P'
#print(str1)

str1='python'
print(str1)
str1='P'+str1[1:]
print(str1)

# 문자열 포맷팅
full_name='Oh Yun Beom'
age=26
print(f"Hello I'm {full_name}, and I'm {age:2.0f} ages.")
#포맷팅->주로 값 입력받는대로 변경되어 출력되는 구조에서 사용
#2.0f --> 26 / 정수 그대로 출력 , 소수자리 0자리
#2.2f --> 26.00 / 정수 그대로 출력 , 소수자리 2자리
#를 의미함

int1=1566.555555
print(f"{int1:2.2f}")
print(f"{int1:1.3f}")
print(f"{int1:3.4f}")

#문자열 자르기
vals=full_name.split(' ')
print(vals)

#문자열 대체
print(full_name.replace('Oh','Woo'))

#문자열 공백 없애기
hi = '      Hello!       '
print(hi.lstrip()+'|')
print(hi.rstrip()+'|')
print(hi.strip()+'|')

#특정 문자 위치 찾기

print(full_name.index('h'))
#index로 없는 문자 검색 시 프로그램 오류
#print(full_name.index('x'))

#find로 없는 문자 검색 시 -1 반환
print(full_name.find('x'))

#문자 갯수 반환
print(full_name.count('o'))

#대문자 변경
print(full_name.upper())

#소문자 변경
print(full_name.lower())

# 연산자 우선순위
# () 소괄호로 빠른 연산 필요한 부분 처리




