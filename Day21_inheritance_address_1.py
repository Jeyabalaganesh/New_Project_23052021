class Contacts:
    all_contacts = list()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contacts.all_contacts.append(self)


class AddressHolder:

    def __init__(self, street, city, state, country):
        self.street = street
        self.city = city
        self.state = state
        self.country = country


class Friends(Contacts, AddressHolder):

    def __init__(self, name, email, ph, street, city, state, country):
        Contacts.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, country)
        self.ph_no = ph


f1 = Friends("Jb", "jb@gmail", 9842, "Ist street", "VNR", "TN", "india")
print(f1.ph_no)

