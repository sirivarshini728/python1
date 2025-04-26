def palindrome(string):
    # remove any spaces and convert the string to lowercase
    string = string.replace(" ", "").lower()
    # check if the string is equal to its reverse
    return string == string[::-1]

# example usage:
print(palindrome("madam"))  # Corrected typo in function call
print(palindrome("hello"))
print(palindrome("a man a plan a canal panama"))
