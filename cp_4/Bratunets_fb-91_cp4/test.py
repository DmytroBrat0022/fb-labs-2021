import random
import time

def Miller_Rabin_test(number, k):
    number = int(number)
    if number%2 == 0 or number%3==0 or number%4==0 or number%5==0 or number%6 ==0 or number%7==0 or number%8==0 or number%9 == 0 or number%10==0:
        return False
    if number<=3 and number>1:
        return True
    if number == 1:
        return False
    s = 0
    d = number-1
    while d%2==0:
        d = d//2
        s = s+1
    t = int(d)
    for i in range(0,k):
        a = random.randint(2,number-1)
        x = pow(a,t,number)
        if x == 1 or x == number - 1:
            continue
        for r in range(0, s-1):
            x = pow(x,2,number)
            if x == 1: 
                return True
            if x == number-1:
                break
        else:
            return False
    return True

if Miller_Rabin_test(62487919534514317603035027685926108112127591727117666714152446598844988448693 , 4):
    print("yes")
    time.sleep(3)