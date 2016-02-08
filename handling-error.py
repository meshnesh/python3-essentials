# import re

# def main():
# 	try: #changed the name of the file intentionally for learning
# 		fh = open('braven.txt')
# 	except IOError as e:
# 		print('could not open the file:', e)
# 	else: 
# 		for line in fh: print(line.strip())

# if __name__ == "__main__": main()




#could also be written as this

import re

def main():
	try: #changed the name of the file intentionally for learning
		fh = open('braven.txt')
		for line in fh: print(line.strip())

	except IOError as e:
		print('could not open the file:', e)
		

if __name__ == "__main__": main()