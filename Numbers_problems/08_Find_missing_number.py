# Find missing number in an array of size N (1 to N+1).

def missing_number(arr):
    array=arr
    maxx=max(arr)
    low=min(arr)
    for i in range(low,maxx):
        if i in array:
            continue
        else :
            print(i)  

# Test 
missing_number([1,2,4,5,6,8])

## Sum method 
def find_missing_number(arr):
    # N is the size of the array
    # The range of numbers is from 1 to N + 1
    n = len(arr)
    
    # Calculate expected sum of first N + 1 natural numbers
    # Formula: (total_count * (total_count + 1)) // 2
    total_count = n + 1
    expected_sum = (total_count * (total_count + 1)) // 2
    
    # Calculate the actual sum of elements in the array
    actual_sum = sum(arr)
    
    # The missing number is the difference
    return expected_sum - actual_sum

# Example usage:
my_array = [1, 2, 4, 5, 6]  # N = 5, missing number is 3
result = find_missing_number(my_array)
print(f"The missing number is: {result}")
