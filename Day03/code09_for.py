#for 문
arr=[11,22,33,44,55]
sum=0
for i in arr:
    #print(f'{i:1.0f}')
    print(i,end=' ')
    sum+=i

print()
print('list 합계 :',sum)

###
arr=[1,2,3,4,5]
for i in range(0,len(arr)):
    print(i+1,'번째 수는',arr[i],'입니다')