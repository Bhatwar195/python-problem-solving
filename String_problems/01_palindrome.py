def is_palindrome(s):
    s = s.lower()  # convert to lowercase
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

# Example
print(is_palindrome("Madam"))
print(is_palindrome("Hello"))