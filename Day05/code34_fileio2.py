file=open('./Day05/sample02.txt','r',encoding='utf-8')
while True:
    text=file.read()
    if not text: break#더이상 text가 없으면 그만읽어라
    print(text)

file.close()#file open 사용시에 반드시 close 필수