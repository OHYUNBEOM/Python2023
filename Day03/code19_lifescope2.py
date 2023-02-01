#전역 / 지역 변수 
num=1
for i in range(1,11):
    num=i*num
    #print(f'{i+1}번')
    print('{0}번'.format(i))
    
    if i%3==0:
        res='테스트'
        print(res)

print(f'결과{num}')
print(res)
