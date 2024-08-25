'''
Q2: Create proper member variables inside the task if required and use them when necessary.For example for this task
create a class private variable named pi=3.141.
'''

'''
Input = radius and private variable pi
logic = class Circle with constructor,private variable pi, class methods area and perimeter)
Output = print (Area using private variable)
'''

# class circle
class circle():

    # constructor for circle
    def __init__(self, radius):

        # Radius attribute
        self.radius = radius

    # Method to calculate area of circle        
    def area(self):

        # Private variable pi in class circle()
        self.__pi = 3.141

        return self.__pi* self.radius**2
    
# Creating an object as circle1
circle1 = circle(2)

# Print the area of circle
print("\nThe area of circle by using private variable in class is", circle1.area())