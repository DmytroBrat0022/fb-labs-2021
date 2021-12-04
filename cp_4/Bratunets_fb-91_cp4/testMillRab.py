import math
import random
import time

def test_miller_rabin(p,k):
	if p <= 1 or p == 4:
		return False
	if p <= 3 or p == 5:
		return True
	if p%2 == 0 or p%3==0 or p%4==0 or p%5==0 or p%6 ==0 or p%7==0 or p%8==0 or p%9 == 0 or p%10==0:
		return False
	# for i in range(3, 999, 2):
	# 	if p % i == 0 and pow(i, 2) <= p:
	# 		return False
	else:
		d,s = rozklad(p)
		for i in range(0,k):
			x = random.randrange(2, p-1)
			# if gcd(x,p)>1:
			# 	return False
			# elif gcd(x,p)==1:
			a = pow(x, d,p)
			if a == 1 or a == p-1:
				continue
			else:
				i=0
				while i<s-1:
					a = pow(a,2)%p
					if a == 1:
						return False
					elif a == p-1:
						break
					else:
						i+=1
				if i==s-1:
					return False
		return True



def rozklad(p):
	counter = p-1
	s=0
	while counter%2==0:
		s+=1
		counter=counter//2
	d = int(counter)
	return(d,s)

def gcd(a, b):
    r = a % b
    q = (a - r) / b
    if r == 0:
        return b
    else:
        return gcd(b, r)

# for n in range(1,100):
#     if (test_miller_rabin(n, 2)):
#         print(n , end=" ");

def generate_key(size):
	while True:
		x = random.randrange(pow(2,size-1)+1, pow(2,size)-1)
		if test_miller_rabin(x, 4):
			return x

# if test_miller_rabin(13, 4):
# 	print("yes")
# 	time.sleep(3)

# if test_miller_rabin(452312848583266388373324160190187140051835877600158453279131187530910662655971, 4):
# 	print("yes")
# 	time.sleep(3)
condition = True
while condition:
	for i in range(0,4):
		q = generate_key(256)
		p =	generate_key(256)
		q1 = generate_key(256)
		p1 = generate_key(256)
		if p*q<= p1*q1:
			condition = False
			print("\n",q,"\n",p,"\n",q1,"\n",p1,"\n")

 q = 81994475584405935948868955911630277182389530435402539001816916720392262770879
 p = 60695060125406353645205586978113049519423657642692092700480783611828281008489
 q1 = 86321480949212574863441223330807749318502228060528766766450179206338212009411
 p1 = 81485329224126869631210665457337554019104661539455710371343449787989340245059