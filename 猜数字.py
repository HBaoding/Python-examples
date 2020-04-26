#猜数字游戏
import random
secret = random.randint(1,10)
print('---猜猜看---')
count = 0
while(count<=2):
    temp = input("0到9，猜猜我在想什么数字：")
    guess = int(temp)
    count = count + 1
    if guess == secret:
        count = 10
        print("这你都能猜得到？！")
        print("哼，猜中也没奖励！")
    else:
        if guess > secret:
            print("大了，大了！")
            if count == 3:
                print("没有机会啦~")
            else:
                print("还有"+ str(3-count) + "机会哦~")
        else:
            print("小了哟~ ")
            if count == secret:
                print("没有机会啦~")
            else:
                print("还有"+ str(3-count) + "机会哦~")
             
        
print("游戏结束，不玩了^_^ ")
