# def main():
# 	print('so far so good.')
# 	for n in inclusive_range(0, 25, 1):
# 		print (n)
#
# def inclusive_range(start, stop, step):
# 	n = start
# 	while  n <= stop:
# 		yield n
# 		n += step
#
# if __name__ == "__main__": main()


def main():
	print('so far so good.')
	for n in inclusive_range(5, 45, 3):
		print (n)

def inclusive_range(*args):
	numargs = len(args)
	if numargs < 1: raise TypeError('requires atleast one argument')
	elif numargs == 1:
		stop = args[0]
		start = 0
		step = 1
	elif numargs == 2:
		(start, stop) =args
		step = 1
	elif numargs == 3:
		(start, stop, step) = args

	else: raise  TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))
	n = start
	while  n <= stop:
		yield n
		n += step

if __name__ == "__main__": main()