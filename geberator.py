class incluive_range():
	def __init__(self, *args):
		numargs = len(args)
		if numargs < 1: raise TypeError('requires atleast one argument')
		elif numargs == 1:
			self.stop = args[0]
			self.start = 0
			self.step = 1
		elif numargs == 2:
			(self.start, self.stop) = args
			self.step = 1
		elif numargs == 3:
			(self.start, self.stop, self.step) = args

		else: raise TypeError('expected at most 3 arguments, got{}'.format(numargs))
		


	def __iter__(self):
		x = self.start
		while x <= self.stop:
			yield x
			x += self.step



def main():
	o = range(25)
	for  x in o: print(x)

if __name__=="__main__": main()