class Contact:
    all_contacts = []
    def __init__(self, name, lastname, phone_number):
        self.name = name
        self.lastname = lastname
        self.phone_number = phone_number
        Contact.all_contacts.append(self)

class Friend(Contact):
    def play_football_with_me(self):
        print('Play football with me!')

class ContactList(list):
    def search_by_name(self, name):
        search_contacts = []
        for contact in self:
            if name in contact.name:
                search_contacts.append(contact)
        return search_contacts

sultan = Contact('Sultan', 'Aitkulov', '0707316794')
murat = Contact('Murat', 'Aitkulov', '0707316794')
barry = Friend('Barry', 'Allen', '0555995511')

print(Contact.all_contacts)

sultan = ContactList(Contact.all_contacts)
search = sultan.search_by_name('Sultan')
print([contact.name for contact in search])
