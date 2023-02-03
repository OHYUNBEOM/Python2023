# 예외처리
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

try:#예외처리 - try / except 
    x,y=list(map(int,input('정수 두개 입력>').split()))

except Exception as e:
    print(e)
    exit()

finally:
    print('exit()있어도 finally 먹음') 

print('test>')

try:#예외처리
    print(f'div:{div(x,y)}')

# except ZeroDivisionError as e:
#     print('0으로 나눌 수 없음')
#     exit()

except Exception as e:
    print(e)

finally:
    print('continue...')

print(f'add:{add(x,y)}')
print(f'mul:{mul(x,y)}')