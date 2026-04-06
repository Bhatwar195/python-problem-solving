# Count number of digits in a number (without string)

def count(n):
    if n==0 :
        return 1
    count_n=0

    n=abs(n)
    while n > 0:
        count_n+=1
        n=n//10
    return count_n

n=int(input("Enter number ::"))
print("Number of digits ::",count(n))

# Find sum of digits of a number

def sumation(n):

    if n==0 :
        return 0
    digit=0
    sum=0
    n=abs(n)
    while n>0:
        digit=n%10
        sum=sum+digit
        n=n//10
    return sum 

n=int(input("Enter number ::"))
print("sum of digits ::",sumation(n))
