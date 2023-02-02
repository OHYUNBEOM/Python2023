class Person:
    name='익명'
    height='?'
    gender='?'
    blood_type='?'
    def walk(self): #def walk() 로 생성하면 실행 시 오류
        print('걷는중')
    def run(self,option):
        if option=='fast':
            #print(f'{self.name}이 빨리 뛰는중')
            print('{0}이 빨리 뛰는중'.format(self.name)) #위 주석과 같은의미
        else:
            print(f'{self.name}이 천천히 뛰는중')
    def stop(self):
        print('멈춤')
yb=Person() #인스턴스 생성
yb.name='오윤범'
yb.height='174cm'
yb.gender='M'
yb.blood_type='A'
print(f'{yb.name}의 키:{yb.height} 성별:{yb.gender}')
yb.walk()
yb.stop()
yb.run('fast')
yb.run('slow')