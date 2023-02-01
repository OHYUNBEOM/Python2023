#무한loop
while True:
    print(
    '''
    숫자 입력하세요
    1.입력
    2.검색
    3.수정
    4.삭제
    5.종료
    ''',end='')
    num=int(input('번호입력>> '))
    if num==1:
        print('입력')
    elif num==2:
        print('검색')
    elif num==3:
        print('수정')
    elif num==4:
        print('삭제')
    elif num==5:
        print('종료')
        break
    else:
        print('\t입력오류>1~5 입력')
        continue