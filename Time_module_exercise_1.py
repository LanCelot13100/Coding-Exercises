# Here is the basic program that asks your login and password, BUT here I imported the 'time' module!
# This thing allowed me to delay some commands declared in the program itself
import time
login = input("Enter the login: ")
password = input("Enter the password: ")
correct_login = "Sally123"
correct_password = "12345678"
while login == correct_login and password == correct_password or login == correct_login and password != correct_password or login != correct_login and password == correct_password or login != correct_login and password != correct_password:
    if login == correct_login and password == correct_password:
        print("Data verification...")
        time.sleep(2)  # This line delays the next command on 2 seconds declared in parentheses as well as the other similar commands with 'time' do
        print("The login and password were entered right!")
        time.sleep(1)
        print("Loading...")
        time.sleep(2)
        print("Welcome!")

        break
    elif login == correct_login and password != correct_password:
        print("Data verification...")
        time.sleep(2)
        print("The password wasn't entered right.")
        password = input("Enter the password again: ")
    elif login != correct_login and password == correct_password:
        print("Data verification...")
        time.sleep(2)
        print("The login wasn't entered right.")
        login = input("Enter the login again: ")
    else:
        print("Data verification...")
        time.sleep(2)
        print("You didn't enter anything right.")
        login = input("Enter the login again: ")
        password = input("Enter the password again: ")

