# Car 부모클래스
class Car:
    #Mother Class
    __name='car'
    __color='white'
    __plate_number=''
    __product_year=1900
    def __str__(self) -> str:
        return '부모 클래스'
    def run(self):
        return 'Car is running'
    def stop(self):
        return 'Car is Stopped'
    def get_name(self):
        return self.__name