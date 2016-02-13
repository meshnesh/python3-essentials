class Cat:
	def __init__(self, color= 'white'):
		self._color = color

	def  meow(self):
		print('meooow!')



	def  walk(self):
		print('walks like a Cat')

	def set_color(self):
		return self._color

	def get_color(self):
		return self._color



def main():
	Tom = Cat()
	# print(Tom.get_color)
	Tom.set_color('red')
	print(Tom.get_color())

if __name__ == '__main__':main()