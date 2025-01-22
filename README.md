# 📖 **README: Cafe Management Program** ☕🍴

Welcome to the **Cafe Management Program**! This Python script is designed to manage a cafe's basic functionalities, such as taking orders and booking reservations. It's interactive, user-friendly, and ensures a smooth process for both customers and staff. 🎉

---

## 🚀 **Features**
1. **📜 Display Menu**  
   Easily view the cafe's menu with prices.
2. **🍽️ Place Orders**  
   Customers can select items from the menu and place an order.  
3. **📅 Make Reservations**  
   Book a table for a specific day and number of members.
4. **✅ Contact Validation**  
   Ensures accurate 10-digit contact numbers for booking.

---

## 🛠️ **How to Use**
1. **Start the Program**  
   Run the script, and the main menu will be displayed with two options:
   - `1` → Place an Order  
   - `2` → Make a Reservation  

2. **Order Process**  
   - Enter your name.  
   - Choose an item from the menu.  
   - If the item exists, your order will be confirmed. If not, you'll be prompted with an error message.

3. **Reservation Process**  
   - Provide your name, the day for booking, the number of members, and a valid 10-digit contact number.  
   - If the contact number is valid, the reservation will be confirmed.

4. **Continue or Exit**  
   After completing an action, you can choose to:
   - **Continue** (`Press C`)  
   - **Exit** (`Press E`)  

---

## 📋 **Menu**  
| 🍴 **Item**      | 💰 **Price** |
|-------------------|-------------|
| Maggi            | Rs 40       |
| Sandwich         | Rs 60       |
| Cutlet           | Rs 50       |
| Pasta            | Rs 160      |
| Momos            | Rs 80       |
| Paneer Roll      | Rs 100      |

---

## 💡 **Code Highlights**
- **`menu()`**  
  Displays the menu items and prices.
  
- **`conti()`**  
  Allows users to continue or exit the program.  
  
- **`validation(contact)`**  
  Ensures contact numbers are 10-digit and numeric.  
  
- **`me(a)`**  
  Handles ordering and booking based on user choice.  
  
- **`choice()`**  
  Main menu that directs users to ordering or booking.

---

## 🛑 **Error Handling**
- Invalid menu item? Get a clear message: `"The item you entered is not available in the menu."`  
- Incorrect contact number? `"Invalid contact number. Please enter a valid 10-digit number."`  
- Invalid choice? `"Invalid choice. Please try again."`

---

### ✨ **Try it Now!**  
Launch the program and experience seamless cafe management! 🌟

