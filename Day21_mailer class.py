class Contacts:
    all_contact = list()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contacts.all_contact.append(self)

    def print(self):
        print("hai")


class Mailer:
    def sent_mail(self, message):
        print("Sending mail to {}".format(self.email))
        print("The mail content is {}".format(message))


class Email_Contacts(Contacts, Mailer):
    pass


jb = Email_Contacts("jb", "Jb@gmail")
jb.sent_mail("Good Morning")
jb.print()
