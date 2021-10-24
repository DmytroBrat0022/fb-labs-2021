file = open('F:\\GitHub\\fb-labs-2021\\cp_2\\Bratunets_fb91_cp2\\var2.txt', encoding='utf-8')
alphabet = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

text = file.read()
def Index(text):
	characters = len(text)
	temp = ""
	r=2
	j=0
	counter=0
	alphcount=0
	Sum=0
	Index=0
	SumBig=0
	while r<30:
		while j<r:
			while counter<characters//r:
				temp += text[counter*r+j]
				counter+=1
				#print(temp)
				if counter == characters//r:
					#print(temp)
					while alphcount<32:
						#print(temp)
						amount = temp.count(alphabet[alphcount])
						Sum += amount*(amount-1)
						alphcount+=1
			Index = Sum/(characters*(characters-1))
			SumBig+= Index
			Sum=0
			temp=""
			counter=0
			alphcount=0
			j+=1
		print(SumBig*1000000)
		SumBig=0
		r+=1
		j=0

# def MathExpectation():


Index(text)