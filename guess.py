import random
s = int(input("請決定開始值: "))
e = int(input("請決定結束值: "))

r = random.randint(s, e) # 開始值務必比結束值小 不然會輸錯!
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