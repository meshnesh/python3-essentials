






def spellcheck(sentence):
	words = open('spell.words').readlines()
	words = list(map(lambda x: x.strip(),words))
	res = sentence.split()
	ret = []
	for item in res:
		if(item not in words):
			ret.append(item)
	return ret

def  main():
	sentence = input("please enter a sentence\n")
	lst = []

	lst = spellcheck(sentence)
	print(lst)

if __name__ == "__main__":main()