#자동차 클래스
class Car:
    __number='15더 8117'

    def get_number(self):
        return self.__number

    def set_number(self,number):
        self.__number=number

    def __init__(self,number='15더 8117') -> None:
        print('생성자 생성')
        self.__number=number

    def __str__(self) -> str:
        return f'차 번호는 {self.__number} 입니다.'

    # def __new__(cls):
    #     print('new')
    #     return super().__new__(cls) #부모클래스(상속)
        

mycar = Car()
print(mycar)

yourcar=Car('88호 7777')
print(yourcar)

yourcar.set_number('99호 9999')
print(yourcar)