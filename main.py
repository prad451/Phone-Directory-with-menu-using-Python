contact = {}

def display_contact():
    print("These are the all contacts of my phone directory...")
    print("Name\t\tContact number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
        
while True:
    print("**********Phone Directory**********")
    choice = int(input(" 1.Add new contact \n 2.Update contact \n 3.Delete contact \n 4.Show a given name contact \n 5.Show all contact \n Enter your choice : "))
    
    if choice == 1:
        name = input("Enter the contact name : ")
        phone = input("Enter the mobile number : ")
        contact[name] = phone
        print("Contact is created successfully in your phone directory : ","\nName: {}, \nPhone Number: {}".format(name, phone))
    
    elif choice == 2:
        update_contact = input("Enter the contact which you want to update : ")
        if update_contact in contact:
            phone = input("Enter the mobile number : ")
            contact[update_contact] = phone
            print("Contact is successfully updated!")
            display_contact()
        else:
            print("Contact name is not found in phone directory")
    
    elif choice ==3:
        del_contact = input("Enter the contact which you want to delete : ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n")
            if confirm=='y' or confirm=='Y':
                contact.pop(del_contact)
            display_contact()
            print("Contact is deleted successfully!")
        else:
            print("Contact name is not found in phone directory")
    
    elif choice == 4:
        search_name = input("Enter the contact name : ")
        if search_name in contact:
            print("Name: {}, Phone Number: {}".format(search_name, phone))

        else:
            print("Contact is not found in phone directory")
   
    elif choice == 5:
        if not contact:
            print("Phone directory is empty")
        else:
            display_contact()
    else:
        print("Ooops...You have entered wrong choice!!")
        break
        