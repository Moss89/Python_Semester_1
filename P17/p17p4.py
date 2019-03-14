"""
Prompt the user for a string, empty to exit.
If the string is not empty, pass it as an argument to isPalindrome.
If isPalindrome is true, print out this fact. Otherwise print out it's false.
Prompt user for another string.

"""

def isPalindrome(s):
    """
    :param s: string
    :return: First call is to def toChars(s), which returns the inputted
    string in lower case and only letters.
    Second call is to isPal, which returns true is len(s) <=1,
    otherwise it returns s[0] == s[-1] and isPal(s[1:-1])
    isPalindrome returns isPal(toChars(s))
    """
    def toChars(s):
        s = s.lower()
        letterstring = ""
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterstring += c
        return letterstring
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))

str = input("Enter a string, empty to exit: ")

while str != "":
    if isPalindrome(str):
        print(str, "is a palindrome!")
    else:
        print(str, "is not a palindrome!")

    str = input("Enter a string, empty to exit: ")
print("Finished!")
