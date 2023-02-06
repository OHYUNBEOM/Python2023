# 주소록 프로그램
# 2023-02-06
# OYB
# 예외처리
# 1. 파일 없을 때 - load_contact에서 잡음
# 2. 입력 시 /갯수 다를때 - run() 함수 내에 sel_menu==1 부분에서 수정
# 3. 메뉴에 숫자 외 문자 입력- get_menu에서 잡음
import os
def clearConsole(): #콘솔 클리어
    os.system('cls')  
# 2. Class 생성
class Contact: 
    def __init__(self,name,phone_num,email,addr) -> None: #생성자 - 이름 / 전화번호 / 이메일 / 주소
        self.__name=name
        self.__phone_num=phone_num
        self.__email=email
        self.__addr=addr
    def __str__(self) -> str: #___str 함수 재정의 - print 찍을 때 기본꼴
        str_return=(f'이름 :{self.__name}\n휴대폰:{self.__phone_num}\n이메일:{self.__email}\n주소:{self.__addr}')
        return str_return
    # 연락처 삭제 시 이름 찾기 
    def isNameExist(self,name):
        if self.__name==name:
            return True
        else:
            return False
    # 연락처 파일 DB 저장을 위한 멤버변수 접근
    def getname(self):
        return self.__name
    def getphonenum(self):
        return self.__phone_num
    def getemail(self):
        return self.__email
    def getaddr(self):
        return self.__addr
# 5. 사용자 입력 
def set_contact():
    name,phone_num,email,addr=input('정보입력(이름/전화번호/이메일/주소[구분자:/]: ').split('/')
    contact = Contact(name,phone_num,email,addr)
    return contact #사용자가 입력한 정보가 들어간 Contact Class를 반환
# 파일 저장
def save_contact(lst_contact):
    f=open('C:/Source/Python2023/Project/contact.txt','w',encoding='utf-8')
    for item in lst_contact:
        text=f'{item.getname()}/{item.getphonenum()}/{item.getemail()}/{item.getaddr()}'
        f.write(f'{text}\n')
    f.close() #파일 닫기
#파일 불러오기
def load_contact(lst_contact):
    try: # file 없을 때 불러오면 예외처리
        f=open('C:/Source/Python2023/Project/contact.txt','r',encoding='utf-8')    
    except Exception as e: #txt파일이 없다면 비어있는 txt하나 생성하고 탈출
        file=open('C:/Source/Python2023/Project/contact.txt','w',encoding='utf-8')    
        file.close()
        return
    while True:
        line=f.readline().replace('\n','')#문장끝 줄바꿈을 없애줘야 정상적으로 저장하고 불러올 수 있음
        # replace 처리를 안해주게되면 아래에서 lines[0]... 불러올 때 인덱스 오류 생김
        if not line:break
        lines=line.split('/')
        contact=Contact(lines[0],lines[1],lines[2],lines[3])
        lst_contact.append(contact)
    f.close()
# 연락처 출력
def get_contact(lst_contact):
    for item in lst_contact: #저장된 연락처 모두 출력
        print(item)
        print('============')
# 6. 메뉴 입력 + 메뉴에 숫자 대신 문자 입력 시 예외 처리
def get_menu():
    str_menu=('주소록 프로그램\n1.연락처 추가\n2.연락처 출력\n3.연락처 삭제\n4.종료\n')
    print(str_menu)
    try:
        menu=int(input('메뉴입력>'))
    except Exception as e: # 숫자 외 입력 예외처리
        menu =0 #문자 넣으면 전부 0으로 처리 
    return menu
#연락처 삭제
def del_contact(lst_contact,name):
    count=0
    for i,item in enumerate(lst_contact): #For 돌리면서 index값도 같이 부여하고싶을때 enumerate 사용
        #i에는 0,1,2,3... 들어가고 item에는 입력한 연락처 자체가 들어감
        if item.isNameExist(name): #삭제하고자 하는 name이 존재한다면
            count+=1
            del lst_contact[i] #해당 위치(i)에 있는 배열을 삭제한다
    if count >0:
        print('삭제했습니다')
    else:
        print('삭제할 연락처가 없습니다')
# 디버그 시 수행
def run():
    # temp=Contact('오윤범','010-8515-0728','dbsqja353@naver.com','부산광역시 중구')
    # print(temp) --> __str__ 함수에서 선언한대로 출력됨
    lst_contact=[] # 사용자 입력을 받을 연락처 list 
    load_contact(lst_contact)
    clearConsole()
    while True:
        sel_menu=get_menu() # 메뉴 입력
        if sel_menu==1: 
            # 연락처 추가
            clearConsole()
            try:
                contact = set_contact() 
                lst_contact.append(contact)# 만들어둔 lst_contact에 새로운 연락처 리스트들을 계속 추가
                input('주소록 입력 성공')
            except Exception as e:
                print('!!이름/전화번호/이메일/주소 형태로 입력!!',end='')
                input()
            finally: #try/except/finally의 로직 - try로 set_contact호출해서 주소록에 자료 입력했는데
                #나뉘는 단위인 '/'를 4개 안찍고 하나만 찍어서 오류를 발생시키면 
                # except 으로 들어가서 오류문을 찍는거고 input()으로 사용자 입력을 기다리고 있다가
                # 사용자가 키보드 입력을 하게되면 finally 로 넘어가게 되고
                # finally에서 clearsoncole()을 통해 콘솔 화면을 초기화 시키고 나면
                # 다시 무한루프 돌고있는 while문의 가장 위로 올라가서 get_menu()를 실행시키기에
                # 메뉴 입력받는 화면이 계속 나타남
                clearConsole()
        elif sel_menu==2:
            # 연락처 출력
            clearConsole()
            if not lst_contact: #list가 비어있다면/입력된 연락처가 없을 때 
                print('연락처가 없습니다')
                input()
                clearConsole()
            else:
                print('저장된 연락처>>')
                get_contact(lst_contact) # 추가된 연락처들이 들어있는 lst_contact를 출력
                input('주소록 출력 성공')
                clearConsole()
            # 연락처 삭제 
        elif sel_menu==3:
            clearConsole()
            name=input('삭제할 이름 입력>')
            del_contact(lst_contact,name)
            input()
            clearConsole()
            # 종료
        elif sel_menu==4:
            save_contact(lst_contact) #입력한 주소록 파일로 저장
            break
        else:
            clearConsole()
# 1. Main 영역
if __name__=='__main__':
    run()#디버그 시 수행