class Employee:
    def __init__(self, name, age, salary,contact):
        self.name = name
        self.age = age
        self.salary = salary
        self.contact = contact
    
    def printDetails(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Salary: ", self.salary)
        print("contact: ", self.contact)


Employee1 = Employee("Amith", 24,1000,123456)
Employee1.printDetails()

Employee2 = Employee("Sarah", 23, 1234,12346)
Employee2.printDetails()

# create a class shape, with attributes length and breadth
# create a function to find the area of a quadrilateral (rectangle)