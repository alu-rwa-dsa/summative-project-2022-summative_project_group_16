# Importing the necessary modules
import ast
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk() #Defining a variable that stores a called tkinter function
root.title("E-commerce Order App") # Adding the title to the UI
root.geometry("1280x720") #Defining the dimensions of our GUI
title = Label(root, text='Online Shirt Order App', bg='white', fg='black', # Defining the dimensions and style of our title
              font=('Montserrat', 30, 'bold'), relief=GROOVE, bd=12)
title.pack(fill=X)

# Creating the first frame where user information will appear
Frame_1 = Frame(root, relief=RIDGE, bd=10, bg='black')
Frame_1.place(x=10, y=80, width=650, height=530)

# Creating the second frame where the user order number will be displayed
Frame_2 = Frame(root, bg="white", relief=RIDGE, bd=10)
Frame_2.place(x=665, y=80, width=610, height=530)

# Defining user input type and storing them in variables
name = StringVar()
address = StringVar()
email = StringVar()
shirt = StringVar()
size = StringVar()
number = IntVar()

# Asking the user to enter his/her name in the user interface
lbl_1 = Label(Frame_1, text="Enter Full name:", font=('Montserrat', 15, 'bold'), fg='white',
              bg='black')
lbl_1.grid(row=0, column=0, padx=30, pady=10) # Defining the style and dimentions of the prompt
# An input box where the user enters the name and its dimensions
txt_1 = Entry(Frame_1, font=('Montserrat', 15, 'bold'), relief=RIDGE, bd=7, textvariable=name)
txt_1.grid(row=0, column=1, pady=10, sticky='w')

# Prompt the user to enter their address, defining the style(how it will appear to the user)
lbl_2 = Label(Frame_1, text="Enter Your Address:", font=('Montserrat', 15, 'bold'), fg='white',
              bg='black')
lbl_2.grid(row=1, column=0, padx=30, pady=10)
# A textbox where the user enters his/her address with its dimensions and sytles
txt_2 = Entry(Frame_1, font=('Montserrat', 15, 'bold'), relief=RIDGE, bd=7, textvariable=address)
txt_2.grid(row=1, column=1, pady=10, sticky='w')

# Prompt the user to enter their email, defining the style(how it will appear to the user) 
lbl_3 = Label(Frame_1, text="Enter Your Email:", font=('Montserrat', 15, 'bold'), fg='white',
              bg='black')
lbl_3.grid(row=2, column=0, padx=30, pady=10)
# A textbox where the user enters his/her email with its dimensions and sytles
txt_3 = Entry(Frame_1, font=('Montserrat', 15, 'bold'), relief=RIDGE, bd=7, textvariable=email)
txt_3.grid(row=2, column=1, pady=10, sticky='w')

# Prompt the user to choose a shirt type, defining the style(how it will appear to the user) 
lbl_4 = Label(Frame_1, text="Choose Shirt Type:", font=('Montserrat', 15, 'bold'), fg='white',
              bg='black')
lbl_4.grid(row=3, column=0, padx=30, pady=10)
# A combo box where the user choose a shirt type with its dimensions and sytles
combo_1 = ttk.Combobox(Frame_1, font=('Montserrat', 15), state='readonly', textvariable=shirt)
combo_1['value'] = ('Plain', 'Floral', 'Short Sleeve Shirt', 'Flannel Shirt', 'Dress Shirt')
combo_1.grid(row=3, column=1, pady=10)

# Prompt the user to choose size, defining the style(how it will appear to the user) 
lbl_5 = Label(Frame_1, text="Choose Your Size:", font=('Montserrat', 15, 'bold'), fg='white',
              bg='black')
lbl_5.grid(row=4, column=0, padx=30, pady=10)
# A combo box where the user choose size with its dimensions and sytles
combo_2 = ttk.Combobox(Frame_1, font=('Montserrat', 15), state='readonly', textvariable=size)
combo_2['value'] = ('X-Large', 'Large', 'Medium', 'Small', 'X-Small')
combo_2.grid(row=4, column=1, pady=10)
# Creating a global variable to store the user information in a dictionary
hashed_dict = {}  # creating a global variable to


