class Cat:
	def __init__(self, **kwargs):
		# self._color= kwargs.get('color', 'white')
		self.variables= kwargs

	def  meow(self):
		print('meooow!')



	# def  walk(self):
	# 	print('walks like a Cat')

	# # def set_color(self):
	# # 	self._color = color

	# def set_color(self):
	# 	self.variables['color']= color

	# # def get_color(self):
	# # 	return self._color

	# def get_color(self):
	# 	return self.variables.get('color', None)



	def  set_variable(self, k, v):
		self.variables[k] = v

	def get_variable(self, k):
		return self.variables.get(k, None)

def main():
	Tom = Cat(color = 'black')
	Tom.set_variable('feet', 'white')
	print(Tom.get_variable('color'))
	print(Tom.get_variable('feet'))


if __name__ == '__main__':main()