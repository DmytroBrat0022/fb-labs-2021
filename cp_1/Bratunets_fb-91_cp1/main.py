import math

file = open('F:\\GitHub\\fb-labs-2021\\cp_1\\Bratunets_fb-91_cp1\\text.txt', encoding='utf-8')

characters = 0;

for line in file:
        wordslist=line.split()
        characters += sum(len(word) for word in wordslist)
print(characters)
file.close

file = open('F:\\GitHub\\fb-labs-2021\\cp_1\\Bratunets_fb-91_cp1\\text.txt', encoding='utf-8')

text = file.read()
def count_frequency_with_spaces(characters):
	print((text.count("а")+text.count("А"))/characters)
	print((text.count("б")+text.count("Б"))/characters)
	print((text.count("в")+text.count("В"))/characters)
	print((text.count("г")+text.count("Г"))/characters)
	print((text.count("д")+text.count("Д"))/characters)
	print((text.count("е")+text.count("Е"))/characters)
	print((text.count("ж")+text.count("Ж"))/characters)
	print((text.count("з")+text.count("З"))/characters)
	print((text.count("и")+text.count("И"))/characters)
	print((text.count("й")+text.count("Й"))/characters)
	print((text.count("к")+text.count("К"))/characters)
	print((text.count("л")+text.count("Л"))/characters)
	print((text.count("м")+text.count("М"))/characters)
	print((text.count("н")+text.count("Н"))/characters)
	print((text.count("о")+text.count("О"))/characters)
	print((text.count("п")+text.count("П"))/characters)
	print((text.count("р")+text.count("Р"))/characters)
	print((text.count("с")+text.count("С"))/characters)
	print((text.count("т")+text.count("Т"))/characters)
	print((text.count("у")+text.count("У"))/characters)
	print((text.count("ф")+text.count("Ф"))/characters)
	print((text.count("х")+text.count("Х"))/characters)
	print((text.count("ц")+text.count("Ц"))/characters)
	print((text.count("ч")+text.count("Ч"))/characters)
	print((text.count("ш")+text.count("Ш"))/characters)
	print((text.count("щ")+text.count("Щ"))/characters)
	print((text.count("ы")+text.count("Ы"))/characters)
	print((text.count("ь")+text.count("Ь"))/characters)
	print((text.count("э")+text.count("Э"))/characters)
	print((text.count("ю")+text.count("Ю"))/characters)
	print((text.count("я")+text.count("Я"))/characters)
	print((text.count(" "))/characters)

def count_letters(word):
    return characters - word.count(' ')
def count_frequency_without_spaces(text):
	textwoutspaces = count_letters(text)

	#print(textwoutspaces)

	print((text.count("а")+text.count("А"))/textwoutspaces)
	print((text.count("б")+text.count("Б"))/textwoutspaces)
	print((text.count("в")+text.count("В"))/textwoutspaces)
	print((text.count("г")+text.count("Г"))/textwoutspaces)
	print((text.count("д")+text.count("Д"))/textwoutspaces)
	print((text.count("е")+text.count("Е"))/textwoutspaces)
	print((text.count("ж")+text.count("Ж"))/textwoutspaces)
	print((text.count("з")+text.count("З"))/textwoutspaces)
	print((text.count("и")+text.count("И"))/textwoutspaces)
	print((text.count("й")+text.count("Й"))/textwoutspaces)
	print((text.count("к")+text.count("К"))/textwoutspaces)
	print((text.count("л")+text.count("Л"))/textwoutspaces)
	print((text.count("м")+text.count("М"))/textwoutspaces)
	print((text.count("н")+text.count("Н"))/textwoutspaces)
	print((text.count("о")+text.count("О"))/textwoutspaces)
	print((text.count("п")+text.count("П"))/textwoutspaces)
	print((text.count("р")+text.count("Р"))/textwoutspaces)
	print((text.count("с")+text.count("С"))/textwoutspaces)
	print((text.count("т")+text.count("Т"))/textwoutspaces)
	print((text.count("у")+text.count("У"))/textwoutspaces)
	print((text.count("ф")+text.count("Ф"))/textwoutspaces)
	print((text.count("х")+text.count("Х"))/textwoutspaces)
	print((text.count("ц")+text.count("Ц"))/textwoutspaces)
	print((text.count("ч")+text.count("Ч"))/textwoutspaces)
	print((text.count("ш")+text.count("Ш"))/textwoutspaces)
	print((text.count("щ")+text.count("Щ"))/textwoutspaces)
	print((text.count("ы")+text.count("Ы"))/textwoutspaces)
	print((text.count("ь")+text.count("Ь"))/textwoutspaces)
	print((text.count("э")+text.count("Э"))/textwoutspaces)
	print((text.count("ю")+text.count("Ю"))/textwoutspaces)
	print((text.count("я")+text.count("Я"))/textwoutspaces)


