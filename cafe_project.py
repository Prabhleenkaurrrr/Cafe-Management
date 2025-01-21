def menu():
    m = {"Maggi": 40, "Sandwich": 60, "Cutlet": 50, "Pasta": 160, "Momos": 80, "Paneer Roll": 100}
    print("Menu: ")
    for item, price in m.items():
        print(f"{item}: Rs {price}")

def conti():
    print("Press C to continue")
    print("Press E to exit")
    j = input("Give the input: ").lower()
    if j == 'c':
        choice()
    else:
        print("Thank you for ordering.")

def validation(contact):
    if contact.isdigit() and len(contact) == 10:
        return True
    return False

def me(a):  
    name = []  
    order = [] 

    if a == 1:
        menu() 
        e = input("Enter your name: ")
        name.append(e)  
        s = input("Enter the item you want to order: ").lower()
        
        menu_items = {"maggi", "sandwich", "cutlet", "pasta", "momos", "paneer roll"}
        
        if s in menu_items:  
            order.append(s)
            print(f"{name[0]} ordered {order[0]}.")
            conti()
        else:
            print("The item you entered is not available in the menu.")
    elif a == 2:
        booking = {}
        name = input("Enter your name: ")
        day = input("Enter the day for booking: ")
        members = int(input("Enter the number of members: "))
    
        contact = int(input("Enter the contact number: "))
        if not validation(contact):
            print("Invalid contact number. Please enter a valid 10-digit number.")
        else:
            booking['name'] = name
            booking['day'] = day
            booking['members'] = members
            booking['contact'] = contact
            print(f"Booking confirmed for {booking['name']} on {booking['day']} for {booking['members']} members. Contact: {booking['contact']}")
            conti()
    else:
        print("Please enter a valid input")

def choice():
    print("Press 1 to order")
    print("Press 2 for booking")
    a = int(input("Enter the choice: "))
    if a in [1, 2]:
        me(a)
    else:
        print("Invalid choice. Please try again.")
        choice()
        
choice()
