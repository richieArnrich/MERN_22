# functions in python
# a block of code used to perform a specific task
# functions can take arguments, return values and be reused
# functions are defined using the def keyword

# create a function to print your name
def PrintMyName():
    # non parameterised function
    print("My name is John Doe")

# end of PrintMyName()

def PrintYourName(name):
    # parameterised function
    print("My name is " + name)

PrintMyName()
PrintMyName()
PrintYourName("Ajay")
PrintYourName("Tendulkar")