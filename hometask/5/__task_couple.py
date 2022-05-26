# Write a program that will find a couple.
# On the start program have to create a list of 10 random people male and female.
# Every person have three fields name, age, sex
# Program asks a user to enter a name and a desired age for search
# Matching rule
# Couple can match if users age difference not more than 5 years and both names has at least same two letters
# If match is found program should print - Congrats there is a matching pair Name1 + Name2!
# It no match - just print Sorry, no match! =(

class People:

	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def __repr__(self):
		return '{' + self.name + ', ' + str(self.age) + ', ' + self.gender + '}'

if __name__ == '__main__':

	people = [
		People('John', 28, "M"),
		People('Sam',  20, "M"),
		People('Joe', 35, "M"),
		People('Dik', 28, "M"),
		People('Alex', 20, "M"),
		People('Ann', 35, "F"),
		People('Kate', 28, "F"),
		People('Mag', 35, "F"),
		People('Sali', 35, "F"),
		People('Joely', 35, "F")
	]

	# print(people.split())

people_list = []
for man in people:
	people_list.append(man)

name = input('Type name: ')
age = int(input('Type desired age: '))

def compare():
	for i in people_list:
		elem1 = [x for x in i.name.split()]
		elem2 = [x for x in name.split()]
		for item in elem1:
			if item in elem2:
				return True

for item in people_list:
	if (age - item.age) <= 5 and compare() is True:
		print("Congrats there is a matching pair")
	else:
		print("Sorry, no match! =(")



# print(people_list)

