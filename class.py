# Define Class
class Contact_Details:

    def __init__(self, name, mobile_number, email, address):
        self.contact_name = name
        self.contact_number = mobile_number
        self.email = email
        self.contact_address = address

        # Make a dictionary of the contact details 
        self.person = {
            "name": self.contact_name,
            "mobile" : self.contact_number,
            "email": self.email,
            "address": self.contact_address,
            "dob": 1234

        } 

    # Define the Methods of the class
    
    # View All Contact Details
    def view_contact_details(self, contact_list):
      print(contact_list)
      

    # Add the contact details to the list    
    def add_contact_details(self, contact_list):
      contact_list.append(self.person)
new_contact = Contact_Details("dev",123456789,'abc@gmail.com',  "address": self.contact_address,
            "dob": 1234
)
print(new_contact)


phonebook_list=[]
new_contact = Contact_Details("dev",123456789,'abc@gmail.com',  "address": self.contact_address, "dob": 1234)

new_contact.add_contact_details(phonebook_list)
[{"name" : "Dev", "mobile" : 1234567890, "email" : "abc@gmail.com","Address" : " acb 123", 
            "dob": 1234
}]