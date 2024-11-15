# for loop in py
# range function

# for i in range(1,11):
    # print(i)
# end of for block

list = [1,2,5,6,7,90,23]

#  print the list using for loop
for i in list:
    print(i)

# end of for block

# given a list of integers write a py program to find the 
# max element in the list, list = [1,2,5,6,7,90,23]
# output: 90

max = 0
for i in list:
    if i>max:
        max = i
    # end of if
# end of for

print(f"maximum element is: {max}")