class SearchContactList(list):
    def search(self, name):
        matching_contacts = []
        # for i in range(6):
        #     print(self[i].name)
        for contact in self:
            if name.casefold() in contact.name.casefold():
                matching_contacts.append(contact)
        return matching_contacts


class Contacts:
    all_contacts = SearchContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contacts.all_contacts.append(self)


class SubContact(Contacts):
    def message(self, text):
        print("This object corresponds to the contacts: {}".format(self.name))


jb = Contacts("JB", "jb@email")
div = Contacts("Div", "Div@email")
jb2 = Contacts("Jbganesh", "jbg@mail")
jb3 = Contacts("Jeyabalaganesh", "jeyabalaganesh@email")
jb4 = Contacts("Jbgan", "jbgan@email")
jb5 = Contacts("bala", "bala@email")
jb6 = SubContact("subJb", "subjb@email")
# jb6.message("hello")

for contact in Contacts.all_contacts:
    print(contact.name, contact.email)
print()
lis = Contacts.all_contacts.search("jb")
for contact in lis:
    print(contact.name)
print()

# Contacts.all_contacts.search()