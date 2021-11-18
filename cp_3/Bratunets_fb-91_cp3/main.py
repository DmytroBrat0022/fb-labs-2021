import math

def gcd(num1, num2, q=None):
    if q is None:
        q=[]
    if num2<num1:
        tempnum=num2
        num2=num1
        num1=tempnum
    if num1 == 0:
        return (num2, q)
    else:
        div, q = gcd(num2 % num1, num1, q)
    q.append(-(num2//num1))
    print(q)
    return (div, q)


#print(gcd(14,33))

def root(a, n, b):
    a = gcd(a,n)
    print(a[0])
    if a[0] >= 1:
        u = a[1]
        u.pop(0)
        u1 = 0
        u2 = 1
        for i in u:
            u2temp = u2
            u2 = u1 + i*u2
            u1 = u2temp
        print(u2)
        if a[0] == 1:
            return((u2*b)%n)
        else:
            i = 0
            x = []
            while i < a[0]:
                x.append(((u2*b/a[0])+(n/a[0])*i)%n)
                i+=1
            return(x)
    else:
        print("There are no solutions")
        


print(root(28,96,20))