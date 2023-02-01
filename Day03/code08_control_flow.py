#if문
while(1):
    name=input()
    if name=='종료':
        print('while문을 종료합니다')
        exit()
    else:
        if name=='윤범':
            print('오윤범')
        elif name =='히동':
            print('우히동')
        else:
            print('윤범/히동 중 입력하세요')

