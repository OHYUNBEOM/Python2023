#계산기
def calc(option,*args):
    result=0
    if option == 'add':
        for i in args:
            result +=i

    elif option == 'mul':
        result=1
        for i in args:
            result *=i

    elif option=='sub':
        result=args[0]
        for i in args[1:]:
            result-=i

    elif option =='div':
        result=args[0]
        for i in args[1:]:
            result/=i

    return print(result)

# calc('add',1,2,3,4,5)
# calc('mul',1,2,3,4,5)
# calc('sub',1,2,3,4,5)
# calc('div',10,5,2)

#함수 결과 하나 이상  
def mul_and_div(x,y):
    return(x*y,x//y)

#print(mul_and_div(10,2))

res1,res2 = mul_and_div(10,2)
#print(res1,res2)