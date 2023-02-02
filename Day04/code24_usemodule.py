# 모듈 사용
import math as m #클래스화 안된 모듈
import code22_person as p #우리가 만든 클래스
from code23_car import Car #code23_car.py 파일의 Car클래스만 뽑아와서 사용
print(m.pi)
# 만든 모듈 사용
Me=p.Person('김김김',188,'M','AB')
print(Me)
mycar=Car()
print(mycar)

