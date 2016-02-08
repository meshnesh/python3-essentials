def main():
	testfunc(11, 2, 34, 56, 7, 89)

def testfunc(who, where, why, *args):
	print(who, where, why, args)
	for n in args: print(n)
if __name__ == "__main__": main()