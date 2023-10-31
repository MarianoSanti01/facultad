class Schedule():
    def __init__(self) -> None:
        self.contacts = []
    def add_contact(self, name, phone, gmail):
        contact = {
            'name': name,
            'phone': phone,
            'gmail': gmail
        }
        self.contacts.append(contact)
    def show_contacts(self):
        if len(self.contacts) != 0:
            for contact in self.contacts:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Gmail: {contact['gmail']}")
                print()
        else:
            print('No tienes contactos para mostrar.')
    def search_contacts(self, to_search):
        contact_found = False
        for contact in self.contacts:
            if to_search.lower() == contact['name'].lower():
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Gmail: {contact['gmail']}")
                contact_found = True
        if not contact_found:
            print('El contacto no existe')
    def edit_contact(self, to_edit, new_name, new_phone, new_gmail):
        contact_found = False
        for contact in self.contacts:
            if to_edit.lower() == contact['name'].lower():
                contact['name'] = new_name
                contact['phone'] = new_phone
                contact['gmail'] = new_gmail
                print('Contacto editado con éxito')
                contact_found = True
        if not contact_found:
            print('El contacto no existe')