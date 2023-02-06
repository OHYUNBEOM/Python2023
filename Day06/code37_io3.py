# 콘솔출력
# 이스케이프 캐릭터(탈출문자)
print('Hello\n\tWorld')
print('Hello\n\'World\'') #\' : '출력
print('Hello \\ World') #\\ : \출력 
# % 포맷코드로 출력
str1='me'
i=99
print('%s는 %d'%(str1,i))
print(f'{str1}는 {i}')
print('{0}는 {1}'.format(str1,i))
#f' 함수 소숫점 제한
print(f'{99.1234:.2f}')