# 파일 만들기
#file = open('C:\DEV\Temp\Bank\sample01.txt', 'w',encoding='utf-8') # 절대경로
#utf-8:모든 나라 언어 표현 가능
#open(경로\파일이름,저장방식,변환) 

file = open('./Day05/sample02.txt', 'w',encoding='utf-8')
# 현재 위치에서 Day05에다가 
# ./Day05/../Day04/sample02.txt라고 지정하면 Day04 폴더에 파일생성
#../sample03.txt 라고 작성하면 Source라는 폴더에 만들어짐(Python2023폴더 제일 밖)

file.write('동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세\n')
file.write('지정한 절대경로에 파일 생성\n')

file.close()
print('파일 생성')

# 파일/폴더 경로
