# write a py function to reverse a number
# input: 1345  output: 5431

def reverse_number(number):
    n = number
    rev = 0
    while(n!=0):
        last = n%10
        rev = rev*10 + last
        n =int(n/10)
    
    print(f"reverse of {number} is {rev}")
    
    if rev == number:
        print("it is pallindrome")
    else:
        print("it is not pallindrome")

reverse_number(1551)