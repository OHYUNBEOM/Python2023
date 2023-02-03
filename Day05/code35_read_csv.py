# 공공데이터포털 csv 파일 읽어오기
# 부산광역시 시내버스, 마을버스 현황 
import csv
file_name = 'busanbus.csv'
dir_name='C:/Source/Python2023/'
full_path=dir_name+file_name
file=open(full_path,'r',encoding='utf-8')
reader = csv.reader(file,delimiter=',') # delimiter은 구분자, 해당 파일에서는 ,
next(reader)

for line in reader:
    print(line)

file.close() # 열었으면 닫자 꼭