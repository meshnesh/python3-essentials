class Cat:
	def  meow(self):
		print('meooow!')

	def fur(self):
		print ('Has grey fur!')



	def  walk(self):
		print('walks like a Cat')

	def bark(self):
		print('the Cat can not bark')

class Dog:
	def bark(self):
		print('woof')

	def fur(self):
		print('The dog has white and brown fur')

	def walk(self):
		print('Walks like a dog')

	def meow(self):
		print('The dog can not meooow!')

def main():
	Tom = Cat()
	Siba = Dog()
	in_the_house(Tom)
	in_the_yard(Siba)

def in_the_house(cat):
	cat.meow()
	cat.walk()



def in_the_yard(dog):
	dog.bark()
	dog.fur()


	# Tom.meow()
	# Tom.bark()
	# Tom.walk()
	# Tom.fur()

	# Siba.meow()
	# Siba.bark()
	# Siba.walk()
	# Siba.fur()




if __name__ == '__main__':main()