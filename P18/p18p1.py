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
 Second call is to isPal, i = 0, while i <= string length/2,
 if s[i] != s[-i - 1] return false, otherwise return true.
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
        print("isPal function called with argument", s)

        str_len = len(s)
        i = 0
        while i <= str_len // 2:
            if s[i] != s[-i - 1]:
                print(s[i], "and", s[-i-1])
                return False
            i += 1
        return True

    return isPal(toChars(s))

str = input("Enter a string, empty to exit: ")

while str != "":
    if isPalindrome(str):
        print(str, "is a palindrome!")
    else:
        print(str, "is not a palindrome!")

    str = input("Enter a string, empty to exit: ")
print("Finished!")