amountofbigrmswithspace = 470789
amountofbigrmswithoutspaces = 569212
def amountofbigrmswithoutspaces(text):
	newtext = text.replace(" ", "")
	alphabet_sm = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']
	alphabet_bg = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ы','Ь','Э','Ю','Я']

	newtext = text.replace(" ", "")
	i=0
	j=0
	Sum=0
	while i<31:
		while j<31:
			amount = newtext.count(alphabet_sm[i]+alphabet_sm[j])+newtext.count(alphabet_bg[i]+alphabet_bg[j])+newtext.count(alphabet_bg[i]+alphabet_sm[j])+newtext.count(alphabet_sm[i]+alphabet_bg[j])
			Sum+=amount
			j+=1
			amount=0
		j=0
		i+=1
	return Sum

def count_bigrams_with_spaces(text):
	alphabet_sm = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']
	alphabet_bg = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ы','Ь','Э','Ю','Я']

	i=0
	j=0
	amount = 0
	for characters in text:
		while i<31:
			while j<31:
				amount = text.count(alphabet_sm[i]+alphabet_sm[j])+text.count(alphabet_bg[i]+alphabet_bg[j])+text.count(alphabet_bg[i]+alphabet_sm[j])+text.count(alphabet_sm[i]+alphabet_bg[j])
				print(alphabet_bg[i]+alphabet_bg[j])
				print(round((amount/amountofbigrmswithspace), 7))
				j+=1
				amount=0

			j=0
			i+=1

def count_bigrams_without_spaces(text):
	alphabet_sm = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']
	alphabet_bg = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ы','Ь','Э','Ю','Я']
	newtext = text.replace(" ", "")
	i=0
	j=0
	amount = 0
	for characters in text:
		while i<31:
			while j<31:
				amount = newtext.count(alphabet_sm[i]+alphabet_sm[j])+newtext.count(alphabet_bg[i]+alphabet_bg[j])+newtext.count(alphabet_bg[i]+alphabet_sm[j])+newtext.count(alphabet_sm[i]+alphabet_bg[j])
				print(alphabet_bg[i]+alphabet_bg[j])
				print(round((amount/amountofbigrmswithoutspaces), 7))
				j+=1
				amount=0
			j=0
			i+=1

def H1_with_spacebars(text):
	alphabet_sm = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']
	alphabet_bg = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ы','Ь','Э','Ю','Я']

	Sum = 0
	i = 0
	while i<31:
		P = ((text.count(alphabet_sm[i]) + text.count(alphabet_bg[i]))/characters)
		Sum += P * math.log2(P)
		i += 1
	print("H1:%1f"%(-Sum))


def H1_without_spacebars(text):
	alphabet_sm = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']
	alphabet_bg = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ы','Ь','Э','Ю','Я']

	textwoutspaces = count_letters(text)
	newtext = text.replace(" ", "")
	Sum = 0
	i = 0
	while i<31:
		P = ((newtext.count(alphabet_sm[i]) + newtext.count(alphabet_bg[i]))/textwoutspaces)
		Sum += P * math.log2(P)
		i += 1
	print("H1:%1f"%(-Sum))

def H2_with_spacebars(text):
	alphabet_sm = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']
	alphabet_bg = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ы','Ь','Э','Ю','Я']

	Sum = 0
	i=0
	j=0
	P = 0
	amount = 0
	while i<31:
		while j<31:
			amount = text.count(alphabet_sm[i]+alphabet_sm[j])+text.count(alphabet_bg[i]+alphabet_bg[j])
			P = amount/amountofbigrmswithspace
			if P!=0:
				Sum += P * math.log2(P)
			j+=1
			amount=0

		j=0
		i+=1
	print("H2:%1f"%(-Sum/2))

def H2_without_spacebars(text):
	alphabet_sm = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']
	alphabet_bg = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ы','Ь','Э','Ю','Я']

	newtext = text.replace(" ", "")
	Sum = 0
	i=0
	j=0
	P = 0
	amount = 0
	while i<31:
		while j<31:
			amount = newtext.count(alphabet_sm[i]+alphabet_sm[j])+newtext.count(alphabet_bg[i]+alphabet_bg[j])
			P = amount/amountofbigrmswithoutspaces
			if P!=0:
				Sum += P * math.log2(P)
			j+=1
			amount=0

		j=0
		i+=1
	print("H2:%1f"%(-Sum/2))

#count_frequency_with_spaces(characters)
#count_frequency_without_spaces(text)

#count_bigrams_without_spaces(text)
#count_bigrams_with_spaces(text)

#H1_with_spacebars(text)
#H2_with_spacebars(text)

#H1_without_spacebars(text)
#H2_without_spacebars(text)

print(amountofbigrmswithoutspaces(text))




