old_boy_age = 56


c=0
for i in range(3) :
    guess_age = int(input("old:"))
    if old_boy_age ==guess_age :
        print("you got it")
        break
    elif guess_age < old_boy_age :
        print("think bigger")
    else:
        print("think smallser")
    c=c+1
else:
    print("you have tried too many times..")
