'''
    The program compares the user inputted string against the stored password, and if they are equal, the user receives
    a successful message, otherwise they get 3 more attempts to try. More than 3 wrong attempts (4) gives the user an
    access denial message.

    Steps:

    Wrong password count starts at zero, and the password is set.
    The user inputted string is stored.
    If the user inputted string and the password are equal, print "You have successfully logged in"
    Otherwise, while the user inputted string doesn't equal the password, and the wrong password count is less than 4,
    the user is prompted to enter the password again and the wrong password attempts variable is incremented.
    If the wrong password count is equal to 4 (more than 3 failed attempts), then print "You have been denied access".

'''

password = "turnipman"
wrong_pw_count = 0

user_input = input("Please enter your password: ")

while user_input != password and wrong_pw_count < 4:
        wrong_pw_count += 1
        if wrong_pw_count == 4:
            print("You have been denied access")
        else:
            user_input = input("Please enter your password: ")

if user_input == password:
    print("You have successfully logged in")