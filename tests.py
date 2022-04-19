# Import library
import unittest


# Class to contain functions used in the GUI
class func(object):
    # Initialize value of the functions to False
    def __init__(self):
        self.back = False
        self.ask = False
        self.output = False

    # Function for going back to previous page
    def go_back(self):
        # Reinitialize value of the function to True
        self.back = True
        print("Function to undo")

    # Function for asking user if they want to quit the program
    def ask_user(self):
        # Reinitialize value of the function to True
        self.ask = True
        print("Function to ask if user wants to quit")

    # Function for showing customer order details and allowing checking of order number
    def output_info(self):
        # Reinitialize value of the function to True
        self.output = True
        print("Function to show customer order details and allow checking of order number")


class TestGame(unittest.TestCase):
    # Testing the back function in func class
    def test_back(self):
        c = func()
        c.go_back()
        self.assertTrue(c.back, 'Expected Function for going back to previous page')

    # Testing the ask function in func class
    def test_ask(self):
        c = func()
        c.ask_user()
        self.assertTrue(c.ask, 'Expected Function for asking user if they want to quit the program')

    # Testing the ask function in func class
    def test_output(self):
        c = func()
        c.output_info()
        self.assertTrue(c.output, 'Expected Function for showing customer order details '
                                  'and allowing checking of order number')


# Call the main function
if __name__ == '__main__':
