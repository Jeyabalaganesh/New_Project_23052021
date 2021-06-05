class SearchContactList(list):
    def search(self, name):
        matching_contacts = []
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


class Friends(Contacts):
    def __init__(self, name, email, ph_no):
        super().__init__(name, email)
        self.ph_no = ph_no


f = Friends("Bala", "Bala@gmail", 9677263852)
c = Contacts("Name1", "Email1")
c2 = Contacts("Name2", "Email2")
c3 = Contacts("Name3", "Email3")
f2 = Friends("Bala2", "Bala@gmail2", 123456789)

for contacts in Contacts.all_contacts:
    print(contacts.name)
print()

lis = Contacts.all_contacts.search("bala")
for item in lis:
    print(item.name, item.email, item.ph_no)
