# 모듈 사용
import random

numbers=[i for i in range(1,46)]
lotto=[]
for i in range(6):
    lotto.append(random.choice(numbers))
print(lotto)

# import random
# numbers=list(range(1,46))
# lotto=[]
# random.shuffle(numbers)
# lotto=random.choices(numbers,k=6)
# print(lotto)

