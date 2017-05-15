old_boy_age = 56


c=0
while c <  3:
    guess_age = int(input("old:"))
    if old_boy_age ==guess_age :
        print("you got it")
        break
    elif guess_age < old_boy_age :
        print("think bigger")
    else:
        print("think smallser")
    c=c+1

    if c==3:
        while True:
            cont = input("再试试吗?y/n:")
            if  cont in ('y','Y') :
                c = 0
                break
            elif cont in ('n','N'):
                break
            else:
                print("输入有误")
                continue
if c == 3:
    print("you have tried too many times..")
