class Contact:
    all_contacts = []

    def __init__(self, name, ph_no, email):
        self.name = name
        self.ph_no = ph_no
        self.email = email
        Contact.all_contacts.append(self)

    def print_contact(self):
        print(self.name, self.ph_no, self.email)


class Sub_contact(Contact):

    def message(self, text):
        print("This class is inherrting - {}".format(text))
        print("the proof is the name {}".format(self.name))
        print("hence proved")


jb = Contact("JB", 9940490427, "balaganesh@gmail.com")
div = Sub_contact("Divaka", 123456, "Diva@nitt.edu")

# div.message("hello")
# div.print_contact()
# print(Contact.all_contacts[1].name)


print(jb.__dict__)
div2 = Contact("diva", 123456, "diva@nitt.edu")
div2.print_contact()

print(jb.all_contacts[1].email)


for obj in Contact.all_contacts:
    print(obj.name, obj.email, obj.ph_no)
