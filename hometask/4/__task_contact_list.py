# Write a simple contact list
# On start program should print available list of commands (example below)
# 1. Add contact
# 2. Find contact
#
# By selecting 1. program asks for contact info to add
# Name
# Phone number
#
# On successful save it should print - New contact has been added
#
# By selecting 2. Program asks for search term. If list of contacts contains required data it should print it to the
# console (example below)
# 1. Ivan - 034567678
# 2. Petr - 345434534


class Contact:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def show(self):
        print(self.name, ":", self.phone)

    def meet(self, term):
        return term in self.name or term in self.phone


class Contact_book:
    def __int__(self):
        self.contactList = []

    def add(self, contact):
        self.contactList.append(contact)

    def print(self):
        for i in self.contactList:
            i.show()

    def find(self, term):
        find_contact = []
        for i in self.contactList:
            if i.meet(term):
                find_contact.append(i)
            else:
                for i in find_contact:
                    i.show()


class Main:

    def __int__(self):
        self.cl = Contact_book()
        self.intro()

    def into(self):
        print('=-=-===-=-=-=-=-  MENU -=-=-=-=-=-==-==')
        print("[ 1 ] ADD \n [ 2 ] FIND \n [ 3 ] \n PRINT ALL \n [ 4 ] EXIT")
        while True:
            option = input('>>> ')
            if option == '1':
                name = input('Name: ').capitalize().strip()
                phone = input('Phone: ').strip()
                new_contact = Contact(name, phone)
                self.cl.add(new_contact)
                print('New contact has been added\n')
            elif option == '2':
                term = input("Type name or phone")
                self.cl.find(term)
            elif option == '3':
                self.cl.print()
            elif option == '4':
                print('>>> Exit\n')
                break
            else:
                print("Incorrect number")
Main()





