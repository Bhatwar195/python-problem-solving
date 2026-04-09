def fact(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return False
    else:
        # Correct recursive step: n * fact(n-1)
        return n * fact(n-1)


#Test 
n=int(input("Enter the Number for factorial ::"))
print(f"Factrorial of {n} is",fact(n))