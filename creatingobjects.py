class student(object):
	"""docstring for student"""
	def __init__(self, busy = 'study'):
		
		self.busy = busy


	def howbusy(self):
		return self.busy
		

def main():
	study = student()
	learning = student("python")
	print(learning.howbusy())


if __name__ == "__main__":main()