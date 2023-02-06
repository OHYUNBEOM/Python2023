from code38_car import *

class Genesis(Car):
    def __init__(self,name,color,plate_number,product_year) -> None:
        super().__init__
        self.__name=name
        self.__color=color
        self.__plate_number=plate_number
        self.__product_year=product_year
        print(f'{self.__name} 인스턴스 생성')
        
    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return self.__name

    def run(self): #부모클래스 run 함수 재정의
        return f'{self.__name}이(가) 달립니다.'
        
    def stop(self):
        return f'{self.__name}이(가) 멈춥니다.'


gv80=Genesis('GV80','BLACK','15더 8117',2010)
gv80.set_name('GV80')
print(f'이 차의 이름은{gv80.get_name()}입니다.')
print(gv80.run())
print(gv80.stop())

print(gv80.__color) 
# 이 구문이 오류가 나는 이유는 변수 선언을 __ 을 통해서 접근을 못하게 막아놨기때문에
# print(gv80.__color)로 바로 변수를 출력하는것 자체도 불가능하고 
# color을 출력하고싶으면 set_name/get_name 처럼 set_color/get_color을 통해서
# 함수로 접근해야 출력할 수 있음.
