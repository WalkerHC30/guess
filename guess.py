import random
r = random.randint(1, 100)
count = 0
while True:
    count += 1
    a = int(input("請輸入數字: "))
    if a == r:
        print('恭喜猜對了!!')
        print('這是第', count, '次猜!')
        break
    elif a > r:
        print('比答案大!')
    else:
        print('比答案小!!')
    print('這是第', count, '次猜!')