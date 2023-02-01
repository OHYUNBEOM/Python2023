#람다함수

def add(x,y):
    return x+y
print(add(10,10))

ladd = lambda x,y : x+y
print(ladd(10,10))

print((lambda x,y : x+y)(10,10))
