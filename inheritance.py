class Animal:
	def talk(self): print('I have something to say!')
	def walk(self): print('Hey! Im walkin here!')
	def clothes(self): print('I dress warmly!')


class Cat(Animal):
	def  meow(self):
		print('meooow!')



	def  walk(self):
		# super.walk()
		print('walks like a Cat')



def main():
	Tom = Cat()
	Tom.meow()
	Tom.walk()
	Tom.clothes()
	print(Tom)

if __name__ == '__main__':main()