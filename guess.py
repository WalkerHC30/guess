import random
r = random.randint(0, 100)
while True:
    a = int(input("請輸入數字: "))
    if a == r:
        print('恭喜猜對了!!')
        break
    elif a > r:
        print('比答案大!')
    else:
        print('比答案小!!')