def digit_frequency(n):
    freq = {}
    
    n = abs(n)  # handle negative numbers
    
    while n > 0:
        digit = n % 10
        freq[digit] = freq.get(digit, 0) + 1
        n //= 10
    
    return freq


## Test
n=int(input("Enter the no for count ::")) 
print(digit_frequency(n))