import mysql.connector as mysql
from datetime import date

db = mysql.connect(host="localhost",user="root",password="1208",database="LPG")
mycursor = db.cursor(buffered=True)

def admin_session():
    while 1:
        print("")
        print("Admin Menu")
        print("1. Register new Customer")
        print("2. Delete Existing Customer")
        print("3. Update Existing Customer")
        print("4. Show all Customers")
        print("5. Search specific Customer")
        print("6. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Register New Customer")
            username = input(str("Create Customer username : "))
            password = input(str("Create Customer password : "))
            name = input(str("Enter Customer Name : "))
            address = input(str("Enter Customer Address : "))
            phone = input(str("Enter Customer Phone No. : "))
            email = input(str("Enter Customer Email : "))
            proof = input(str("Enter Address Proof of Customer (Aadhar/Passport/DL/Voter ID) : "))
            proof_no = input(str("Enter Customer Proof Number : "))
            query_vals = (username, password, name, address, phone, email, proof, proof_no)
            mycursor.execute("INSERT INTO customers (Username, Password, Name, Address, Phone_No, Email, ID_Proof, ID_Proof_No) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",query_vals)
            db.commit()
            print(username + " has been registered as a customer")
            
        elif user_option == "2":
            print("")
            print("Delete Existing Customer Account")
            cust_id = input("Enter Customer's ID : ")
            mycursor.execute("DELETE FROM customers WHERE Customer_ID = '"+cust_id+"';")
            db.commit()
            if mycursor.rowcount < 1:
                print("User not found")
            else:
                print(cust_id, " has been deleted")
        
        elif user_option == "3":
            print("")
            print("Update Existing Customer Account")
            cust_id = input("Enter Customer's ID : ")
            print("")
            print("Choose which field you want to change.")
            print("1.   Customer Name")  
            print("2.   Customer Address")
            print("3.   Customer's Phone Number")
            print("4.   Customer's Email ID")
            print("5.   Customer's Password")
            choice = int(input('Enter your choice :'))
            field_name =''
            if choice == 1:
                field_name='Name'
            if choice == 2:
                field_name='Address'
            if choice == 3:
                field_name='Phone_No'
            if choice == 4:
                field_name='Email'
            if choice == 5:
                field_name='Password'
            value = input('Enter new value :')
            mycursor.execute('UPDATE customers SET '+field_name+ '="' +value+ '" WHERE Customer_ID = '+cust_id+';')
            db.commit()
            print(mycursor.rowcount, "record(s) affected")
            
        elif user_option == "4":
            mycursor.execute("SELECT * FROM customers")
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)

        elif user_option == "5":
            print("Search Customer DataBase")
            print("")
            print("Search By:")
            print("1.  Customer's Name")
            print("2.  Customer's Address")
            print("3.  Customer's Phone")
            print("4.  Customer's Email")
            print("5.  ID Proof")
            print("6.  ID Proof No.")
            print("7.  Customer's Username")
            choice = int(input('Enter your choice : '))
            field_name =''
            if choice == 1:
              field_name = "Name"
            if choice == 2:
              field_name = "Address"
            if choice == 3:
              field_name = "Phone_No"
            if choice == 4:
              field_name = "Email"
            if choice == 5:
              field_name = "ID_Proof"
            if choice == 6:
                field_name = "ID_Proof_No"
            if choice == 7:
                field_name = "Username"

            value = input('Enter value that you want to search :')
            if field_name =='ID_Proof_No':
                sql = 'SELECT * FROM customers WHERE '+field_name +' = '+ value + ';'
            else:
                sql = 'SELECT * FROM customers WHERE ' +field_name + ' like "' + value + '";'
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)

        elif user_option == "6":
            break
        else:
            print("No valid option selected")

