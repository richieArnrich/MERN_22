class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    
    def area_shape(self):
        area = self.length*self.breadth
        print(area)
    
    def perimeter(self):
        perimeter = 2*(self.length + self.breadth)
        print(perimeter)

shape1 = Shape(4,4)
shape1.area_shape()

shape2 = Shape(10,5)
shape2.area_shape()

# define a function to find perimeter of a rectangle