# Defining a function to collect user information
def hashmap():
    global hashed_dict # using our global dict
    # Using .get() to collect information inputed on the frontend
    user = name.get()
    user_address = address.get()
    user_email = email.get()
    shirt_type = shirt.get()
    shirt_size = size.get()
    # Creating our dictionary
    
    # Handling any user error that might occur while user input data
    if user == '':
        Error()
    elif user_address == '':
        Error()
    elif user_email == '':
        Error()
    elif shirt_type == '':
        Error()
    elif shirt_size == '':
        Error()
    else:
      # Storing data in a dictionary when an error does not occur
        order_dict = {}
        for variables in ["user", "user_address", "user_email", "shirt_type", "shirt_size"]:
            order_dict[variables] = eval(variables)
        
        # A variable that generates a random numbers(will be used for order number)
        order_no = random.randint(0, 1000)

        # Creating a random number to identify orders and making sure that the number does not exist in our files
        while order_no in hashed_dict:
            order_no = random.randint(0, 1000)
        
        # Defining a message that will be sent to the users screen
        msg.config(text="Your Order Number is " + str(order_no))
        # Storing the order number and the user information in a dictionary
        hashed_dict = {order_no: order_dict}
        # Calling the orderDetails and filing() function
        orderDetails()
        filing()

# Defining a function that helps us store data in a file
def filing():
    global hashed_dict
    # Opening the order_data.txt in append mode( to make sure that we do not delete any data from the file)
    order_data = open("order_data.txt", 'a')
    # Writing the user details with their respective order numbers to the dictionary
    order_data.write(str(hashed_dict))
    order_data.write("\n")
    order_data.close()


# How the customer tracks the order
def orderProgress():
    # Collecting the order number inputted by the user
    order_no = number.get()
    # Opening our file system where all the orders have been stored
    order_details = open("order_data.txt", 'r')
    # Looping through it then converting it to a dictionary
    for no in order_details.readlines():
        values = ast.literal_eval(no)
        if order_no in values.keys():  # Find out if the order number exists in our system.

            Frame_4 = Frame(root, bg="white", relief=RIDGE, bd=10)
            Frame_4.place(x=10, y=80, width=1260, height=530)

            view = Label(Frame_4, font=('Montserrat', 20, 'bold'), fg='black',
                         bg='white')
            view.grid(row=0, column=0, padx=150, pady=10)
            view_0 = Label(Frame_4, font=('Montserrat', 20, 'bold'), fg='black',
                           bg='white')
            view_0.grid(row=1, column=0, padx=150, pady=10)

            view.config(text='Your order is being Processed')
            view_0.config(text="Here are your Details")
            count = 2
            # Looping through the dictionary and assigning values to be printed
            for n, k in values[order_no].items():
                view_1 = Label(Frame_4, font=('Montserrat', 15, 'bold'), fg='black',
                               bg='white')
                view_1.grid(row=count, column=0, padx=30, pady=10)
                view_1.config(text=n + " : " + k)
                count += 1

    order_details.close()


# function to display error if the user leaves an empty field
def Error():
    messagebox.showerror('Empty Fields', 'Do not fill any fields empty!')

# Creating the order details function
def orderDetails():
    # Getting user information and displalying it to the user
    user = name.get()
    user_address = address.get()
    user_email = email.get()
    shirt_type = shirt.get()
    shirt_size = size.get()
    # Using the config() function to display the user information
    out.config(text='Customer Order Details')
    out_1.config(text='Customer Name: ' + str(user))
    out_2.config(text='Customer Address: ' + str(user_address))
    out_3.config(text='Customer Contact: ' + str(user_email))
    out_4.config(text='Shirt Type: ' + str(shirt_type))
    out_5.config(text='Shirt Size: ' + str(shirt_size))
    
    # Defining  a check order button with its styling and dimensions
    check_button = Button(Frame_3, text='Check Order', font=('Arial', 15, 'bold'), bg='yellow',
                          fg='black', width=20, command=check)
    check_button.grid(row=0, column=1, padx=130, pady=15)
    
    # coping the information to a text file
    txt_file = open("order.txt", "w")
    txt_file.write("Customer name: " + str(user))
    txt_file.write("\nCustomer Address: " + str(user_address))
    txt_file.write("\nCustomer Contact: " + str(user_email))
    txt_file.write("\nShirt Type: " + str(shirt_type))
    txt_file.write("\nShirt Size: " + str(shirt_size))
    txt_file.close()

