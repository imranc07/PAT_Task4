'''
Q3: From the given List create two class Methods Area and Perimeter which will be going to calculate 
the Area and Perimeter.
'''

'''
Input = radius = [10,501,22,37,100,999,87,351]
logic = class Circle with constructor, for loop with range function, class methods area and perimeter)
Output = print (Area and Perimeter)
'''

# class circle
class circle():

    # constructor for circle
    def __init__(self, radius):

        # Radius attribute
        self.radius = radius
        self.pi=3.141

    # Method to calculate area of circle        
    def area(self):

        # Print area of circle of the given list
        print("\nThe area of circle of the given list is")

        # For loop with rage function and formula to calculate area of circle
        for i in range(8):
            print(self.pi*self.radius[i]*self.radius[i])

    # Method to calculate Perimeter of circle
    def perimeter(self):

        # Print perimeter of circle of the given list
        print("\nThe perimeter of circle of the given list is")

        # For loop with range function and formula to calculate perimeter of cicle
        for i in range(8):           
            print(2*self.pi*self.radius[i])

# Creating an object as circle1
circle1 = circle(radius = [10,501,22,37,100,999,87,351])

# Print the area output
print(circle1.area())

# Print the perimeter output
print(circle1.perimeter())