def customer_session():
    while 1:
        print("")
        print("Customer's Menu")
        print("1. Book LPG")
        print("2. Update Information")
        print("3. View information")
        print("4. Logout")
    
        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            print("Cost of 1 LPG is 650 Rupees")
            print("You need your Customer ID to book LPG, If you don't remember your ID then go back and view your Information")
            cust_id = input("Enter Customer's ID : ")
            date_of_issue = input("Enter date of booking (yyyy-mm-dd) :")
            mycursor.execute("UPDATE customers SET Last_Issued_Date ='" +date_of_issue+ "' WHERE Customer_ID = '"+cust_id+"';")
            db.commit()
            print(mycursor.rowcount, "record(s) affected")

        elif user_option == "2":
            print("")
            print("Update your Account Information")
            cust_id = input("Enter Customer's ID : ")
            print("")
            print("Choose which field you want to change.")
            print("1.   Your Name")
            print("2.   Your Address")
            print("3.   Your Phone Number")
            print("4.   Your Email ID")
            print("5.   Your Password")
            choice = int(input('Enter your choice :'))
            field_name =''
            if choice == 1:
                field_name='Name'
            if choice == 2:
                field_name='Address'
            if choice == 3:
                field_name='Phone_No'
            if choice == 4:
                field_name='Email'
            if choice == 5:
                field_name='Password'
            value = input('Enter new value :')
            mycursor.execute('UPDATE customers SET '+field_name+ '="' +value+ '" WHERE Customer_ID = "'+cust_id+ '";')
            db.commit()
            print(mycursor.rowcount, "record(s) affected")

        elif user_option == "3":
            username = input(str("Username : "))
            password = input(str("Password : "))
            query_vals = (username, password)
            mycursor.execute("SELECT * FROM customers WHERE Username = %s AND Password = %s",query_vals)
            if mycursor.rowcount <= 0:
                print("Wrong Credentials")
            else:
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
            
        elif user_option == "4":
            break
        else:
            print("No valid option selected")
            
def new_customer_session():
    while 1:
        print("")
        print("1. Add your informations")
        print("2. Exit")
    
        user_option = input(str("Option : "))
        if user_option == "1":
            print("Add your informations")
            username = input(str("Create Your Username : "))
            password = input(str("Create Your Password : "))
            name = input(str("Enter your Name : "))
            address = input(str("Enter your Address : "))
            phone = input(str("Enter your Phone No. : "))
            email = input(str("Enter your Email : "))
            proof = input(str("Enter Address Proof you are providing(Aadhar/Passport/DL/Voter ID) : "))
            proof_no = input(str("Enter your Proof Number : "))
            query_vals = (username, password, name, address, phone, email, proof, proof_no)
            mycursor.execute("INSERT INTO customers (Username, Password, Name, Address, Phone_No, Email, ID_Proof, ID_Proof_No) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",query_vals)
            db.commit()
            print(username + " has been registered as a customer")
            mycursor.execute('SELECT Customer_ID FROM customers WHERE ID_Proof_No = ' +proof_no+ ';')
            myresult = mycursor.fetchall()
            for x in myresult:
                print("This is your Customer ID : ",x)
            print("Note your Username and Password and keep it remembered because it will be used in further works")    
            print("Now Exit and login as Customer to book your LPG")

        elif user_option == "2":
            break
        else:
            print("No valid option selected")


def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised")

def auth_customer():
    print("")
    print("Customer's Login")
    print("")
    username = input(str("Enter Your Username : "))
    password = input(str("Enter Your Password : "))
    query_vals = (username,password)
    mycursor.execute("SELECT * FROM customers WHERE Username = %s AND Password = %s",query_vals)
    if mycursor.rowcount <= 0:
        print("Login not recognized")
    else:
        customer_session()

def main():
    while 1:
        print("-"*50)
        print("Welcome to the LPG Booking system")
        print("")
        print("1. Login as Customer")
        print("2. Register as New Customer")
        print("3. Login as Admin")

        user_option = input(str("Option : "))
        if user_option == "1":
            auth_customer()
        elif user_option == "2":
            new_customer_session()
        elif user_option == "3":
            auth_admin()
        else:
            print("No valid option was selected")

main()