# Calling the hashmap
def output():
    hashmap()

# Defining a function to check whether the user wants to quit or not
def ask():
    # Quit if the user wants to quit otherwise just display the same page
    ans = messagebox.askquestion("Confirm Exit", "Do you really want to exit?")
    if ans == "yes":
        root.quit()

# A function to define the details on our user interface
def check():
    # A frame to display user information
    Frame_4 = Frame(root, bg="black", relief=RIDGE, bd=10)
    Frame_4.place(x=10, y=80, width=1260, height=530)
    # Defining dimensions and style
    lbl = Label(Frame_4, text="Enter Order Number:", font=('Montserrat', 15, 'bold'), fg='white',
                bg='black')
    lbl.grid(row=0, column=0, padx=30, pady=10)
    
    txt = Entry(Frame_4, font=('Montserrat', 15, 'bold'), relief=RIDGE, bd=7, textvariable=number)
    txt.grid(row=0, column=1, pady=10, sticky='w')
    # Defining a submit button with its styles for the user to enter data
    enter = Button(Frame_4, text='Submit', font=('Arial', 12, 'bold'), bg='yellow',
                   fg='black', command=orderProgress)
    enter.grid(row=0, column=2, padx=10, pady=15)
    
    # A function to allow the user to go back to the home page
    def back():
        Frame_1.tkraise()
        Frame_2.tkraise()
        Frame_4.destroy()
    # Defining the back button with its dimensions and style
    back = Button(Frame_3, text='Go Back', font=('Arial', 15, 'bold'), bg='yellow',
                  fg='black', command=back, width=20)
    back.grid(row=0, column=2, padx=10, pady=15)
    Frame_4.tkraise()

# Defining the dimensions of the order number message that will appear to the user
msg = Label(Frame_2, font=('Montserrat', 15, 'bold'), fg='black',
            bg='white')
msg.grid(row=8, column=0, padx=150, pady=10)
# Dimensions and sytyling that will help in displaying the user data
out = Label(Frame_2, font=('Montserrat', 20, 'bold'), fg='black',
            bg='white')
out.grid(row=0, column=0, padx=150, pady=10)
# Dimensions and sytyling that will help in displaying the user data
out_1 = Label(Frame_2, font=('Montserrat', 15, 'bold'), fg='black',
              bg='white')
out_1.grid(row=1, column=0, padx=30, pady=10)
# Dimensions and sytyling that will help in displaying the user data
out_2 = Label(Frame_2, font=('Montserrat', 15, 'bold'), fg='black',
              bg='white')
out_2.grid(row=2, column=0, padx=30, pady=10)
# Dimensions and sytyling that will help in displaying the user data
out_3 = Label(Frame_2, font=('Montserrat', 15, 'bold'), fg='black',
              bg='white')
out_3.grid(row=3, column=0, padx=30, pady=10)
# Dimensions and sytyling that will help in displaying the user data
out_4 = Label(Frame_2, font=('Montserrat', 15, 'bold'), fg='black',
              bg='white')
out_4.grid(row=4, column=0, padx=30, pady=10)
# Dimensions and sytyling that will help in displaying the user data
out_5 = Label(Frame_2, font=('Montserrat', 15, 'bold'), fg='black',
              bg='white')
out_5.grid(row=5, column=0, padx=30, pady=10)

# Creating the third frame
Frame_3 = Frame(root, bg="white", relief=RIDGE, bd=15)
Frame_3.place(x=10, y=615, width=1260, height=100)

# Defining buttons dimensions and style
button_1 = Button(Frame_1, text='Submit Order', font=('Arial', 15, 'bold'), bg='yellow', fg='black', width=20,
                  command=output)
button_1.grid(row=5, column=1, pady=10)
# Defining buttons dimensions and style
button_2 = Button(Frame_3, text='Exit', font=('Arial', 15, 'bold'), bg='yellow', fg='black', width=20,
                  command=ask)
button_2.grid(row=0, column=3, padx=130, pady=15)

# Calling the mainloop with the tkinter function to enable display of the user interface 
root.mainloop()
