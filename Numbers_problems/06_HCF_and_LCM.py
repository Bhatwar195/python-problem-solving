"""The Greatest Common Divisor (GCD) is primarily known as the Highest Common Factor (HCF). It is also commonly referred to as the Greatest Common Factor (GCF). Both terms represent the largest positive integer 
that divides two or more non-zero integers without leaving a remainder. """

def hcf(a,b):
    
    while b > 0:
        r=a%b # r=(12%8)=4 #r=0
        a=b   # a=8  # a=4
        b=r   # b=4  # 0 loop end 
    return a 

#Test 
a=int(input("Enter the number for GCD ::"))
b=int(input())
print("GCD::",hcf(a,b))


### LCM=(a*b)/GCD

def lcm(a,b):
    t1,t2=a,b
    while b > 0:
        r=a%b # r=(12%8)=4 #r=0
        a=b   # a=8  # a=4
        b=r   # b=4  # 0 loop end 
    GCD=a
    lcm=(t1*t2)/GCD
    return lcm
#Test 
a=int(input("Enter the number for GCD ::"))
b=int(input())
print("GCD::",lcm(a,b))
