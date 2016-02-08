# import re

# def main():
# 	try: 
# 		for line in readfile('braven.py'): print (line.strip())
# 	except IOError as e:
# 		print('cannot readfile:', e)
# 	except ValueError as e:
# 		print('bad filename', e)

# def readfile(filename):
# 	if filename.endswith('.txt'):
# 		fh = open(filename)
# 		return fh.readlines()
# 	else: raise ValueError('filename must end with .txt')

# if __name__ == "__main__": main()

import re

def main():
	try: 
		for line in readfile('braven.txt'): print (line.strip())
	except IOError as e:
		print('cannot readfile:', e)
	except ValueError as e:
		print('bad filename', e)

def readfile(filename):
	if filename.endswith('.txt'):
		fh = open(filename)
		return fh.readlines()
	else: raise ValueError('filename must end with .txt')

if __name__ == "__main__": main()