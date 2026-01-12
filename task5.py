contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append([name, phone, email, address])
    print("Contact added!")

def view_contacts():
    if not contacts:
        print("No contacts.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c[0]} - {c[1]}")

def search_contact():
    key = input("Enter name or phone: ")
    for c in contacts:
        if key in c[0] or key in c[1]:
            print(c)
            return
    print("Not found.")

def update_contact():
    view_contacts()
    if not contacts:
        return
    i = int(input("Contact number: ")) - 1
    contacts[i] = [
        input("New name: "),
        input("New phone: "),
        input("New email: "),
        input("New address: ")
    ]
    print("Updated!")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    i = int(input("Contact number: ")) - 1
    contacts.pop(i)
    print("Deleted!")

while True:
    print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
    ch = input("Choose: ")

    if ch == "1":
        add_contact()
    elif ch == "2":
        view_contacts()
    elif ch == "3":
        search_contact()
    elif ch == "4":
        update_contact()
    elif ch == "5":
        delete_contact()
    elif ch == "6":
        break
    else:
        print("Invalid choice")