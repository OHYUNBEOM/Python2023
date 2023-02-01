#구구단
for i in range(2,10):
    print(f'{i}단 시작!')
    for j in range(1,10):
        #print(i,'*',j,'=',i*j)
        print(f'{i} X {j} = {i*j:>2}', end=' ')
        # :>2 --> f'(포맷 함수를 이용한) 오른쪽 정렬
    print()