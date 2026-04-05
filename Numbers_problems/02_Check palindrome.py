# Check if a number is Palindrome 
# palindron -121 
# not a palindrom -123

def is_palindrom(n):
    n_string=str(n)

    if n_string == n_string[::-1] :
        return True
    else :
        return False
    
# Test 
n=int(input("Enter number to check::"))
x=is_palindrom(n)
if x == True :
    print("number is Palindrome")
else :
    print("Not a Palindrome")
