"""An Armstrong number (also called a narcissistic number) is a number that equals the sum of its own digits
, with each digit raised to the power of the total number of digits."""

"""3-Digit Number (Power of 3):
For 153, there are 3 digits.(Yes)."""

"""4-Digit Number (Power of 4):
For 1634, there are 4 digits.
 (Yes)."""


def is_armstrong(n):
    
    if n <= 9:
        return True
    
    original_sum=n
    count=len(str(n))
    n=abs(n)
    digit=0
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit**count
        n=n//10
    if original_sum==sum :
        return True
    else :
        return False
    
n=int(input("Enter number ::"))
print("is Armstron  ::",is_armstrong(n))