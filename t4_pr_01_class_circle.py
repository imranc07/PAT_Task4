'''
Q1: Create a program class called circle with constructor which will take a list as an argument for the task.
The List is[10,501,22,37,100,999,87,351]
'''

'''
Input = list as an argument for class circle
logic = class Circle with constructor, instance variable and instance method
Output = print (class Circle with given list as an argument)
'''

# Circle Class
class Circle:
    def __init__(self):

        # Intializing instance variables
        self.num = [10,501,22,37,100,999,87,351]

    # Method to read and print number
    def read_number(self):
        print(self.num)

# Creating an object circle1   
circle1 = Circle()

# calling instance method using object circle1
circle1.read_number()