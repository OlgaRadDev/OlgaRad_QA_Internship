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


class Contact(object):
    contact_list = []

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        return Contact.contact_list.append(self)
    



