# This program defines the email prefix of the entered email without the numbers that could be entered after the user-name of the email
# If you enter not an email, this program will tell you that.
# Was created using 'for' loop and 'time' module :D

import time
email = input("Enter your email: ").lower()
while not ("@" in email and ".com" in email):
    print("You didn't enter email.")
    email = input("Enter your email again: ").lower()
original_email = list(email)
transformed_email = []
for row in original_email:
    if row == "@":
        break
    if row.isdigit():
        break
    new_row = str(row)
    transformed_email.append(new_row)
new_email = "".join(transformed_email)

def send_email():
    return f"Hello {new_email}!"

print("Loading...")
time.sleep(1.5)
print(send_email())
