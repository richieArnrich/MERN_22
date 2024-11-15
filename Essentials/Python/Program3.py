# boolean operators in python
# and, or, not
# and operator returns True if both conditions are met
# or operator returns True if at least one condition is met
# not operator returns True if the condition is False

#  <= lesser than or equal to
#  >= greater than or equal to
#  == equal to
#  != not equal to
#  < lesser than
#  > greater than
#  in operator checks if a value is present in a sequence (like a list or a string)

a = 10
b = 20
result1 = a<b
print(result1) # True
result2 = a>b 
print(result2) #False

a = 7
b = 10
result1 = (a<=b) #True
result2 = (a>=b) #False

#and operator
#Syntax: (condition1) and (condition2)
a = 8
b = 7
c = 6

andResult = (c<a) and (a>b)
print(andResult)

# or operator 
# Syntax: (condition1) or (condition2)
orResult = (c>a) or (a>b)
print(orResult)

# in operator
# Syntax: (value) in (sequence)
str = "Mango"
print("z in mango",'z' in str)

list = ["Mango", "Apple", "Banana"]

print("Berry" in list)

# not operator
# Syntax: not (condition)
# It returns True if the condition is False and vice versa
str = "Apple"

print('p' not in str)