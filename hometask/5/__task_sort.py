# Write a program that will create a list of people with name, age, height, and weight
# Sort the list of people by age
class Employee:

	def __init__(self, name, age, height, weight):
		self.name = name
		self.age = age
		self.height = height
		self.weight = weight

	def __repr__(self):
		return '{' + self.name + ', ' + str(self.age) + ', ' + str(self.height) + ', ' + str(self.weight) + '}'


if __name__ == '__main__':

	employees = [
		Employee('John', 28, 165, 65),
		Employee('Sam',  20, 175, 75),
		Employee('Joe', 35, 185, 85)
	]

	employees.sort(key=lambda x: x.age)
	print(employees)


