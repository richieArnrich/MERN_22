class Student:
    # constructor
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact
    
    def printDetails(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("contact: ", self.contact)

# end of student class

# create an object of the class

student1 = Student("Ankit", 20,1234567890)
print(student1.name)
print(student1.age)
print(student1.contact)

student2 = Student("Amith", 22, 567890122)
print(student2.name)
print(student2.age)
print(student2.contact)

# create a class employee with attributes 
# name,age,salary,contact and print the values