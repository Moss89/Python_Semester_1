'''

The program checks to see if the user has inputted the correct password. If they haven't, they must enter the correct
password three times in a row to log in. If they fail to do so, access is denied.

Steps:

Store password in password variable. Set right password count to 0, and attempts to 0.

Take inputted string from user.

If the inputted string = the password, print log in success message.

Else print that the password is wrong.

While the attempts to enter the password is lower than 3, we ask the user to input the password again and increment the
attempts variable.

If password = the user input, then the right password attempts variable is incremented.

If the right password attempts = 3, print a log in success message. Else, print an access denied message.
'''

password = "turnipman"
right_pw_count = 0
attempts = 0

user_input = input("Please enter your password: ")

if user_input == password:
    print("You have successfully logged in")

else:
    print("Sorry, the password is wrong")
    while attempts < 3:
        attempts += 1
        user_input = input("Please enter your password: ")
        if user_input == password:
            right_pw_count += 1

    if right_pw_count == 3:
        print("You have successfully logged in")

    else:
        print("You have been denied access")


