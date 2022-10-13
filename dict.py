# Mapping Data Types

name = "dev"
print(type(name))

info = []
print(type(info))

person = {

}
print(type(person))


person = {
    "name" : "Dev",
    "mobile" : 1234567890,
    "email" : "abc@gmail.com",
    "Address" : " acb 123"
}

print(person["name"])
print(person["email"])

new_contact = Contact_Details("dev",123456789,'abc@gmail.com')
print(new_contact)


phonebook_list=[]
new_contact = Contact_Details("dev",123456789,'abc@gmail.com')

new_contact.add_contact_details(phonebook_list)
[{"name" : "Dev", "mobile" : 1234567890, "email" : "abc@gmail.com","Address" : " acb 123"}]