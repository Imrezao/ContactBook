class contactbook:   
    """
    A simple contact book application that stores contacts in memory.

    Each contact has a name (key), phone number, email address, and physical address.
    Contacts can be added, viewed, updated, and deleted.
    """

    def __init__(self):
        self.contacts: dict = {}

    def add_contact(self, name: str, phone: str, email:str, address: str):
        if name in self.contacts:
            print('Contact exists.')

        else:
            # self.contacts[name] = {
            #     'phone': phone,
            #     'email': email, 
            #     'address': address
            # }   
            self.contacts[name] = {}
            self.contacts[name]['phone'] = phone
            self.contacts[name]['email'] = email
            self.contacts[name]['address'] = address

            print('Contact added')
            print('-'*50)

    def view_contacts(self):
        for name, info in self.contacts.items():
            print("Name:", name)
            print("Phone:", info['phone'])
            print("Email:", info['email'])
            print("Address:", info['address'])
            print('-'*50)

    def update_contact(self, name:str, phone: str = None, email: str = None, address: str = None):
        if name in self.contacts:
            # self.contacts[name] = {
            #     'phone': phone,
            #     'email': email,
            #     'address': address
            # }
            if phone:
                self.contacts[name]['phone'] = phone
            if email:    
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            print('Conract updated')  
            print('-'*50)  
            return

        print('Contact not found!')     

    def delete_contact(self, name: str):
        if name in self.contacts:
            del self.contacts[name]
            print('Contact deleted')
            return
        print('Contact not found')
        