for i in range(10):
    if i%2 != 0:
        print(i)  #i是奇数直接输出
        continue
    else:
        i += 2    #i是偶数就加2输出
        print(i)
