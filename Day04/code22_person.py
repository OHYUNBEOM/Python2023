class Person:
    def __init__(self,name='익명',height='?',gender='?',blood_type='?') -> None: #생성자,초기화,파라미터에 기본값 지정
        self.name=name
        self.height=height
        self.gender=gender
        self.blood_type=blood_type
        

    def walk(self): #def walk() 로 생성하면 실행 시 오류
        print(f'{self.name}이 걷는중')


    def run(self,option):
        if option=='fast':
            #print(f'{self.name}이 빨리 뛰는중')
            print('{0}이 빨리 뛰는중'.format(self.name)) #위 주석과 같은의미
        else:
            print(f'{self.name}이 천천히 뛰는중')


    def stop(self):
        print(f'{self.name}이 멈춤')


    def show(self):
        print(f'이름:{self.name}\n키:{self.height}\n성별:{self.gender}\n혈액형:{self.blood_type}\n================')

    #2. 생성자 외 매직메서드(Function) __str__ --> print(객체) 했을 때 나오게 하는 기본 꼴
    # 즉 전형적으로 정보를 보여주는 함수인 show의 역할을 print(객체) 했을 때 그대로 출력 될 수 있게함
    def __str__(self) -> str:
        return f'출력 : 이름은 {self.name}, 성별은 {self.gender}'

# 1. 초기화 후 객체생성
yb1=Person('오윤범','178cm','M','A')
yb1.show()
yb1.walk()
yb1.run('fast')
yb1.run('slow')
yb1.stop()

print(yb1)