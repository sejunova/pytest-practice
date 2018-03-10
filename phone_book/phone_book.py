class PhoneBook:
    def __init__(self):
        self.contacts = dict()

    def add_contact(self, name, number):
        self.check_consistency(number)
        self.contacts[name] = number

    def look_up(self, name):
        if name not in self.contacts:
            raise KeyError('This contact does not exist')
        return self.contacts.get(name)

    def check_consistency(self, number):
        for contact in self.contacts.values():
            if len(number) > len(contact):
                num1, num2 = number[:len(contact)], contact
            else:
                num1, num2 = number, contact[:len(number)]
            if num1 == num2:
                raise ValueError('Phone book should be consistent')

