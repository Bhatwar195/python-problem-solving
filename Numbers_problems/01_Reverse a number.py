# Reverse digits of an integer without string 

def reversed(n):
    x=0
    rev=0

    while n > 0:
        x=n%10
        n=n//10
        rev=rev*10+x
    return rev

# Test 
n=int(input("Enter number to reversed ::"))
print("Before reversed :: ",n)
print("After reversed  ::",reversed(n))