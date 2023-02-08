class Person:

    first_name = "none "
    last_name = "0"
    male = "none"
    female = "0"
    email_address = ""
    phone_number = ""
    postal_address = ""

    def __init__(self):
        self.person_first_name = None
        self.person_last_name = None

    def set_person_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def set_person_gender(self, male, female):
        self.male = male
        self.female = female

    def set_person_contact_details(self, email_address, phone_number, postal_address):
        self.email_address = email_address
        self.phone_number = phone_number
        self.postal_address = postal_address

    def get_person_name(self):
        return self.person_first_name, self.person_last_name

    def get_person_contact_info(self):
        return self.email_address, self.phone_number, self.postal_address

    def get_person_gender(self):
        return self.male, self.female
